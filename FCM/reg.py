from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import Database
import datetime


db = Database('dietbase.db')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class OrderReg(StatesGroup):
    waiting_name = State()
    waiting_age = State()
    waiting_height = State()
    waiting_weight = State()

# Реагирующий на команду /reg:
async def reg_start(message: types.Message):
    await message.answer("Укажите Вашу Фамилию и имя: \n(например: Иванова Наталья)")
    await OrderReg.waiting_name.set()

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено.")

# Устанавливаем "name"
async def parametr_name(message: types.Message, state: FSMContext):
    await state.update_data(name=str(message.text))
    user_data = await state.get_data()
    await OrderReg.waiting_age.set()
    await message.answer("Теперь укажите Ваш возраст цифрами:")

# Устанавливаем "age"
async def parametr_age(message: types.Message, state: FSMContext):
    if not message.text.isalnum():
        await message.answer("Пожалуйста, укажите возраст корректно цифрами без пробелов.")
        return
    await state.update_data(age=int(message.text))
    user_data = await state.get_data()
    await OrderReg.waiting_height.set()
    await message.answer("Теперь укажите Ваш рост\n\
(напишите цифрами в метрах, 2 знака после точки(например: 1.60)):")

# Устанавливаем "height"
async def parametr_height(message: types.Message, state: FSMContext):
    if not is_number(message.text):
        await message.answer("Пожалуйста, укажите рост корректно: \n\
цифрами без пробелов, 2 знака после точки!")
        return
    await state.update_data(height=float(message.text))
    await OrderReg.waiting_weight.set()
    await message.answer("Теперь укажите Ваш вес (напишите цифрами в кг,\n\
с точность до 1 знака после точки (например: 50.5)):")

# Устанавливаем "weight"
async def parametr_weight(message: types.Message, state: FSMContext):
    if not is_number(message.text):
        await message.answer("Пожалуйста, укажите вес корректно - цифрами без пробелов,\n\
            с точностью до 1 знака после точки!")
        return
    await state.update_data(weight=float(message.text))
    user_data = await state.get_data()
    imt = round(user_data['weight']/((user_data['height'])**2), 1)
    db.set_users(message.from_user.id, user_data['name'], user_data['age'], user_data['height'], user_data['weight'], datetime.date.today())
    await message.answer(f"Ваш индекс массы тела = {imt}\n")
    await state.finish()

async def admin_start(message: types.Message):
    if message['from']['id'] == *********** or ***********:
        a = db.exists()
        await message.answer(a)
    else:
        await message.answer("Обратитесь к администратору!".format())


def register_handlers_reg(dp: Dispatcher):
    dp.register_message_handler(reg_start, text="💗 Регистрация", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(admin_start, commands="admin", state="*")
    dp.register_message_handler(parametr_name, state=OrderReg.waiting_name)
    dp.register_message_handler(parametr_age, state=OrderReg.waiting_age)
    dp.register_message_handler(parametr_height, state=OrderReg.waiting_height)
    dp.register_message_handler(parametr_weight, state=OrderReg.waiting_weight)



