from typing import List

from fastapi import APIRouter, Depends, status

from ..models import games as game_model
from ..services.games import GameService
from ..services.users import UserSerivce

router = APIRouter(
    prefix="/games",
    tags=["games"],
)


@router.get(
    "/",
    response_model=List[game_model.Game],
)
def get_games(game_service: GameService = Depends()):
    """List all games."""
    return game_service.get_all()


@router.get(
    "/{game_id}",
    response_model=game_model.Game,
)
def get_game(game_id: int, game_service: GameService = Depends()):
    """Get particular game."""
    return game_service.get(game_id)


@router.post(
    "/",
    response_model=game_model.Game,
    status_code=status.HTTP_201_CREATED,
)
def create_game(
    user_id: int,
    user_service: UserSerivce = Depends(),
    game_service: GameService = Depends(),
):
    """Create new game."""
    user = user_service.get(user_id)
    return game_service.create(user.id)
