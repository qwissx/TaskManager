from pydantic import BaseModel


class SUserCreate(BaseModel):
    id: int
    username: str
    profile_id: int

class SUserDisplay(BaseModel):
    username: str