from fastapi import FastAPI

from config.database import Base, engine

from models.user import User
from models.tag import Tag
from models.task import Task
from models.task_tag import TaskTag
from models.subtask import Subtask

from routes import subtask_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestor de Tareas",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Gestor de Tareas API"}


app.include_router(subtask_routes.router)