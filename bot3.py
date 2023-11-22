from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import telebot
from telebot import types
import subprocess
from img_formatter import process_image
import tempfile
import requests


TOKEN = '6425319786:AAEScENXwLGMGqKdhD3xiJwxk_DgK-aos-8'
bot = telebot.TeleBot(TOKEN)

user_balance = {'user_id': 0}
user_data = {}
form = 'pdf'
file_path = ''

def save_image_from_telegram(file_path, file_name):
    file_url = f'https://api.telegram.org/file/bot{TOKEN}/{file_path}'
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f'Изображение успешно сохранено как {file_name}')
    else:
        print('Не удалось загрузить изображение')

def create_res_file(user_id, form):

    true_suffix = '.' + form
    if form == 'pdf':
        temp_pdf_file = BytesIO()
        pdf_canvas = canvas.Canvas(temp_pdf_file, pagesize=letter)
        pdf_canvas.drawString(100, 100, "Файл результат")
        pdf_canvas.save()
        temp_pdf_file.seek(0)
        temp_pdf_file.name = 'result.pdf'
        bot.send_document(user_id, temp_pdf_file)
    else:
        with tempfile.NamedTemporaryFile(suffix=true_suffix, delete=False, mode='w', encoding='utf-8') as temp_file:
            temp_file.write('Итоговый файл')
        with open(temp_file.name, 'rb') as file:
            bot.send_document(user_id, file)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    if user_id not in user_balance:
        user_balance[user_id] = 1000

    keyboard = types.InlineKeyboardMarkup()

    keyboard.row(types.InlineKeyboardButton('Личный кабинет', callback_data='profile'),
                 types.InlineKeyboardButton('Начать работу', callback_data='start_sending'))

    bot.send_message(user_id, "Привет! Добро пожаловать в бота.", reply_markup=keyboard)

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
    keyboard.add(types.InlineKeyboardButton('О боте', callback_data='info'))
    keyboard.add(types.InlineKeyboardButton('Статистика', callback_data='stat'))
    keyboard.add(types.InlineKeyboardButton('Поддержка', callback_data='support'))
    keyboard.add(types.InlineKeyboardButton('Пополнение баланса', callback_data='pay'))

    bot.send_message(user_id, f"Ваш баланс: {balance} руб", reply_markup=keyboard)


def show_payment_options(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton('100 руб', callback_data='100'),
                 types.InlineKeyboardButton('300 руб', callback_data='300'),
                 types.InlineKeyboardButton('500 руб', callback_data='500'))
    keyboard.row(types.InlineKeyboardButton('1000 руб', callback_data='1000'),
                 types.InlineKeyboardButton('1500 руб', callback_data='1500'),
                 types.InlineKeyboardButton('2000 руб', callback_data='2000'))

    bot.send_message(user_id, "Выберите сумму для пополнения:", reply_markup=keyboard)


def show_support_options(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Написать в поддержку', url='https://www.google.com'))
    keyboard.add(types.InlineKeyboardButton('Личный кабинет', callback_data='profile'))

    bot.send_message(user_id, "Выберите действие:", reply_markup=keyboard)


def show_bot_info(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Личный кабинет', callback_data='profile'))
    bot.send_message(user_id, "Это бот сканер", reply_markup=keyboard)


def show_statistics(user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Личный кабинет', callback_data='profile'))
    bot.send_message(user_id, "Статистика...", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_id = call.message.chat.id
    global files
    if call.data in ['100', '300', '500', '1000', '1500', '2000']:

        user_balance[user_id] += float(call.data)
        bot.answer_callback_query(call.id, text=f"Счет успешно пополнен на {call.data} руб")
        bot.send_message(user_id, "Баланс успешно пополнен!")

    elif call.data == 'profile':
        show_profile(call.message.chat.id)
    elif call.data == 'pay':
        show_payment_options(call.message.chat.id)
    elif call.data == 'info':
        show_bot_info(call.message.chat.id)
    elif call.data == 'stat':
        show_statistics(call.message.chat.id)
    elif call.data == 'support':
        show_support_options(call.message.chat.id)
    elif call.data == 'start_sending':
        bot.send_message(user_id, "Отправьте фото")
    elif call.data in ['pdf', 'txt', 'doc', 'xml']:
        create_res_file(user_id, call.data)
    else:
        bot.answer_callback_query(call.id, text="Ошибка!")


@bot.message_handler(content_types=['photo', 'document'])
def handle_content(message):
    user_id = message.chat.id
    cost = float(0.2)

    if user_balance[user_id] < cost:
        bot.send_message(user_id, "На балансе недостаточно средств!")
        show_payment_options(user_id)
    file_id = None
    if (message.document and message.document.mime_type in ['application/pdf', 'image/png', 'image/jpeg', 'image/jpg']):
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        save_image_from_telegram(file_path, 'result_img.jpg')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton('pdf', callback_data='pdf'),
                     types.InlineKeyboardButton('txt', callback_data='txt'),
                     types.InlineKeyboardButton('doc', callback_data='doc'),
                     types.InlineKeyboardButton('xml', callback_data='xml'))
        bot.send_message(user_id, "Выберите итоговый формат файла-результата:", reply_markup=keyboard)

        user_balance[user_id] -= cost
    else:
        bot.send_message(user_id, "Извините, не умею работать с таким форматом данных.")
        return

bot.polling()