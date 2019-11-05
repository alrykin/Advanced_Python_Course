beginning_kb = {
    "news": "Последние новости",
    "products": "Продукты",
    "sales": "Продукты со скидкой",
    "about": "Информация о магазине"
}

from telebot.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)

class ReplyKB(ReplyKeyboardMarkup):
    def __init__(self, one_time_keyboard=True, resize_keyboard=True, row_width=3):
        super().__init__(one_time_keyboard=one_time_keyboard,
                        resize_keyboard=resize_keyboard,
                        row_width=row_width)

    def generate_kb(self, *args):
        """
        Buttons names
        """
        buttons = [KeyboardButton(x) for x in args]
        self.add(*buttons)
        return self
