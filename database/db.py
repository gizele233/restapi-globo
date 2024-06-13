from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

url = 'postgresql://postgres:ap1rickmorty@localhost/rickmortydata'
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base = declarative_base()


def insert_character_into_database(data, model):
    for item in data['results']:
        character = model(
            name=item['name'],
            species=item['species'],
            gender=item['gender']
        )
        session.add(character)
    session.commit()


def insert_episode_into_database(data, model):
    for item in data['results']:
        record = model(
            name=item['name'],
            air_date=item['air_date'],
            episode=item['episode']
        )
        session.add(record)
    session.commit()
