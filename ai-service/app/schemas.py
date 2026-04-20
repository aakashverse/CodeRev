from pydantic import BaseModel
from typing import List

class FileInput(BaseModel):
    path: str
    content: str

class ReviewRequest(BaseModel):
    files: List[FileInput]

class ReviewResponse(BaseModel):
    review: str
    issues: List[str]
    suggestions: List[str]
    severity: str
