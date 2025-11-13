from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    user_id: str
    thread_id: str
    query: str
    top_k: int = 3

class SourceDoc(BaseModel):
    source: Optional[str]
    content: Optional[str]

class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceDoc]
