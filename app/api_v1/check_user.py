from fastapi import APIRouter, Depends, status
from pydantic.networks import EmailStr

from ..models.check_user import CheckOutput
from ..services.check_user import CheckUserService

router = APIRouter(
    prefix="/check",
    tags=["check user"],
)


@router.post(
    "/",
    response_model=CheckOutput,
    status_code=status.HTTP_201_CREATED,
)
def check_user(email: EmailStr, check_service: CheckUserService = Depends()):
    return check_service.check(email)
