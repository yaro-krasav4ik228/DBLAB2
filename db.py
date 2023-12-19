from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URI = "postgresql+psycopg2://postgres:banana@localhost:5432/postgres"

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
