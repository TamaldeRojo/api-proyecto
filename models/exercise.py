from pydantic import BaseModel
from typing import Optional

class Exercise(BaseModel):
    id: Optional[str]
    userID: str
    Type: str
    Count: int