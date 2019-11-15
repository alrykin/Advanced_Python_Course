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

#TODO LESSON 3
# 1. Визуализация корзины, вывод всех продуктов, общей стоимости корзины.
# 2. Вывод товаров со скидкой, реализовать функциональность
# 3. Таблица История_Заказов, при покупке корзины, отправлять ее
# в эту таблицу.
# 4. Для загрузнки на сервер:
#     4.1 Аккаунт на гугл клауде
#     4.2 Там создать экземпляр виртуальной машины с Ubuntu 18.04 server

from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import telebot
import config
import keyboards
from keyboards import ReplyKB, ReplyIKB
from models import models
from flask import Flask, request, abort

app = Flask(__name__)

STORE_TITLE = "AlcoStore"
bot = telebot.TeleBot(config.TOKEN)

# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


def main_menu(message):
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, u'\U0001F3E0' + "   Главное меню", reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    greeting_str = models.Texts.objects(title='Greetings').get().body
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, greeting_str, reply_markup=keyboard)


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
        keyboard = keyboards.ReplyIKB(key='root', lookup_field='id', named_arg='category')
        bot.send_message(message.chat.id, "Категории" , reply_markup=keyboard.generate_ikb())

    elif message.text.lower() == 'продукты со скидкой':
        product_objects = models.Product.objects(is_discount=True)
        for i in product_objects:
            photo = i.photo.read()
            markup = telebot.types.InlineKeyboardMarkup()
            button = telebot.types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add-to-cart_' + str(i.id))
            markup.add(button)
            bot.send_message(message.chat.id, text=f"<b>{i.title}</b>", parse_mode='HTML')
            bot.send_photo(message.chat.id, photo, parse_mode='HTML', caption=f"Старая цена: " + str(i.price/100) + "\n<b>Новая цена:" + str(i.new_price/100) + "</b>" + f"\n{i.description}", reply_markup=markup)

    elif message.text.lower() == 'корзина':
        if message.from_user.id in models.User.objects.distinct("user_id"):
            user_obj = models.User.objects.get(user_id=message.from_user.id)
            user_cart = models.Cart.objects(user=user_obj, active=True)
            if not user_cart:
                bot.send_message(message.chat.id, "Корзина пуста")
                return
            cart_text = ""
            for i in user_cart:
                cart_text = cart_text + i.product.title + " " + str(i.product.get_price) + " грн.\n"
            cart_summ = models.Cart().get_catr_summ(user_obj)
            cart_text = cart_text + "Общая сумма покупок: " + str(cart_summ) + " грн."
            markup = telebot.types.InlineKeyboardMarkup()
            by_button = telebot.types.InlineKeyboardButton(text='Купить', callback_data='by-cart_' + str(i.user.id))
            clear_button = telebot.types.InlineKeyboardButton(text='Очистить корзину', callback_data='clear-cart_' + str(i.user.id))
            markup.add(by_button, clear_button)
            bot.send_message(message.chat.id, cart_text, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Корзина пуста")
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
        keyboard.generate_ikb()
        keyboard.add(InlineKeyboardButton(text="<<",
                                            callback_data=f'back_{category.id}'))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Сделайте свой выбор",
            reply_markup=keyboard
        )

    else:
        product_objects = category.get_products()
        for i in product_objects:
            photo = i.photo.read()
            markup = telebot.types.InlineKeyboardMarkup()
            button = telebot.types.InlineKeyboardButton(text='Добавить в корзину', callback_data='add-to-cart_' + str(i.id))
            markup.add(button)
            bot.send_message(call.message.chat.id, parse_mode='HTML', text=f"<b>{i.title}</b>")
            if i.is_discount:
                bot.send_photo(call.message.chat.id, photo, parse_mode='HTML', caption=f"Старая цена: " + str(i.price/100) + "\n<b>Новая цена:" + str(i.new_price/100) + "</b>" + f"\n{i.description}", reply_markup=markup)
            else:
                bot.send_photo(call.message.chat.id, photo, parse_mode='HTML', caption=f"<b>Цена: " + str(i.price/100) + "</b>" + f"\n{i.description}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'add-to-cart')
def add_to_cart(call):
    if call.from_user.id not in models.User.objects.distinct("user_id"):
        user_obj = models.User(**{"user_id" : call.from_user.id}).save()
    else:
        user_obj = models.User.objects.get(user_id=call.from_user.id)
    product_obj = models.Product.objects.get(id=call.data.split('_')[1])
    models.Cart(**{"user" : user_obj, "product": product_obj}).save()
    bot.send_message(call.message.chat.id, "Товар " + product_obj.title + " добавлен в корзину")


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'clear-cart')
def clear_cart(call):
    models.Cart.objects(active=True, user=call.data.split('_')[1]).delete()
    bot.send_message(call.message.chat.id, "Корзина очищена")


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'by-cart')
def by_cart(call):
    cart_objects = models.Cart.objects(active=True, user=call.data.split('_')[1])
    for i in cart_objects:
        models.OrderHistory(**{"cart":i}).save()
    cart_objects.update(active=False)
    bot.send_message(call.message.chat.id, "Спасибо за покупку!")


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'back')
def go_back(call):
    obj_id = call.data.split("_")[1]
    category = models.Category.objects(id=obj_id).get()

    if category.is_root:
        keyboard = keyboards.ReplyIKB(key = 'root', lookup_field='id', named_arg='category')
        keyboard.generate_ikb()

    else:
        keyboard = keyboards.ReplyIKB(
            iterable=category.parent.subcategory,
            lookup_field='id',
            named_arg='category'
        )
        keyboard.generate_ikb()
        keyboard.add(InlineKeyboardButton(text="<<",
                                        callback_data=f"back_{category.parent.id}"))

    text="Категории" if not category.parent else category.parent.title
    bot.edit_message_text(chat_id=call.message.chat.id,
                            message_id=call.message.message_id,
                            text=text,
                            reply_markup=keyboard)


if __name__ == "__main__":
    import time
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(config, webhook_url)
    print("bot started")

    # bot.polling(none_stop=True)
