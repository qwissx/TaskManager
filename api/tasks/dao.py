from dao import BaseDAO
from exceptions import TaskNotFoundException

from .models import Task


class TaskDAO(BaseDAO):
    class_obj = Task
    not_find_exception = TaskNotFoundException