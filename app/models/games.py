from pydantic import BaseModel


class GameBase(BaseModel):
    """Base schema for game."""

    pass


class Game(GameBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class GameCreate(GameBase):
    pass


class GameUpdate(GameBase):
    pass
