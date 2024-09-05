# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

from fastapi import FastAPI
from .routers import item_router
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(item_router.router)