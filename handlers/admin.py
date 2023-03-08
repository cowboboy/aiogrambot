from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from create_bot import bot
from keyboards import admin_kb

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def is_moderator(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Включены админ-функции.", reply_markup=admin_kb.kb_admin)
    await message.delete()

async def cm_start(message : types.Message):
    if ID == message.from_user.id:
        await FSMAdmin.photo.set()
        await message.reply("Загрузите фото.")

async def load_photo(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Введите название.")

async def load_name(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите описание.")

async def load_description(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите цену.")

async def load_price(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    await sqlite_db.sql_add_command(state)
    await state.finish()

async def cancel_handler(message : types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await state.reply("Ок.")

def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands="Загрузить", state=None)
    dp.register_message_handler(load_photo, content_types = ["photo"], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state="*", commands="отмена")
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(is_moderator, commands=["Админка"], is_chat_admin=True)



