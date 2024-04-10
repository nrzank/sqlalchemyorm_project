import os
from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import sessionmaker

from dotenv import load

load()
LOGIN = os.getenv('LOGIN')

engine = create_engine(
    LOGIN
)

Session = sessionmaker(bind=engine)
