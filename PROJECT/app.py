import telebot
import config
import keyboards
from keyboards import ReplyKB
from models import models

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #greeting_str = models.Texts(title='Greetings').get().body
    greeting_str = "Hi"
    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, greeting_str, reply_markup=keyboard)

if __name__ == "__main__":
    bot.polling(none_stop=True)
