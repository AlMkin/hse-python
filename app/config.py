from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TASKS_FILE: str = "tasks.txt"


settings = Settings()
