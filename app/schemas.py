from pydantic import BaseModel
from typing import List

class ItemBase(BaseModel):
    name: str
    description: str
    price: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    available: int

class Item(ItemBase):
    id: int
    available: int

    class Config:
        orm_mode = True