from pydantic import BaseModel

from app.models.task import Priority


class TaskCreate(BaseModel):
    title: str
    priority: Priority


class TaskResponse(BaseModel):
    id: int
    title: str
    priority: Priority
    is_done: bool
