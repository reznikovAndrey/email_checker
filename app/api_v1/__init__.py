from fastapi import APIRouter

from . import users, games

router = APIRouter()

router.include_router(users.router)
router.include_router(games.router)
