from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your actual MySQL connection details
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/petpaw_db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL queries for debugging
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

