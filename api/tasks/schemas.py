from datetime import date

from pydantic import BaseModel


class STaskCreate(BaseModel):
    dead_line: date
    description: str
    profile_id: int

class STaskDisplay(BaseModel):
    id: int
    dead_line: date
    description: str