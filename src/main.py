from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.database import Base, engine

from models.user import User
from models.tag import Tag
from models.task import Task
from models.task_tag import TaskTag
from models.subtask import Subtask

from routers import user_router, task_router, tag_router, subtask_router, auth_router

app = FastAPI(title="Gestor de Tareas", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)
app.include_router(task_router.router)
app.include_router(tag_router.router)
app.include_router(subtask_router.router)
app.include_router(auth_router.router)


@app.get("/")
def root():
    return {"message": "Gestor de Tareas API"}