from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
   
engine = create_engine(f"postgresql+psycopg2://test_wallet_user:hardpassword@localhost:5432/wallets")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
