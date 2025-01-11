import pytest

from api.connections import async_session_maker
from api.exceptions import UserNotFoundException
from api.users.dao import UserDAO
from api.users.models import User


@pytest.mark.asyncio
@pytest.mark.usefixtures('clean_repository', 'add_profile_for_user')
@pytest.mark.parametrize('input_data', [
    ({'id': 1, 'username': 'Bogdan', 'profile_id': 1}),
])
async def test_add_and_get_user_with_userDAO(input_data: dict):
    new_user = User(**input_data)

    async with async_session_maker() as conn:
        await UserDAO.add_object(conn, **input_data)
        result =  await UserDAO.get_object(conn, **input_data)

    assert result.id == new_user.id
    assert result.username == new_user.username


@pytest.mark.asyncio
@pytest.mark.usefixtures('clean_repository', 'add_profile_for_user')
@pytest.mark.parametrize('input_data,filter_by', [
    ({'id': 1, 'username': 'Bogdan', 'profile_id': 1}, {'id': 1}),
    ({'id': 1, 'username': 'Bogdan', 'profile_id': 1}, {'username': 'Bogdan'}),
    ({'id': 1, 'username': 'Bogdan', 'profile_id': 1}, {'id': 1, 'username': 'Bogdan'}),
])
async def test_add_del_get_user_with_userDAO(input_data: dict, filter_by: dict):
    async with async_session_maker() as conn:
        await UserDAO.add_object(conn, **input_data)
        await UserDAO.delete_obj(conn, **filter_by)

        with pytest.raises(UserNotFoundException):
            assert await UserDAO.get_object(conn, **filter_by) 
