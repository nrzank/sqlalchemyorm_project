import os
from dotenv import load
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load()
URL = os.getenv('URL_STRING')
engine = create_engine(
    URL
    # echo=True
)

Session = sessionmaker(bind=engine)

Base = declarative_base()
