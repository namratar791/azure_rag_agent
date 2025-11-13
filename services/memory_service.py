from typing import Dict
from models.state import RAGState

# Global thread state memory (in production, use Redis or SQL)
THREAD_SESSIONS: Dict[str, RAGState] = {}

def get_or_create_session(user_id: str, thread_id: str) -> RAGState:
    key = f"{user_id}:{thread_id}"
    if key not in THREAD_SESSIONS:
        THREAD_SESSIONS[key] = RAGState(user_id=user_id, thread_id=thread_id)
    return THREAD_SESSIONS[key]
