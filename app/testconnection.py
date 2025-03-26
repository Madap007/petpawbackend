from sqlalchemy import text
from database import engine, SessionLocal

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1")).fetchone()
        print("Connection successful, result:", result)
except Exception as e:
    print("Database connection error:", e)