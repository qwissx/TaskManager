import requests
import settings
from dependencies.prepare_data import prepare_data_profile, prepare_data_user
from telebot.types import Message

from .welcome_handler import app_bot
from dependencies.check_exist import check_exist_user


# регистрация пользователя
@app_bot.message_handler(commands=["registration"])
def start_message(message: Message):
    if check_exist_user(message):
        text = "Looks like you are already in system."
        app_bot.send_message(message.chat.id, text)
        return 

    text = "Let's create an account for you. Create your username."
    app_bot.send_message(message.chat.id, text)
    app_bot.register_next_step_handler(message, get_username)


def get_username(message: Message):
    name = message.text

    profile_data = prepare_data_profile(name)  # готовим данные для отправки
    request = requests.post(
        f"{settings.API_URL}/profiles", json=profile_data # делаем обращение к апи чтобы добавить новый профиль
    )  

    user_data = prepare_data_user(message, profile_id=request.json().get("id"))
    requests.post(
        f"{settings.API_URL}/users", json=user_data # делам обращение к апи чтобы добавить пользователя
    )  

    text = f"Okay, glad to see you {name}!"
    app_bot.send_message(message.chat.id, text)
