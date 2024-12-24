from fastapi import APIRouter, HTTPException
from app.schemas.task_schema import TaskCreate, TaskResponse
from app.services.task_service import TaskService
from app.utils.logger import logger
from app.utils.task_validators import validate_task_data

router = APIRouter()
task_service = TaskService()


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    try:
        logger.info("Received request to create a task")
        validate_task_data(task)
        return task_service.create_task(title=task.title, priority=task.priority)
    except HTTPException as e:
        logger.error("Validation error: %s", e.detail)
        raise e
    except Exception as e:
        logger.error("Error creating task: %s", e)
        raise HTTPException(status_code=500, detail="An error occurred while creating the task")


@router.get("/", response_model=list[TaskResponse])
def get_tasks():
    try:
        logger.info("Received request to fetch all tasks")
        return task_service.get_all_tasks()
    except Exception as e:
        logger.error("Error fetching tasks: %s", e)
        raise HTTPException(status_code=500, detail="An error occurred while fetching tasks")


@router.post("/{task_id}/complete")
def complete_task(task_id: int):
    try:
        logger.info("Received request to complete task ID %d", task_id)
        task = task_service.complete_task(task_id)
        if not task:
            logger.warning("Task ID %d not found", task_id)
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task marked as complete"}
    except Exception as e:
        logger.error("Error completing task ID %d: %s", task_id, e)
        raise HTTPException(status_code=500, detail="An error occurred while completing the task")
