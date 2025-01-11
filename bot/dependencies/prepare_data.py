from datetime import date

from telebot.types import Message


def prepare_data_user(message: Message, **extra_data):
    data_user = {
        'id': message.from_user.id,
        'username': message.from_user.username,
    }
    for key, val in extra_data.items():
        data_user[key] = val
    return data_user

def prepare_data_profile(name: str):
    data_profile = {
        'name': name,
        'level': 0
    }
    return data_profile

def prepare_data_task(description: str, dead_line: date, profile_id: int):
    data_task = {
        'dead_line': dead_line,
        'description': description,
        'profile_id': profile_id,
    }
    return data_task