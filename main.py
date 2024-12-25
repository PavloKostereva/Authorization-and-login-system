# main.py
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Base, User, Post
from typing import List
from database import engine, session_local
from schemas import UserCreate, PostCreate, User as DbUser, PostResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Перемістіть цей виклик після визначення моделей

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts/", response_model=PostResponse)
async def create_post(post: PostCreate, db: Session = Depends(get_db)) -> PostResponse:
    db_user = db.query(User).filter(User.id == post.author_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return PostResponse(id=db_post.id, title=db_post.title, body=db_post.body, author_id=db_user.id)


@app.get("/posts/", response_model=List[PostResponse])
async def posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@app.get("/users/{name}", response_model=DbUser)
async def posts(name: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == name).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db.query(Post).all()
