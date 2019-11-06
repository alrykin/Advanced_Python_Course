# #TODO LESSON 1
# 1) Написать seeder, который заполнит бд тестоыыми данными
# 2) Добавить функциональносить к кнопкам
# 3) (При клике на продукты). Реализовать вывод категорий (инлайн).
# (Необязательно сделать вывод подкатегорий с удаленимем предыдущего сообщения))
# sales кнопку - не трогаем.

import telebot
import config
import keyboards
from keyboards import ReplyKB, ReplyIKB
from models import models

from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

STORE_TITLE = "eStore"
bot = telebot.TeleBot(config.TOKEN)


def main_menu(message):
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, "Главное меню", reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    greeting_str = models.Texts.objects(title='Greetings').get().body
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, greeting_str, reply_markup=keyboard)

# @bot.message_handler(func=lambda message: True)
@bot.message_handler(content_types=['text'])
def main_text_handler(message):
    if message.text.lower() == 'информация о магазине':
        about_str = models.Texts.objects(title='About').get().body
        bot.send_message(message.chat.id, about_str)
        main_menu(message)
        return
    elif message.text.lower() == 'последние новости':
        about_str = models.Texts.objects(title='Last news').get().body
        bot.send_message(message.chat.id, about_str)
        main_menu(message)
        return
    elif message.text.lower() == 'продукты':
        categories = models.Category().ger_root_categories()
        keyboard = ReplyIKB().generate_ikb(*categories)
        bot.send_message(message.chat.id, "Выберите интересующую Вас категорию: " , reply_markup=keyboard)

    else:
        pass


@bot.callback_query_handler(func=lambda call: True)
def callback_example(call):
    bot.send_message(call.message.chat.id,
            f"I'am a message from inline mode the data is {call.data}")


if __name__ == "__main__":
    print("bot started")
    bot.polling(none_stop=True)
