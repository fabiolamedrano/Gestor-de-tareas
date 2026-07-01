from fastapi import FastAPI

app = FastAPI(
    title = "Gestor de Tareas",
    version = "1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Gestor de Tareas API"}