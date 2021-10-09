from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from setting.database import get_db
from src.schemas import BaseSchemas
from src.controller import TaxController


router = APIRouter()


@router.post("", response_model=BaseSchemas.Receipt)
def get_reciept_calculation(
    itemInput: BaseSchemas.ItemInput, db: Session = Depends(get_db)
):
    taxRate = TaxController.taxRate(db)
    item = TaxController.calculateReceipt(db, itemInput, taxRate)
    return item


@router.get("", response_model=BaseSchemas.itemType)
def item_type(itemInput: str):
    item_type_name = TaxController.analyse_item(itemInput)
    return item_type_name
