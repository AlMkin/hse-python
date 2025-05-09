from app.repositories.task_repository import TaskRepository
from app.utils.logger import logger


class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    def create_task(self, title: str, priority: str):
        logger.info("Creating a new task with title '%s' and priority '%s'", title, priority)
        new_task = self.repository.add_task(title=title, priority=priority)
        logger.info("Task created successfully with ID: %s", new_task.id)
        return new_task

    def get_all_tasks(self):
        logger.info("Fetching all tasks")
        tasks = self.repository.get_tasks()
        logger.info("Fetched %d tasks", len(tasks))
        return tasks

    def complete_task(self, task_id: int):
        logger.info("Marking task ID %d as complete", task_id)
        task = self.repository.update_task_status(task_id, is_done=True)
        if task:
            logger.info("Task ID %d marked as complete", task_id)
        else:
            logger.warning("Task ID %d not found", task_id)
        return task
