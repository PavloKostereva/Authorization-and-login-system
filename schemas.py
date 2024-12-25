from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    age: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        from_attributes = True  # Заміна orm_mode на from_attributes

class PostBase(BaseModel):
    id: int
    title: str
    body: str
    author_id: int

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    author_id: User

    class Config:
        from_attributes = True  # Заміна orm_mode на from_attributes
