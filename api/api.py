from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database.db import SessionLocal
from models.character import Character
from models.episode import Episode

app = FastAPI()


class CharacterModel(BaseModel):
    name: str
    species: str
    gender: str

    class Config:
        from_attributes = True


class EpisodeModel(BaseModel):
    name: str
    air_date: str
    episode: str

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/characters/", response_model=CharacterModel)
def create_character(character: CharacterModel, db: Session = Depends(get_db)):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


@app.get("/characters/", response_model=List[CharacterModel])
def read_characters(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    characters = db.query(Character).offset(skip).limit(limit).all()
    return characters


@app.get("/characters/{character_id}", response_model=CharacterModel)
def read_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(
        Character.id == character_id
    ).first()
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@app.put("/characters/{character_id}", response_model=CharacterModel)
def update_character(
    character_id: int,
    character: CharacterModel,
    db: Session = Depends(get_db)
):
    db_character = db.query(Character).filter(
        Character.id == character_id
    ).first()
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    for key, value in character.dict().items():
        setattr(db_character, key, value)
    db.commit()
    db.refresh(db_character)
    return db_character


@app.delete("/characters/{character_id}", response_model=CharacterModel)
def delete_character(character_id: int, db: Session = Depends(get_db)):
    db_character = db.query(Character).filter(
        Character.id == character_id
    ).first()
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(db_character)
    db.commit()
    return db_character


@app.post("/episodes/", response_model=EpisodeModel)
def create_episode(episode: EpisodeModel, db: Session = Depends(get_db)):
    db_episode = Episode(**episode.dict())
    db.add(db_episode)
    db.commit()
    db.refresh(db_episode)
    return db_episode


@app.get("/episodes/", response_model=List[EpisodeModel])
def read_episodes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    episodes = db.query(Episode).offset(skip).limit(limit).all()
    return episodes


@app.get("/episodes/{episode_id}", response_model=EpisodeModel)
def read_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if episode is None:
        raise HTTPException(status_code=404, detail="Episode not found")
    return episode


@app.put("/episodes/{episode_id}", response_model=EpisodeModel)
def update_episode(
    episode_id: int,
    episode: EpisodeModel,
    db: Session = Depends(get_db)
):
    db_episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if db_episode is None:
        raise HTTPException(status_code=404, detail="Episode not found")
    for key, value in episode.dict().items():
        setattr(db_episode, key, value)
    db.commit()
    db.refresh(db_episode)
    return db_episode


@app.delete("/episodes/{episode_id}", response_model=EpisodeModel)
def delete_episode(episode_id: int, db: Session = Depends(get_db)):
    db_episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if db_episode is None:
        raise HTTPException(status_code=404, detail="Episode not found")
    db.delete(db_episode)
    db.commit()
    return db_episode
