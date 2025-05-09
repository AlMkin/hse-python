from enum import Enum

from pydantic import BaseModel


class Priority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"


class Task(BaseModel):
    id: int
    title: str
    priority: Priority
    is_done: bool = False
