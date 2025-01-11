from pydantic import BaseModel
from tasks.schemas import STaskDisplay


class SProfileCreate(BaseModel):
    name: str
    level: float

class SProfileDisplay(BaseModel):
    id: int
    name: str
    level: float
    tasks: list[STaskDisplay] = []