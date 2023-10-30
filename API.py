import aiogram
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

TOKEN_API = ''  # Авторизационный токен
bot = aiogram.Bot(TOKEN_API)
dp = aiogram.Dispatcher()

MAIN_KeyboardButton = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='-Записаться')
    ],
    [
        KeyboardButton(text='-Отменить запись ')
    ]
], resize_keyboard=True)
