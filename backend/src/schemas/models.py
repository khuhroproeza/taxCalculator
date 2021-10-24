from datetime import date
from typing import List
from setting.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
)


class Receipt(Base):
    __tablename__ = "Receipt"
    id = Column(Integer, primary_key=True)
    TaxType = Column(String, nullable=False)
    Itemtype = Column(String, nullable=False)
    item = Column(String, nullable=False)
    tax = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    created_at = created_at = Column(DateTime, nullable=False)


class Taxtype(Base):
    __tablename__ = "TaxType"
    id = Column(Integer, primary_key=True)
    TaxType = Column(String, nullable=False)
    Percentage = Column(Float, nullable=False)
