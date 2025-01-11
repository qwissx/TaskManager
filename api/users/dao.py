from dao import BaseDAO
from exceptions import UserNotFoundException
from users.models import User


class UserDAO(BaseDAO):
    class_obj = User
    not_find_exception = UserNotFoundException