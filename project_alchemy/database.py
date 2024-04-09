import os
from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load

load()
LOGIN = os.getenv('LOGIN')

engine = create_engine(
    LOGIN,
    echo=True
)

Session = sessionmaker(bind=engine)

Base = declarative_base()
