from app.utils.file_manager import load_tasks_from_file, save_tasks_to_file
from app.models.task import Task


class TaskRepository:
    def __init__(self):
        self.tasks = [Task(**task) for task in load_tasks_from_file()]

    def add_task(self, title: str, priority: str) -> Task:
        task = Task(id=self._generate_id(), title=title, priority=priority)
        self.tasks.append(task)
        self._save_to_file()
        return task

    def get_tasks(self) -> list[Task]:
        return self.tasks

    def update_task_status(self, task_id: int, is_done: bool) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                task.is_done = is_done
                self._save_to_file()
                return task
        return None

    def _generate_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def _save_to_file(self):
        save_tasks_to_file([task.dict() for task in self.tasks])
