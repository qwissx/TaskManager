from abc import ABC

from repositories.repository import Repository
from sqlalchemy.ext.asyncio import AsyncSession


class BaseDAO(ABC):
    class_obj = None
    not_find_exception = None

    @classmethod
    async def add_object(cls, conn: AsyncSession, **data):
        object = await Repository.add(cls.class_obj, conn, **data)
        return object

    @classmethod
    async def get_object(cls, conn: AsyncSession, **filter_by):
        object = await Repository.get(cls.class_obj, conn, **filter_by)
        if not object:
            raise cls.not_find_exception
        return object
        
    @classmethod
    async def delete_obj(cls, conn: AsyncSession, **filter_by):
        await cls.get_object(conn, **filter_by)
        await Repository.delete(cls.class_obj, conn, **filter_by)