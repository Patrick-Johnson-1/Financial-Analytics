from fastapi import FastAPI, Depends
from sqlalchemy import text
from database import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/health")
async def root():
    return {"status": "healthy"}

@app.get("/db-test")
async def db_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {"db_connected": True}