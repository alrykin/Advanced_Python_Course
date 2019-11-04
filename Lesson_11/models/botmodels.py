# ) Написать бота-консультанта, который будет собирать информацию с
# пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
# Записывать сформированную заявку в БД (по желанию SQl/NOSQL).).

from mongoengine import *
import datetime

connect("bot_consultand_mgdb")


class User(Document):
    # reg_stage = IntField(default=0)
    user_id = IntField()
    fio = StringField(max_length=100)
    telephone_number = StringField(max_length=12)
    email = EmailField()
    address = StringField(max_length=100)
    wishes = StringField(max_length=255)

    def get_reg(self):
        return User.objects(author=self).count()


class Request(Document):
    request = ReferenceField(User, reverse_delete_rule=1)
