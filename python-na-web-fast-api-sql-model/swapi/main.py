# tudo que se refere ao FastAPI
from fastapi import FastAPI
from swapi.db import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def hello_world():
    return {"details": "Hello T23!!"}
