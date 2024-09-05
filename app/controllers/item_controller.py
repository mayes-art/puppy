from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import Item
from ..schemas import ItemCreate, ItemUpdate

class ItemController:

    def get_items(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Item).offset(skip).limit(limit).all()

    def get_item(self, db: Session, item_id: int):
        item = db.query(Item).filter(Item.id == item_id).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    
    def create_item(self, db: Session, item: ItemCreate):
        db_item = Item(name=item.name, description=item.description, price=item.price)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def update_item(self, db: Session, item_id: int, item: ItemUpdate):
        db_item = self.get_item(db, item_id)
        for key, value in item.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item

    def delete_item(self, db: Session, item_id: int):
        db_item = self.get_item(db, item_id)
        db.delete(db_item)
        db.commit()
        return db_item