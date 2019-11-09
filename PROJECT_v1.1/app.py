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

STORE_TITLE = "AlcoStore"
bot = telebot.TeleBot(config.TOKEN)


def main_menu(message):
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, u'\U0001F3E0' + "   Главное меню", reply_markup=keyboard)


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
        category_queryset = models.Category.get_root_categories()
        keyboard = keyboards.ReplyIKB(
            iterable=category_queryset,
            lookup_field='id',
            named_arg='category'
        )
        bot.send_message(message.chat.id, "Выберите интересующую Вас категорию: " , reply_markup=keyboard.generate_ikb())
    else:
        pass


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def show_products_or_subcategory(call):
    obj_id = call.data.split("_")[1]
    category = models.Category.objects(id=obj_id).get()
    if category.is_parent:
        keyboard = keyboards.ReplyIKB(
            iterable=category.subcategory,
            lookup_field='id',
            named_arg='category'
        )
        #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Сделайте свой выбор', reply_markup=keyboard)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Сделайте свой выбор",
            reply_markup=keyboard.generate_ikb()
        )
    else:
        print(call.data)



# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     # Если сообщение из чата с ботом
#     if call.message:
#         endpoint_categories = models.Category.objects(subcategory=[]).distinct("title")
#         if call.data not in endpoint_categories:
#             sub_categories = models.Category().get_subcategories(call.data)
#             keyboard = ReplyIKB().generate_ikb(*sub_categories)
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Сделайте свой выбор', reply_markup=keyboard)
#         else:
#             print(call.data)# здесь в дальнейшем реализовать выовод самих товаров
#     else:
#         pass



if __name__ == "__main__":
    print("bot started")
    bot.polling(none_stop=True)
