from fastapi import BackgroundTasks, Depends
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from ..db import tables
from ..db.database import get_session
from ..esp.esp import Esp, esp
from ..models.check_user import CheckOutput
from ..services.games import GameService


class CheckUserService:
    """Main logic."""

    def __init__(
        self,
        background_tasks: BackgroundTasks,
        db_session: Session = Depends(get_session),
        esp_session: Esp = Depends(),
        game_service: GameService = Depends(),
    ) -> None:
        self.db_session = db_session
        self.esp_session = esp_session
        self.game_serivce = game_service
        self.background_tasks = background_tasks

    def check(self, email: EmailStr) -> CheckOutput:
        """Check user`s email.

        Check that email with given email in db.
        If true:
            - add game in db.
            - count games.
        If false:
            - check email in esp.
            - add email in esp if email not in esp.
            - create new user with given email.
            - increment games count.
        """
        user = (
            self.db_session.query(
                tables.User,
            )
            .filter(
                tables.User.email == email,
            )
            .first()
        )
        if user:
            self.game_serivce.create(user.id)
            games = (
                self.db_session.query(tables.Game)
                .filter(
                    tables.Game.user_id == user.id,
                )
                .count()
            )
            data = {
                "esp": True,
                "db": True,
                "games": games,
            }
            return CheckOutput(**data)
        in_esp: bool = esp.check_user_email(email)
        if not in_esp:
            self.background_tasks.add_task(esp.add_user_email, email)
        new_user = tables.User(email=email)
        self.db_session.add(new_user)
        self.db_session.commit()
        new_game = tables.Game(user_id=new_user.id)
        self.db_session.add(new_game)
        self.db_session.commit()
        data = {
            "esp": in_esp,
            "db": False,
            "games": 1,
        }
        return CheckOutput(**data)
