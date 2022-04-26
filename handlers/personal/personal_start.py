from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter

import markups as nav
from main import dp



@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup = nav.mainMenu)

@dp.message_handler(commands=['links'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/natali_***********/"),
        types.InlineKeyboardButton(text="Администратор", url="https://t.me/**********")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)


