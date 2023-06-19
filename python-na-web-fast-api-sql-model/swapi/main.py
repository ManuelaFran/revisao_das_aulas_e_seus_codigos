# tudo que se refere ao FastAPI
from fastapi import FastAPI
from sqlmodel import Session, select
from swapi.model import Planet
from swapi.db import create_db_and_tables, engine
from swapi.db_populate import populate_empty_tables

app = FastAPI()


def get_session():
    return Session(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

    with get_session() as session:
        populate_empty_tables(session)


def create_response(result):
    return {
        "count": len(result),
        "next": None,
        "previous": None,
        "results": result,
    }


@app.get("/")
async def hello_world():
    return {"details": "Hello T23!!"}


@app.get("/api/planets/", tags=["planets"])
async def list_planets():
    with get_session() as session:
        planets = session.exec(select(Planet)).all()
        return create_response(planets)
