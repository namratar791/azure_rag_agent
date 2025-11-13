from azure.ai.openai import OpenAIClient
from azure.ai.openai import ChatMessage, ChatCompletionsOptions
from config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT

openai_client = OpenAIClient(credential=AZURE_OPENAI_KEY, endpoint=AZURE_OPENAI_ENDPOINT)

def generate_answer(context: str, query: str):
    """Generate LLM answer based on context"""
    prompt = f"""
You are an AI assistant that answers using the given sources.
Question: {query}

Context:
{context}

If you don't find the answer, respond: 'I'm not sure, but I can find out for you.'
Include source references.
"""
    messages = [
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content=prompt),
    ]
    options = ChatCompletionsOptions(messages=messages, max_tokens=600, temperature=0)
    response = openai_client.get_chat_completions(deployment_id=AZURE_OPENAI_DEPLOYMENT, options=options)
    return response.choices[0].message.content
