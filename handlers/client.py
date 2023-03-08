from aiogram import types
from create_bot import bot
from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardRemove

async def command_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id, "Здравствуйте", reply_markup=ReplyKeyboardRemove())
        await message.delete()
    except:
        await message.reply("Напишите боту в ЛС")

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])

