import requests
import settings
from telebot.types import Message

from .registration import app_bot


@app_bot.message_handler(commands=['get_profile'])
def get_profile(message: Message):
    text = "Please waite, searching your profile..."
    bot_message = app_bot.send_message(message.chat.id, text) # отправляем сообщение и запоминаем его чтобы удалить в будущем

    profile_response = requests.get(f"{settings.API_URL}/profiles/{message.from_user.id}/") # получаем данные о профиле
    profile = profile_response.json()

    text = f"Here you go, this is information about you: \n{profile['name']} level {profile['level']}\nTasks:\n"
    for task in profile['tasks']:
        task_info = f"{task['description']} before {task['dead_line']}\n\n"
        text += task_info

    app_bot.delete_message(message.chat.id, message_id=bot_message.message_id) # удаляем сообщение и отправляем пользователю его данные
    app_bot.send_message(message.chat.id, text)