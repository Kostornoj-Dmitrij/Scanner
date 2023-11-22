import telebot
from telebot import types

# Токен вашего бота Telegram
TOKEN = '6425319786:AAEScENXwLGMGqKdhD3xiJwxk_DgK-aos-8'
bot = telebot.TeleBot(TOKEN)

user_balance = {'user_id': 1000}  # Пример баланса пользователя


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    if user_id not in user_balance:
        user_balance[user_id] = 0
    bot.send_message(user_id, "Привет! Добро пожаловать в бота.")


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_id = message.chat.id
    if message.text == '/profile':
        show_profile(user_id)
    elif message.text == '/pay':
        show_payment_options(user_id)
    elif message.text == '/support':
        show_support_options(user_id)
    elif message.text == '/info':
        show_bot_info(user_id)
    elif message.text == '/stat':
        show_statistics(user_id)
    else:
        bot.send_message(user_id, "Извините, не могу обработать этот запрос.")


def show_profile(user_id):
    balance = user_balance[user_id]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton('О боте', callback_data='info'))
    keyboard.row(types.InlineKeyboardButton('Статистика', callback_data='stat'))
    keyboard.row(types.InlineKeyboardButton('Поддержка', callback_data='support'))
    bot.send_message(user_id, f"Ваш баланс: {balance} руб", reply_markup=keyboard)


def show_payment_options(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton('100 руб', callback_data='100'),
                 types.InlineKeyboardButton('300 руб', callback_data='300'),
                 types.InlineKeyboardButton('500 руб', callback_data='500'))
    bot.send_message(user_id, "Выберите сумму для пополнения:", reply_markup=keyboard)


def show_support_options(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton('Написать в поддержку', url='https://t.me/your_support_bot'),
                 types.InlineKeyboardButton('Личный кабинет', callback_data='profile'))
    bot.send_message(user_id, "Выберите действие:", reply_markup=keyboard)


def show_bot_info(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Личный кабинет', callback_data='profile'))
    bot.send_message(user_id, "Информация о боте...", reply_markup=keyboard)


def show_statistics(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Личный кабинет', callback_data='profile'))
    bot.send_message(user_id, "Статистика...", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data in ['100', '300', '500']:
        user_id = call.message.chat.id
        user_balance[user_id] += int(call.data)
        bot.answer_callback_query(call.id, text=f"Счет успешно пополнен на {call.data} руб")
        bot.send_message(user_id, "Баланс успешно пополнен!")
    elif call.data == 'profile':
        show_profile(call.message.chat.id)
    elif call.data == 'info':
        show_bot_info(call.message.chat.id)
    elif call.data == 'stat':
        show_statistics(call.message.chat.id)
    elif call.data == 'support':
        show_support_options(call.message.chat.id)
    else:
        bot.answer_callback_query(call.id, text="Ошибка!")


@bot.message_handler(content_types=['photo', 'document'])
def handle_content(message):
    user_id = message.chat.id
    if message.photo or message.document:
        cost = len(message.photo) * 0.2 if message.photo else 0.2
        if user_balance[user_id] < cost:
            show_payment_options(user_id)
        else:
            # Логика обработки изображений/файлов и формирование результата
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(types.KeyboardButton('pdf'), types.KeyboardButton('txt'))
            keyboard.add(types.KeyboardButton('doc'), types.KeyboardButton('xlsx'))
            bot.send_message(user_id, "Выберите итоговый формат файла-результата:", reply_markup=keyboard)
            user_balance[user_id] -= cost
    else:
        bot.send_message(user_id, "Извините, не умею работать с таким форматом данных.")


bot.polling()