from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from .abstract_repository import AbstractRepository


class Repository(AbstractRepository):

    @classmethod
    async def add(cls, class_obj, connection:  AsyncSession, **data) -> None:
        query = insert(class_obj).values(**data)
        await connection.execute(query)

    @classmethod
    async def get(cls, class_obj, connection: AsyncSession, **filter_by):
        query = select(class_obj).filter_by(**filter_by)
        result = await connection.execute(query)
        return result.scalar_one_or_none()
    
    @classmethod
    async def delete(cls, class_obj, connection: AsyncSession, **filter_by) -> None:
        deleted_obj = delete(class_obj).filter_by(**filter_by)
        await connection.execute(deleted_obj)

    @classmethod
    async def execute_query(cls, query, connection: AsyncSession):
        class_obj = await connection.execute(query)
        return class_obj