import requests
import settings
from telebot.types import Message

from .add_task import app_bot


@app_bot.message_handler(commands=['del_task'])
def del_task(message: Message):
    profile_request = requests.get(f"{settings.API_URL}/profiles/{message.from_user.id}/")
    profile = profile_request.json()
    tasks = profile['tasks']

    text = f"Tell me, which one do you want to delete(enter dead line):\n"
    for task in tasks:
        task_info = f"Description: {task['description']}, dead line: {task['dead_line']}\n\n"
        text += task_info

    app_bot.send_message(message.chat.id, text)
    app_bot.register_next_step_handler(message, get_task_dead_line, tasks)


def get_task_dead_line(message: Message, tasks):
    task_pattern = message.text

    task_id = None
    for task in tasks:
        if task['dead_line'] == task_pattern:
            task_id = task['id']
            break

    if not task_id:
        text = "Sorry, I can't find this task."
        app_bot.send_message(message.chat.id, text)
        return 

    requests.delete(f"{settings.API_URL}/tasks/{task_id}/")

    text = "Okay, I deleted your task."
    app_bot.send_message(message.chat.id, text)