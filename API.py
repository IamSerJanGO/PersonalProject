import aiogram
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

TOKEN_API = '6712465987:AAEY7cCPbp8BhcBjtzcf1zc1m6K1XRLHE54'  # Авторизационный токен
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