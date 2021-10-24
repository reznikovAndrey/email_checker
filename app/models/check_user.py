from pydantic import BaseModel


class CheckOutput(BaseModel):
    """Output after check email and count games."""

    esp: bool
    db: bool
    games: int
