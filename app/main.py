from fastapi import FastAPI
from app.routers import task_router
from app.utils.file_manager import load_tasks_from_file
from app.utils.logger import logger

app = FastAPI(title="Task Manager API")


@app.on_event("startup")
def startup_event():
    try:
        logger.info("Starting up the server and loading tasks from file")
        load_tasks_from_file()
        logger.info("Tasks loaded successfully")
    except Exception as e:
        logger.error("Error during startup: %s", e)


app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
