from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/wallets/{wallet_id}/operation", response_model=schemas.WalletResponse)
def perform_operation(
    wallet_id: str, 
    operation: schemas.OperationRequest, 
    db: Session = Depends(get_db)
):
    try:
        wallet = crud.perform_operation(db, wallet_id, operation.operation_type, operation.amount)
        return wallet
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))