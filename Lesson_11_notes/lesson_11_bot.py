import telebot
import config
from telebot.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Дароф")
    keyboard = ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
    list_of_buttons = [KeyboardButton(f"Button {k}") for k in range(6)]
    keyboard.add(*list_of_buttons)
    bot.send_message(message.chat.id, "The text",
        reply_markup=keyboard
    )



@bot.message_handler(func=lambda message: message.text == "Hi")
def echo(message):
    bot.send_message(message.chat.id, "Hi to you to")



@bot.message_handler(commands=["inline"])
def inlint(message):
    keyboard = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton(f"inline-button-{k}",
                                    callback_data=str(k)) for k in range(12)]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, "Inline mode example" , reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_example(call):
    bot.send_message(call.message.chat.id,
            f"I'am a message from inline mode the data is {call.data}")


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)




bot.polling(none_stop=True)
