from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from passlib.context import CryptContext

from models import User, Book, Movie, Rating, Recommendation
from sqlmodel import Session, select
from database import get_session
from schemas import (
    UserCreate, UserRead, UserUpdate,
    BookCreate, BookRead, BookUpdate,
    MovieCreate, MovieRead, MovieUpdate,
    RatingCreate, RatingRead,
    RecommendationRead
)

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

@router.post("/users/", response_model=UserRead, status_code=status.HTTP_201_CREATED, tags=["users"])
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.username == user.username)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username já existe")
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password)
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.put("/users/{user_id}", response_model=UserRead, tags=["users"])
def update_user(user_id: int, user_update: UserUpdate, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    if user_update.username is not None:
        user.username = user_update.username
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.password is not None:
        user.hashed_password = get_password_hash(user_update.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.post("/ratings/", response_model=RatingRead, status_code=status.HTTP_201_CREATED, tags=["ratings"])
def create_rating(rating: RatingCreate, session: Session = Depends(get_session)):
    if not rating.book_id and not rating.movie_id:
        raise HTTPException(status_code=400, detail="Uma avaliação deve estar associada a um livro ou filme.")
    db_rating = Rating.from_orm(rating)
    session.add(db_rating)
    session.commit()
    session.refresh(db_rating)
    return db_rating