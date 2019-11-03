# ) Написать бота-консультанта, который будет собирать информацию с
# пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
# Записывать сформированную заявку в БД (по желанию SQl/NOSQL).).

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

import config
from models.botmodels import *
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
        bot.send_message(message.chat.id, "Введите ФИО: ")
    elif not user.telephone_number:
        keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
        reg_button = KeyboardButton(text="Поделиться своим номером телефона", request_contact=True)
        keyboard.add(reg_button)
        bot.send_message(message.chat.id,"У меня отсутствуют данные о Вашем номере телефона, поделитесь ?", reply_markup=keyboard)
        # bot.send_message(message.chat.id, "Введите мобильный : ")
    # bot.send_message(message.chat.id, user.user_id)


# @bot.message_handler(func=lambda message: True)
# def scstart(message):
#     start(message)
@bot.message_handler(func=lambda message: True)
def main_message(message):
    users_id_list = [i.user_id for i in User.objects()]
    if message.from_user.id not in users_id_list:
         start(message)
    # user = User.objects.get(user_id=message.from_user.id)
    start(message)


@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    client_number = message.contact.phone_number
    client_number = re.sub("\D", "", client_number)
    client_number = re.sub("^380", "0", client_number)
    if re.match(r"^[0]{1}[0-9]{9}$", client_number):
        id_number[message.from_user.id] = client_number
        user.telephone_number = client_number
        user.save()
        bot.send_message(message.chat.id, 'Отлично, я запомнил Ваш номер телефона.')
        start(message)
    else:
        bot.send_message(message.chat.id, 'Формат Вашего номера не верен')
        start(message)




print("bot started")
bot.polling(none_stop=True)
