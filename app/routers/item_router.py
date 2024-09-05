from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database
from ..schemas import Item, ItemCreate, ItemUpdate
from ..services.item_service import ItemService

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

item_service = ItemService()

@router.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return item_service.get_items(db, skip=skip, limit=limit)

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    return item_service.get_item(db, item_id)

@router.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db, item)

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    return item_service.update_item(db, item_id, item)

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return item_service.delete_item(db, item_id)

