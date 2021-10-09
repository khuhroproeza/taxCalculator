from enum import Enum


class TaxTypes(str, Enum):
    IMPORT = "imported_item"
    LOCAL = "local_item"


class ItemType(str, Enum):
    BOOKS = "books"
    FOOD = "food"
    MEDICAL = "medical"
    OTHER = "other"
