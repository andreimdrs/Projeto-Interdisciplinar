from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel

# Usuário
class UserBase(SQLModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str  # senha em texto plano, será convertida para hash

class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

# Livro
class BookBase(SQLModel):
    title: str
    author: Optional[str] = None
    description: Optional[str] = None
    cover_url: Optional[str] = None
    external_id: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int

    class Config:
        orm_mode = True

class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    cover_url: Optional[str] = None
    external_id: Optional[str] = None

# Filme
class MovieBase(SQLModel):
    title: str
    director: Optional[str] = None
    description: Optional[str] = None
    cover_url: Optional[str] = None
    external_id: Optional[str] = None

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int

    class Config:
        orm_mode = True

class MovieUpdate(SQLModel):
    title: Optional[str] = None
    director: Optional[str] = None
    description: Optional[str] = None
    cover_url: Optional[str] = None
    external_id: Optional[str] = None

# Avaliação
class RatingBase(SQLModel):
    user_id: int
    book_id: Optional[int] = None
    movie_id: Optional[int] = None
    score: float
    comment: Optional[str] = None

class RatingCreate(RatingBase):
    pass

class RatingRead(RatingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Recomendação
class RecommendationBase(SQLModel):
    user_id: int

class RecommendationRead(RecommendationBase):
    id: int
    recommended_books: Optional[List[int]] = None
    recommended_movies: Optional[List[int]] = None
    created_at: datetime

    class Config:
        orm_mode = True