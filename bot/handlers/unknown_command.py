from telebot.types import Message

from .del_task import app_bot


#хэндлер если пользователь будет присылать хуйню 
@app_bot.message_handler(func=lambda message: True)
def unknown_command(message: Message):
    text = "Sorry, I don't know this command."
    app_bot.reply_to(message, text)