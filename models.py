from sqlalchemy import Column, Integer, String, Float, DateTime, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from database import Base

class DimCompany(Base):
    __tablename__ = 'dim_company'
    company_id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(10), unique=True, nullable=False)
    name = Column(String(50))
    sector = Column(String(100))
    industry = Column(String(100))
    market_cap = Column(Float())
    country = Column(String(15))
    last_updated = Column(DateTime)

class DimDate(Base):
    __tablename__ = 'dim_date'
    date_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    year = Column(Integer)
    quarter = Column(Integer)
    month = Column(Integer)
    month_name = Column(String(15))
    day_of_week = Column(Integer)
    day_name = Column(String(15))
    is_weekend = Column(Boolean)
    week_of_year = Column(Integer)