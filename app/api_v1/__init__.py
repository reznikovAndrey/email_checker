from fastapi import APIRouter

from . import users, games, check_user

router = APIRouter()

router.include_router(users.router)
router.include_router(games.router)
router.include_router(check_user.router)
