from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    """Base schema for user."""

    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
