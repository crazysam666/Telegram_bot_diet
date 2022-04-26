from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import Database

db = Database('dietbase.db')


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class OrderCalc(StatesGroup):
    waiting_for_parametr_age = State()
    waiting_for_parametr_height = State()
    waiting_for_parametr_weight = State()
    
# обработчик первого шага, 
# реагирующий на команду /calc (регистрировать его будем позднее):
async def calc_start(message: types.Message):
    await message.answer("Укажите Ваш возраст:")
    await OrderCalc.waiting_for_parametr_age.set()

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено.")
    
    # Обратите внимание: есть второй аргумент
async def parametr_age(message: types.Message, state: FSMContext):
    if not message.text.isalnum():
        await message.answer("Пожалуйста, укажите возраст корректно цифрами без пробелов.")
        return
    else:
        await state.update_data(age=int(message.text))

    # Для последовательных шагов можно не указывать название состояния, обходясь next()
    await OrderCalc.waiting_for_parametr_height.set()
    await message.answer("Теперь укажите Ваш рост цифрами в сантиметрах, с точность до 1 знака после точки. Например: 179.5".format())

async def parametr_height(message: types.Message, state: FSMContext):
    if not is_number(message.text):
        await message.answer("Пожалуйста, укажите рост корректно: без пробелов, 1 знак после точки!".format())
        return
    else:
        await state.update_data(height=float(message.text))

# Для последовательных шагов можно не указывать название состояния, обходясь next()
    await OrderCalc.waiting_for_parametr_weight.set()
    await message.answer("Теперь укажите Ваш вес (напишите цифрами в кг,\n\
с точность до 1 знака после точки (например: 50.5)):".format())

async def parametr_weight(message: types.Message, state: FSMContext):
    if not is_number(message.text):
        await message.answer("Пожалуйста, укажите вес корректно - цифрами без пробелов, с точностью до 1 знака после точки!".format())
        return
    else:
        await state.update_data(weight=float(message.text))
    user_data = await state.get_data()
    imt = round(user_data['weight']/(user_data['height']/100)**2)
    i_w = round((user_data['height'] - 110) * 1.15)
    await message.answer(f"Ваш индекс массы тела = {imt}\nВаш идеальный вес = {i_w} кг. Также посмотрите норму коэффициента для Вас в таблице по команде '\carts'".format())
    await state.finish()

def register_handlers_calc(dp: Dispatcher):
    dp.register_message_handler(calc_start, commands="calc", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(parametr_age, state=OrderCalc.waiting_for_parametr_age)
    dp.register_message_handler(parametr_height, state=OrderCalc.waiting_for_parametr_height)
    dp.register_message_handler(parametr_weight, state=OrderCalc.waiting_for_parametr_weight)







