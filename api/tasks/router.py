from connections import session_getter
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .dao import TaskDAO
from .schemas import STaskCreate

tasks_router = APIRouter(prefix="/tasks", 
                         tags=["Tasks"])
    

@tasks_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: STaskCreate, 
    connection: AsyncSession = Depends(session_getter)
):
    await TaskDAO.add_object(connection, **task_data.model_dump())    
    await connection.commit()
    return {"message": "task added successfully"}


@tasks_router.delete("/{task_id}/", status_code=status.HTTP_200_OK)
async def del_task(
    task_id: int,
    connection: AsyncSession = Depends(session_getter),
):
    await TaskDAO.delete_obj(connection, id=task_id)
    await connection.commit()
    return {"message": "task deleted successfully"}