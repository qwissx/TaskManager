import pytest

from api.connections import async_session_maker
from api.profiles.models import Profile
from api.repositories.repository import Repository
from api.users.models import User


@pytest.mark.asyncio
@pytest.mark.usefixtures('clean_repository')
@pytest.mark.parametrize('input_data', [
    ({'id': 1, 'name': 'qwissx', 'level': 0}),
])
async def test_add_and_get_profile_from_repository(input_data: dict):
    async with async_session_maker() as conn:
        new_profile = Profile(**input_data)
        await Repository.add(Profile, conn, **input_data)
        output_profile = await Repository.get(Profile, conn, **input_data)

        assert output_profile.id == new_profile.id
        assert output_profile.name == new_profile.name
        assert output_profile.level == new_profile.level


@pytest.mark.asyncio
@pytest.mark.usefixtures('clean_repository')
@pytest.mark.parametrize('input_data,filter_by', [
    ({'id': 1, 'name': 'qwissx', 'level': 0}, {'id': 1}),
    ({'id': 1, 'name': 'qwissx', 'level': 0}, {'name': 'qwissx'}),
    ({'id': 1, 'name': 'qwissx', 'level': 0}, {'level': 0}),
])
async def test_add_del_get_profile_from_repository(input_data: dict, filter_by: dict):
    async with async_session_maker() as conn:
        await Repository.add(Profile, conn, **input_data)
        await Repository.delete(Profile, conn, **filter_by)
        output = await Repository.get(Profile, conn, **filter_by)

        assert output is None

 
@pytest.mark.asyncio
@pytest.mark.usefixtures('clean_repository', 'add_profile_for_user')
@pytest.mark.parametrize('input_data', [
    ({'id': 1, 'username': 'Bogdan', 'profile_id': 1}),
])
async def test_add_and_get_user_from_repository(input_data: dict):
    async with async_session_maker() as conn:
        new_user = User(**input_data)
        await Repository.add(User, conn, **input_data)
        output_user = await Repository.get(User, conn, **input_data)

        assert output_user.id == new_user.id 
        assert output_user.username == new_user.username


@pytest.mark.asyncio
@pytest.mark.usefixtures('clean_repository', 'add_profile_for_user')
@pytest.mark.parametrize('input_data,filter_by', [
    ({'id': 1, 'username': 'Bogdan', 'profile_id': 1}, {'id': 1}),
    ({'id': 1, 'username': 'Bogdan', 'profile_id': 1}, {'username': 'Bogdan'}),
    ({'id': 1, 'username': 'Bogdan', 'profile_id': 1}, {'id': 1, 'username': 'Bogdan'}),
])
async def test_add_del_get_user_from_repository(input_data: dict, filter_by: dict):
    async with async_session_maker() as conn:
        await Repository.add(User, conn, **input_data)
        await Repository.delete(User, conn, **filter_by)
        output = await Repository.get(User, conn, **filter_by)

        assert output is None