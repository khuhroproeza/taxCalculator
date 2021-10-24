from pydantic import BaseModel
from datetime import date
from typing import List
from src.enums import TaxTypes
from src.enums import ItemType


class ItemInput(BaseModel):
    item: str = None
    Itemtype: ItemType = None
    TaxType: TaxTypes = None
    quantity: int = None
    price: float = None


class Receipt(BaseModel):
    id: int = None
    item: str = None
    Itemtype: ItemType = None
    TaxType: TaxTypes = None
    quantity: int = None
    price: float = None
    total: float = None
    tax: float = None
    created_at: date = None

    class Config:
        orm_mode = True


class itemType(BaseModel):
    item: str = None


class Taxtype(BaseModel):
    id: int = None
    TaxType: TaxTypes = None
    Percentage: float = None
