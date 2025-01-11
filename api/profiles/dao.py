from dao import BaseDAO
from exceptions import ProfileNotFoundException
from profiles.models import Profile
from repositories.repository import Repository
from sqlalchemy import insert, join, select
from sqlalchemy.ext.asyncio import AsyncSession
from tasks.models import Task
from users.models import User


class ProfileDAO(BaseDAO):
    class_obj = Profile
    not_find_exception = ProfileNotFoundException

    @classmethod
    async def get_profile_by_user_id(cls, connection: AsyncSession, user_id):
        """
        SELECT Porfile FROM Profile
        JOIN User ON User.profile_id = Profile.id
        WHERE User.id = user_id
        """

        profile_query = (
                select(Profile)
                .select_from(join(User, Profile, User.profile_id == Profile.id))
                .where(User.id == user_id)
            )
        
        profile_request = await Repository.execute_query(profile_query, connection)
        profile = profile_request.scalar()
        
        """
        SELECT Task FROM tasks
        WHERE Task.profile_id = profile.id
        """

        tasks_query = (
            select(Task).where(Task.profile_id == profile.id)
        )

        tasks_request = await Repository.execute_query(tasks_query, connection)
        tasks = tasks_request.scalars().all()

        profile = profile.__dict__
        profile['tasks'] = []

        for task in tasks:
            profile['tasks'].append(task.__dict__)

        return profile

        
    
    @classmethod
    async def add_object(cls, connection: AsyncSession, **data):
        query = (
            insert(cls.class_obj)
            .values(**data)
            .returning(cls.class_obj)
        )
        profile = await Repository.execute_query(query, connection)
        return profile.scalar()