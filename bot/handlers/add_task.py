from datetime import date

import requests
import settings
from dependencies.prepare_data import prepare_data_task
from telebot.types import Message

from .get_profile import app_bot


@app_bot.message_handler(commands=["add_task"]) # добавление таски пользователю
def add_task(message: Message):
    text = "Okay, let's create new task. Tell me her description."
    app_bot.send_message(message.chat.id, text)
    app_bot.register_next_step_handler(message, get_description)


def get_description(message: Message):
    description = message.text
    text = "Now, let's set the due date. Please, fill in the date with the appropriate format: YYYY-MM-DD."
    app_bot.send_message(message.chat.id, text)
    app_bot.register_next_step_handler(message, get_dead_line, description)


def get_dead_line(message: Message, description):
    dead_line: date = message.text
    text = "Good, let me remember your task..."
    bot_message = app_bot.send_message(message.chat.id, text)

    profile_request = requests.get(
        f"{settings.API_URL}/profiles/{message.from_user.id}/"
    )

    profile_id = profile_request.json().get("id")
    task_data = prepare_data_task(description, dead_line, profile_id)
    
    task_request = requests.post(
        f"{settings.API_URL}/tasks",
        json=task_data,
    )

    text = f"Okay, now you have your new task.\n{description} before {dead_line}."
    app_bot.delete_message(message.chat.id, message_id = bot_message.message_id)
    app_bot.send_message(message.chat.id, text)