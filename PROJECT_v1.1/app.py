# #TODO LESSON 1
# 1) Написать seeder, который заполнит бд тестоыыми данными
# 2) Добавить функциональносить к кнопкам
# 3) (При клике на продукты). Реализовать вывод категорий (инлайн).
# (Необязательно сделать вывод подкатегорий с удаленимем предыдущего сообщения))
# sales кнопку - не трогаем.

# #TODO LESSON 2
# 1. Реализовать вывод продуктов.
# 1.1 Выводить товары с картинкой.
# 2. Реализация корзины. -> Создать таблицу юзера -> Связать юзера и список товаров

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
        #print(call.data)
        product_objects = category.get_products()
        for i in product_objects:
            photo = i.photo.read()
            markup = telebot.types.InlineKeyboardMarkup()
            button = telebot.types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add-to-cart_' + str(i.id))
            markup.add(button)
            bot.send_message(call.message.chat.id, parse_mode='HTML', text=f"<b>{i.title}</b>")
            bot.send_photo(call.message.chat.id, photo, parse_mode='HTML', caption=f"<b>Цена: " + str(i.price/100) + "</b>" + f" {i.description}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'add-to-cart')
def add_to_cart(call):
    # user_last_name = call.from_user.last_name
    # user_first_name = call.from_user.first_name
    if call.from_user.id not in models.User.objects.distinct("user_id"):
        user_obj = models.User(**{"user_id" : call.from_user.id}).save()
    else:
        user_obj = models.User.objects.get(user_id=call.from_user.id)
    product_obj = models.Product.objects.get(id=call.data.split('_')[1])
    models.Cart(**{"user" : user_obj, "product": product_obj}).save()
    print(str("Пользователь: " + str(call.from_user.id) + " добавил в корзину товар: "  + call.data.split('_')[1]))


if __name__ == "__main__":
    print("bot started")
    bot.polling(none_stop=True)
