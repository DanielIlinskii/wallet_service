from sqlalchemy.orm import Session
from .models import Wallet
from decimal import Decimal

def perform_operation(db: Session, wallet_id: str, operation_type: str, amount: float):
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).with_for_update().first()
    if not wallet:
        raise ValueError("Wallet not found")

    if operation_type == "DEPOSIT":
        wallet.balance += Decimal(amount)
    elif operation_type == "WITHDRAW":
        if wallet.balance < Decimal(amount):
            raise ValueError("Insufficient funds")
        wallet.balance -= Decimal(amount)
    
    db.commit()
    db.refresh(wallet)
    return wallet