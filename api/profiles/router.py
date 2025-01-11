from connections import session_getter
from fastapi import APIRouter, Depends, status
from profiles.schemas import SProfileCreate, SProfileDisplay
from sqlalchemy.ext.asyncio import AsyncSession

from .dao import ProfileDAO

profile_router = APIRouter(prefix="/profiles",
                           tags=["Profiles"])


@profile_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_profile(
    profile_data: SProfileCreate,
    connection: AsyncSession = Depends(session_getter)
) -> dict[str, int]:
    profile = await ProfileDAO.add_object(connection, **profile_data.model_dump())
    await connection.commit()
    return {'id': profile.id}


@profile_router.get("/{user_id}/")
async def get_profile_by_user_id(
    user_id: int,
    connection: AsyncSession = Depends(session_getter)
) -> SProfileDisplay:
    profile = await ProfileDAO.get_profile_by_user_id(connection, user_id)
    return profile