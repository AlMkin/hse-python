from fastapi import HTTPException
from app.models.task import Priority
from app.schemas.task_schema import TaskCreate


def validate_task_data(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    if task.priority not in Priority:
        raise HTTPException(status_code=400, detail=f"Invalid priority. Must be one of {[p.value for p in Priority]}")
