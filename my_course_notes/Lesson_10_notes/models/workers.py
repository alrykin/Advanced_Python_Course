from mongoengine import *

connect("workers_mgdb")


class Location(EmbeddedDocument):
    CITY_CHOICES = (
        ('Kyiv', 'Kyiv'),
        ('Kharkiv', 'Kharkiv'),
        ('Lviv', 'Lviv')
    )
    city = StringField(choices=CITY_CHOICES)
    street = StringField(max_length=255)


class Person(Document):
    first_name = StringField(max_length=64)
    surname = StringField(max_length=64)
    age = IntField()
    experience = IntField()
    location = EmbeddedDocumentField(Location)
