import asyncio
from API import bot, dp, MAIN_KeyboardButton
from aiogram import types
from aiogram.filters import Command
from aiogram.methods import DeleteWebhook
from logic import *
from aiogram.fsm.context import FSMContext








async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)
