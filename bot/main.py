from handlers.unknown_command import app_bot

#бесконечная работа бота начинающаяся и заканчивающаяся соответствующими фразами
try:
    print("Bot is working")
    app_bot.polling() 
finally:
    print("Shutting down")