from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton


 # --- Main Menu ---
btnReg = KeyboardButton('💗 Регистрация')
btnRecom = KeyboardButton('✅ Рекомендации')
btnWeight = KeyboardButton('📏 Вес')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True).add(btnReg, btnRecom, btnWeight)


# # ---Btn main ---``
# btnMain = KeyboardButton('⏪ Главное меню')

# # --- Main Menu ---
# btnRandom = KeyboardButton('🍜 Рандомное меню')
# btnOther = KeyboardButton('🍸 Другое')
# mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnOther)

# # --- Other Menu ---
# btnInfo = KeyboardButton('💆 Информация')
# btnCalc = KeyboardButton('🍰 Калькулятор тела')
# otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnCalc, btnMain)


