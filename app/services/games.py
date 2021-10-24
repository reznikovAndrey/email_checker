from typing import List, Optional

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from ..db.database import get_session
from ..db import tables


class GameService:
    """Service for game."""

    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get(self, game_id: int) -> tables.Game:
        game = self._get(game_id)
        return game

    def get_all(self) -> List[tables.Game]:
        games = self.session.query(tables.Game).all()
        return games

    def create(
        self,
        user_id: int,
    ) -> tables.Game:
        game = tables.Game(user_id=user_id)
        self.session.add(game)
        self.session.commit()
        return game

    def _get(self, game_id: int) -> Optional[tables.Game]:
        game = (
            self.session.query(
                tables.Game,
            )
            .filter(
                tables.Game.id == game_id,
            )
            .first()
        )
        if not game:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return game
