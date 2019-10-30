from mongoengine import *

connect("store_mgdb")

class SubCategory(EmbeddedDocument):
    name = StringField(max_length=100)
    description = StringField(max_length=255)

class ItemCategory(EmbeddedDocument):
    CATEGORY_CHOICES = (
            ('strong alcohol', 'strong alcohol'),
            ('low alcohol', 'low alcohol'),
            ('semi alcohol', 'semi alcohol')
    )
    name = StringField(choices=CATEGORY_CHOICES)
    subcategory = EmbeddedDocumentField(SubCategory)

class Item(Document):
    name = StringField(max_length=100)
    intems_count = IntField(default=0)
    category = EmbeddedDocumentField(ItemCategory)
    price = FloatField(default=0)
    view_count = IntField(default=0)

    def get_count(self):
        pass





# xcx = Person.objects().distinct('id')
# print(Person5db9a868cad3393209c323e3' in xcx)
