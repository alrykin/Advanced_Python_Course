from mongoengine import *

connect("store_mgdb")


class Item(Document):
    first_name = StringField(max_length=100)
    price = FloatField()

    def get_count





# xcx = Person.objects().distinct('id')
# print(Person5db9a868cad3393209c323e3' in xcx)
