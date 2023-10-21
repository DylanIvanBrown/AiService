from pydantic import BaseModel
from typing import Optional


class CompletionResponse(BaseModel):
    ai_response: str
