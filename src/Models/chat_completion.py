from pydantic import BaseModel
from typing import Optional


class ChatCompletion(BaseModel):
    user_message: str
    context: [str] | None
    system_prompt: Optional[str]
    preferred_model: Optional[str]
