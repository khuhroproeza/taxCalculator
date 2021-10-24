from datetime import datetime
from sqlalchemy.orm import Session
from src.schemas import BaseSchemas
from src import enums
from src.schemas import BaseSchemas
from src.schemas import models
from src.helpers import itemAnalyser
from src.helpers.itemAnalyser import proper_round


def taxRate(db: Session):
    taxRate = models.Taxtype
    return db.query(taxRate)


def calculateReceipt(
    db: Session, itemInput: BaseSchemas.ItemInput, taxRate: BaseSchemas.Taxtype
):
    tax_rate = {}
    total_tax = 0
    for rate in taxRate:
        tax_rate[rate.TaxType] = rate.Percentage
    item_type_tax_rate = tax_rate[itemInput.TaxType]
    item_type = itemInput.Itemtype

    tax_allowed_on_type = [enums.ItemType.OTHER]

    if itemInput.TaxType == enums.TaxTypes.IMPORT:
        total_tax = item_type_tax_rate
    if item_type in tax_allowed_on_type:
        total_tax = total_tax + tax_rate[enums.TaxTypes.LOCAL]
    total_tax = (total_tax * itemInput.price) / 100
    total_tax = proper_round(total_tax)
    total_price = (
        total_tax
        + itemInput.price  # float(str(round(round(itemInput.price / 0.05) * 0.05, 2)))
        * itemInput.quantity
    )

    tax_receipt_orm = models.Receipt(**itemInput.dict(exclude_unset=True))
    tax_receipt_orm.tax = total_tax * itemInput.quantity
    tax_receipt_orm.total = total_price
    tax_receipt_orm.created_at = datetime.utcnow()

    db.add(tax_receipt_orm)
    db.commit()

    db.refresh(tax_receipt_orm)
    return tax_receipt_orm


def analyse_item(string):
    item = BaseSchemas.itemType()
    item.item = itemAnalyser.find_item_type(string)

    return item
