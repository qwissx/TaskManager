import pytest_asyncio
from connections import Base, async_session_maker, engine
from profiles.models import Profile
from repositories.repository import Repository


@pytest_asyncio.fixture
async def clean_repository():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture
async def add_profile_for_user():
    profile_data = {'id': 1, 'name': 'qwissx', 'level': 0}
    async with async_session_maker() as conn:
        await Repository.add(Profile, conn, **profile_data)
        await conn.commit()