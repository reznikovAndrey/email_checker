from typing import List

from fastapi import APIRouter, Depends, status

from ..models import users as user_model
from ..services.users import UserSerivce

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/",
    response_model=List[user_model.User],
)
def get_users(user_serivce: UserSerivce = Depends()):
    """List all available users."""
    return user_serivce.get_all()


@router.get(
    "/{user_id}",
    response_model=user_model.User,
)
def get_user(user_id: int, user_serivce: UserSerivce = Depends()):
    """Get particular user."""
    return user_serivce.get(user_id)


@router.post(
    "/",
    response_model=user_model.User,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: user_model.UserCreate,
    user_service: UserSerivce = Depends(),
):
    """Create new user."""
    return user_service.create(user_data)
