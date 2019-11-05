# ) Написать бота-консультанта, который будет собирать информацию с
# пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
# Записывать сформированную заявку в БД (по желанию SQl/NOSQL).).

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

import config
from models.botmodels import User, Request
import re

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    users_id_list = [i.user_id for i in User.objects()]
    if message.from_user.id not in users_id_list:
        user = User(**{"user_id": message.from_user.id}).save()
        bot.send_message(message.chat.id, "Добрый день! Вас приветствует бот-консультант. Мне нужно собрать информацию о Вас.")
    else:
        user = User.objects.get(user_id=message.from_user.id)
    if not user.fio:
        bot.send_message(message.chat.id, "Введите Ваще ФИО: ")
    elif not user.telephone_number:
        keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
        reg_button = KeyboardButton(text="Поделиться своим номером телефона", request_contact=True)
        keyboard.add(reg_button)
        bot.send_message(message.chat.id,"Укажите свой номер телеофна либо нажмите кнопку поделиться номером телефона", reply_markup=keyboard)
    elif not user.email:
        bot.send_message(message.chat.id, "Введите Ваш email: ")
    elif not user.address:
        bot.send_message(message.chat.id, "Введите Ваш адрес: ")
    elif not user.wishes:
        bot.send_message(message.chat.id, "Укажите Ваши пожелания: ")
    else:
        bot.send_message(message.chat.id, 'Я уже имею всю необходимую информацию о Вас. Ожидайте, менеджер свяжется с Вами в ближайшее время')


@bot.message_handler(func=lambda message: True)
def main_message(message):
    users_id_list = [i.user_id for i in User.objects()]
    if message.from_user.id not in users_id_list:
         start(message)
         return
    user = User.objects.get(user_id=message.from_user.id)
    if not user.fio:
        if re.match(r"^[А-ЯІЇЄЁ][а-яіїєё']* [А-ЯІЇЄЁ][а-яіїєё']* [А-ЯІЇЄЁ][а-яіїєё']*$", message.text):
            user.fio = message.text
            user.save()
            bot.send_message(message.chat.id, 'Отлично, я запомнил Ваше ФИО')
            start(message)
        else:
            bot.send_message(message.chat.id, "Не верный формат, введите ФИО в формате Иванов Иван Иванович")
            start(message)

    elif not user.telephone_number:
        client_number = message.text
        client_number = re.sub("\D", "", client_number)
        client_number = re.sub("^380", "0", client_number)
        if re.match(r"^[0]{1}[0-9]{9}$", client_number):
            user.telephone_number = client_number
            user.save()
            bot.send_message(message.chat.id, 'Отлично, я запомнил Ваш номер телефона.')
            start(message)
        else:
            bot.send_message(message.chat.id, 'Формат Вашего номера не верен')
            start(message)

    elif not user.email:
        client_email = message.text
        if re.match(r"[^@]+@[^@]+\.[^@]+", client_email):
            user.email = client_email
            user.save()
            bot.send_message(message.chat.id, 'Отлично, я запомнил Ваш email.')
            start(message)
        else:
            bot.send_message(message.chat.id, 'email не верен')
            start(message)

    elif not user.address:
        user.address = message.text
        user.save()
        bot.send_message(message.chat.id, 'Отлично, я теперь я знаю где ты живешь. Буагага')
        start(message)

    elif not user.wishes:
        user.wishes = message.text
        user.save()
        request = Request(**{"request": user}).save()
        bot.send_message(message.chat.id, 'Спасибо за предоставленную информацию. Информация будет обработана в течение двух часов.')
    else:
        bot.send_message(message.chat.id, 'Я уже имею всю необходимую информацию о Вас. Ожидайте, менеджер связется с Вами в ближайшее время')


@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    users_id_list = [i.user_id for i in User.objects()]
    if message.from_user.id not in users_id_list:
         start(message)
         return
    user = User.objects.get(user_id=message.from_user.id)
    if not user.fio:
        start(message)
        return
    elif user.telephone_number:
        start(message)
        return
    client_number = message.contact.phone_number
    client_number = re.sub("\D", "", client_number)
    client_number = re.sub("^380", "0", client_number)
    if re.match(r"^[0]{1}[0-9]{9}$", client_number):
        user.telephone_number = client_number
        user.save()
        bot.send_message(message.chat.id, 'Отлично, я запомнил Ваш номер телефона.')
        start(message)
    else:
        bot.send_message(message.chat.id, 'Формат Вашего номера не верен')
        start(message)


print("bot started")
bot.polling(none_stop=True)
