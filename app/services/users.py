from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from ..db.database import get_session
from ..db import tables
from ..models import users as user_model


class UserSerivce:
    """Service for user."""

    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get(self, user_id: int) -> tables.User:
        user = (
            self.session.query(
                tables.User,
            )
            .filter(
                tables.User.id == user_id,
            )
            .first()
        )
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return user

    def get_all(self) -> List[tables.User]:
        users = self.session.query(tables.User).all()
        return users

    def create(self, user_data: user_model.UserCreate) -> tables.User:
        user = tables.User(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user
