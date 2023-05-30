from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = declarative_base()

engine = create_engine("postgresql://postgres:postgres@localhost:5433/flask_db")

session = sessionmaker(bind=engine)

