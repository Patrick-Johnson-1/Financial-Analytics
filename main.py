from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import DimCompany, DimDate

app = FastAPI()

@app.get("/health")
async def root():
    return {"status": "healthy"}

@app.get("/db-test")
async def db_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {"db_connected": True}

Base.metadata.create_all(bind=engine, checkfirst=True)