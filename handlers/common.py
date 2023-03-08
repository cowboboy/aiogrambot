from aiogram import types
from create_bot import bot
from aiogram import Dispatcher
from keyboards import kb_client

async def echo_send(message : types.message):
    await bot.send_message(message.from_user.id, message.text, reply_markup=kb_client)

def register_handlers_common(dp : Dispatcher):
    dp.register_message_handler(echo_send)