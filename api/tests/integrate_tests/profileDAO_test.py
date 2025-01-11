import pytest

from api.connections import async_session_maker
from api.profiles.dao import ProfileDAO
from api.profiles.models import Profile
from api.users.dao import UserDAO
from api.users.models import User


@pytest.mark.asyncio
@pytest.mark.usefixtures('clean_repository')
@pytest.mark.parametrize('input_profile_data,input_user_data', [
    ({'name': 'qwissx', 'level': 0}, {'id': 1, 'username': 'Bogdan', 'profile_id': 1}),
])
async def test_add_and_get_profile_with_profileDAO(input_profile_data: dict, input_user_data: dict):
    new_profile = Profile(**input_profile_data)
    new_user = User(**input_user_data)

    async with async_session_maker() as conn:
        await ProfileDAO.add_object(conn, **input_profile_data)
        await UserDAO.add_object(conn, **input_user_data)

        output_profile = await ProfileDAO.get_profile_by_user_id(conn, user_id=new_user.id)

    assert output_profile['name'] == new_profile.name
    assert output_profile['level'] == new_profile.level