import finnhub
import time
from datetime import date, timedelta, datetime
from config import get_settings, WATCHLIST
from database import SessionLocal
from models import DimDate, DimCompany

settings = get_settings()
client = finnhub.Client(api_key=settings.FINNHUB_API_KEY)
db = SessionLocal()

# --- Seed dim_date ---
start_date = date.today() - timedelta(days=365)

for i in range(365):
    d = start_date + timedelta(days=i)

    dim_date = DimDate(
        date_id=int(d.strftime("%Y%m%d")),
        date=d,
        year=d.year,
        quarter=(d.month - 1) // 3 + 1,
        month=d.month,
        month_name=d.strftime("%B"),
        day_of_week=d.weekday(),
        day_name=d.strftime("%A"),
        is_weekend=d.weekday() >= 5,
        week_of_year=d.isocalendar()[1]
    )
    db.add(dim_date)

db.commit()
print(f"Seeded {365} dates")

# --- Seed dim_company ---
for symbol in WATCHLIST:
    profile = client.company_profile2(symbol=symbol)

    company = DimCompany(
        symbol=symbol,
        name=profile.get("name"),
        sector=profile.get("finnhubIndustry"),
        industry=profile.get("finnhubIndustry"),
        market_cap=profile.get("marketCapitalization"),
        country=profile.get("country"),
        last_updated=datetime.utcnow()
    )
    db.add(company)
    print(f"Added {symbol}: {profile.get('name')}")
    time.sleep(1)

db.commit()
db.close()
print("Seeding complete")