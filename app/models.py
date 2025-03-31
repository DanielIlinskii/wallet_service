import sqlalchemy
from sqlalchemy import Column, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = sqlalchemy.orm.declarative_base()

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(String, primary_key=True, index=True)  # юид
    balance = Column(Numeric(10,2), default=0.00)

