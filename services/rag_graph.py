from langgraph.graph import StateGraph, END
from models.state import RAGState
from services.search_service import retrieve_context
from services.openai_service import generate_answer

def build_rag_graph():
    graph = StateGraph()

    # Step 1: Retrieve docs
    def retrieve_step(state: RAGState):
        state.context_docs = retrieve_context(state.memory.load_memory_variables({})["chat_history"][-1].content, 3)
        return state

    # Step 2: Generate answer
    def generate_step(state: RAGState):
        context = "\n\n".join([f"Source: {d['source']}\n{d['content']}" for d in state.context_docs])
        user_query = state.memory.load_memory_variables({})["chat_history"][-1].content
        answer = generate_answer(context, user_query)
        state.last_answer = answer
        return state

    # Graph definition
    graph.add_node("retrieve", retrieve_step)
    graph.add_node("generate", generate_step)
    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)
    return graph
