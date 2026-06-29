import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


load_dotenv()
notifying_user_id = os.getenv("USER_ID")

bot = TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

def notify(name, email, subject, message):
    text = f"У Вас новое обращение!\n\nОт: {name}\nEmail: {email}\nТема: {subject}\nСообщение:\n{message}"
    bot.send_message(notifying_user_id, text)
    
    