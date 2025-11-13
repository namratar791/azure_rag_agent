from typing import List, Dict, Optional
from langgraph.graph import StateGraph, END
from langchain_core.messages import AIMessage, HumanMessage
from langchain.memory import ConversationBufferMemory

class RAGState:
    """Holds conversation state per user/thread"""
    def __init__(self, user_id: str, thread_id: str):
        self.user_id = user_id
        self.thread_id = thread_id
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.context_docs: List[Dict] = []
        self.last_answer: Optional[str] = None

