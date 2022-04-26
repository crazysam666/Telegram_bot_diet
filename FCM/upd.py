from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import Database
import datetime
from text import rec1

db = Database('dietbase.db')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class Upd_Weight(StatesGroup):
    waiting_weight = State()

# реагирующий на команду /update:
async def upd_start(message: types.Message):
    await message.answer("Укажите Ваш новый вес, с точностью до знака после точки. например: 60.5 или 56.0".format())
    await Upd_Weight.waiting_weight.set() # Ожидание ввода данных

# Обновляем данные в таблице reg:
async def upd_weight(message: types.Message):
    db.update_weight(message.from_user.id, message.text, datetime.date.today())
    await message.answer("Данные обновлены!")

# По кнопке ✅ Рекомендации:
async def recom(message: types.Message):
    await message.answer(rec1)
    

def register_handlers_upd(dp: Dispatcher):
    dp.register_message_handler(upd_start, text="📏 Вес", state="*")
    dp.register_message_handler(recom, text="✅ Рекомендации", state="*")    
    dp.register_message_handler(upd_weight, state=Upd_Weight.waiting_weight)
