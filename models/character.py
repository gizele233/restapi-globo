from database.db import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    species = Column(String)
    gender = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
