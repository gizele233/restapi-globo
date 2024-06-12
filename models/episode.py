from database.db import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


class Episode(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    air_date = Column(String)
    episode = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
