from dependencies.check_exist import check_exist_user
from telebot.types import Message

from bot import app_bot


#приветственное сообщение, которое делает обращение к апи, чтобы узнать есть ли пользователь в системе 
@app_bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    text = "Hi, I'm your Task Manager. Let me look if you in system." 
    app_bot.send_message(message.chat.id, text)

    if check_exist_user(message):
        text = "Looks like you are already in system. So what do you want to do?"
        app_bot.send_message(message.chat.id, text)
    else:
        text = "Let's start our trip together. For the beginning you need to /registration first."
        app_bot.send_message(message.chat.id, text)