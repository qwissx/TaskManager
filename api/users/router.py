from connections import session_getter
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .dao import UserDAO
from .schemas import SUserCreate, SUserDisplay

users_router = APIRouter(prefix="/users",
                         tags=["Users"])


@users_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: SUserCreate,
    connection: AsyncSession = Depends(session_getter)
) -> dict[str, str]:
    await UserDAO.add_object(connection, **user_data.model_dump())
    await connection.commit()
    return {"message": "user added successfully"}


@users_router.get("/{user_id}/")
async def get_user_by_id(
    user_id: int,
    connection: AsyncSession = Depends(session_getter)
) -> SUserDisplay:
    user = await UserDAO.get_object(connection, id=user_id)
    return user