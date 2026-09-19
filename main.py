from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()

task_queue = []

class Task(BaseModel):
    outfit_id: str
    raw_text: str
    category: str
    side: str
    stand: str
    paths: Dict[str, str]

@app.get("/")
def home():
    return {"status": "Servidor funcionando perfeitamente!"}

@app.post("/add-task")
def add_task(task: Task):
    task_queue.append(task.dict())
    return {"status": "ok"}

@app.get("/get-task")
def get_task():
    if len(task_queue) > 0:
        return task_queue.pop(0)
    return {}
