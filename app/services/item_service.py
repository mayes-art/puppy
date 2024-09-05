from sqlalchemy.orm import Session
from ..controllers.item_controller import ItemController
from ..schemas import ItemCreate, ItemUpdate

class ItemService:
    
    def __init__(self):
        self.controller = ItemController()

    def get_items(self, db: Session, skip: int = 0, limit: int = 10):
        return self.controller.get_items(db, skip, limit)
    
    def get_item(self, db: Session, item_id: int):
        return self.controller.get_item(db, item_id)
    
    def create_item(self, db: Session, item: ItemCreate):
        return self.controller.create_item(db, item)
    
    def update_item(self, db: Session, item_id: int, item: ItemUpdate):
        return self.controller.update_item(db, item_id, item)
    
    def delete_item(self, db: Session, item_id: int):
        return self.controller.delete_item(db, item_id)