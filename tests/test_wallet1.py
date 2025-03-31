import sys, pytest
from pathlib import Path
from fastapi.testclient import TestClient
from decimal import Decimal
sys.path.append(str(Path(__file__).parent.parent))
from main import app
from app.database import SessionLocal
from sqlalchemy import text

client = TestClient(app)

def test_create_wallet():
    db = SessionLocal()
    db.execute(
            text("INSERT INTO wallets (id, balance) VALUES ('test_wallet15', :balance)"),
            {"balance": Decimal("0.00")}
        )
    db.commit()
    db.close()

    response = client.post(
        "/api/v1/wallets/test_wallet15/operation",
        json={"operation_type": "DEPOSIT", "amount": 0.0}
    )
    assert response.status_code == 200
    assert response.json()["balance"] == 0.0


def test_deposit():
    response = client.post(
        "/api/v1/wallets/test_wallet15/operation",
        json={"operation_type": "DEPOSIT", "amount": 1000}
    )
    assert response.status_code == 200
    assert response.json()["balance"] == 1000.0

def test_withdraw():

    response = client.post(
        "/api/v1/wallets/test_wallet15/operation",
        json={"operation_type": "WITHDRAW", "amount": 500}
    )
    assert response.status_code == 200
    assert response.json()["balance"] == 500.0


def test_insufficient_funds():
    response = client.post(
        "/api/v1/wallets/test_wallet15/operation",
        json={"operation_type": "WITHDRAW", "amount": 1000}
    )
    assert response.status_code == 400


def test_delete_wallet():
    db = SessionLocal()
    db.execute(
            text("DELETE FROM wallets WHERE id = 'test_wallet15'")
        )
    db.commit()
    db.close()

    response = client.get("/api/v1/wallets/test_wallet15")
    assert response.status_code == 404
