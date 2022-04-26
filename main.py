import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand
from auth_data import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
# photo = open('usr//bot//imt.png', 'rb')



async def set_commands(bot: Bot):
    commands = [
        BotCommand(text="💗 Регистрация", description="Регистрация"),
        BotCommand(text="✅ Рекомендации", description="Рекомендации"),
        BotCommand(text="📏 Вес", description="Измерение веса"),
        BotCommand(command="/calc", description="Посчитать ИМТ"),
        BotCommand(command="/links", description="Ссылки"),
        BotCommand(command="/cancel", description="Отменить текущее действие"),
        BotCommand(command="/admin", description="Посмотреть пользователей"),
        BotCommand(command="/carts", description="Отправить картинки")
    ]
    await bot.set_my_commands(commands)



# @dp.message_handler(commands=['carts'])
# async def send_carts(message: types.Message):   
#     await bot.send_photo(chat_id=message.chat.id, photo=photo)


# --- Авторизация ---
# def auth(func):
#     async def wrapper(message):
#         if message['from']['id'] != **********:
#             return await message.reply("Для работы с ботом обратитесь к администратору!", reply=False)
#         return await func(message)
#     return wrapper

# реагирующий на команду /admin:
# @auth




if __name__ == '__main__':
    from handlers import dp
    from FCM import register_handlers_upd, register_handlers_reg, register_handlers_calc
     # Регистрация хэндлеров
    register_handlers_calc(dp)
    register_handlers_reg(dp)
    register_handlers_upd(dp)
    executor.start_polling(dp, skip_updates = True)

# --- Ответ на смайл смайлом ---
# @dp.message_handler(content_types=[types.ContentType.ANIMATION])
# async def echo_document(message: types.Message):
#     await message.reply_animation(message.animation.file_id)



# # --- Ответ на какой то текст в сообщении ---
# @dp.message_handler(content_types=['text'])
# async def echo_document(message: types.Message):
#     if message.text.lower() == "пока":
#         await message.answer("пока")


# @dp.message_handler()
# async def bot_message(message: types.Message):
#     if message.text == '🍜 Рандомное меню':
#         await bot.send_message(message.from_user.id, "Ваше число: " + str(random.randint(1000, 9999)))

#     elif message.text == '⏪ Главное меню':
#         await bot.send_message(message.from_user.id, '⏪ Главное меню', reply_markup = nav.mainMenu)
    
#     elif message.text == '🍸 Другое':
#         await bot.send_message(message.from_user.id, '🍸 Другое', reply_markup = nav.otherMenu)

#     elif message.text == '💆 Информация':
#         await bot.send_message(message.from_user.id, '💆 Информация', reply_markup = nav.profMenu)

#     elif message.text == '👀 Профиль':
#         await bot.send_message(message.from_user.id, 'Информация профиля')

#     elif message.text == '💗 Подписка':
#         await bot.send_message(message.from_user.id, 'Страничка инсты')

#     elif message.text == '🍰 Калькулятор тела':
#         await bot.send_message(message.from_user.id, 'Калькулятор тела')
    
#     else:
#         await message.reply('Неизвестная команда')



