from pydantic import BaseModel

class OperationRequest(BaseModel):
    operation_type: str # deposit or withdraw
    amount: float

class WalletResponse(BaseModel):
    id: str
    balance: float