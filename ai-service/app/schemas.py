from pydantic import BaseModel
from typing import List

class FileInput(BaseModel):
    path: str
    content: str

class ReviewRequest(BaseModel):
    files: List[FileInput]

class ReviewResponse(BaseModel):
    file: str
    line: int
    review: str
    severity: str
    issues: List[str]
    fix: List[str]
