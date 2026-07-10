from fastapi import FastAPI

from config.database import Base, engine

from models.user import User
from models.tag import Tag
from models.task import Task
from models.task_tag import TaskTag
from models.subtask import Subtask

from routers import user_router, task_router, tag_router, subtask_router

app = FastAPI(title="Gestor de Tareas", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(task_router.router)
app.include_router(tag_router.router)
app.include_router(subtask_router.router)

@app.get("/")
def root():
    return {"message": "Gestor de Tareas API"}