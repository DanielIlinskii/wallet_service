from fastapi import FastAPI
from app.api.v1.endpoints import router as v1_router
from app.database import engine
from app.models import Base


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(v1_router, prefix="/api/v1")