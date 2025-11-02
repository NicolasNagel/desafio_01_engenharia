from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from include.database.db import Base

class BitcoinTable(Base):
    __tablename__ = 'bitcoin'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=True)
    base = Column(String, nullable=True)
    currency = Column(String, nullable=True)
    timestamp = Column(DateTime, default=func.now())