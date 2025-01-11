import requests
import settings
from telebot.types import Message


def check_exist_user(message: Message) -> bool:
    request = requests.get(f"{settings.API_URL}/users/{message.from_user.id}/") # обращение к апи с целью получения пользователя или 404 кода(его отсутсвие)

    if request.status_code == 404:
        return False
    return True