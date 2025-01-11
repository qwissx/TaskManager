from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    async def add(class_obj, coonection, **data):
        pass

    @abstractmethod
    async def get(class_obj, connection, **filter_by):
        pass

    @abstractmethod
    async def delete(class_obj, connection, **filter_by):
        pass

    @abstractmethod
    async def get_with_join(cls, class_obj, connection, id):
        pass