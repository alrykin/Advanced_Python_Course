from mongoengine import *

connect("web_shop_bot")


class Texts(Document):
    title = StringField(unique=True)
    body = StringField(max_length=4096)


class Properties(DynamicEmbeddedDocument):
    weight = FloatField(min_value=0)


class Category(Document):
    title = StringField(max_length=255, required=True)
    description = StringField(max_length=512)
    subcategory = ListField(ReferenceField('self'))
    is_root = BooleanField(default=False)

    @property
    def is_parent(self):
        return bool(self.subcategory)

    @property
    def get_products(self, **kwargs):
        return Product.objects(category=self, **kwargs)#  **{"sadf": "sdf"}

    def add_subcategory(self, obj):
        self.subcategory.append(obj)

    def get_subcategories(self, parent_title):
        sub_cats_title_list = []
        sub_cats_obj = Category.objects.get(title=parent_title).subcategory
        for i in sub_cats_obj:
            sub_cats_title_list.append(i.title)
        return sub_cats_title_list


    @classmethod
    def get_root_categories(cls):
        return cls.objects(is_root=True)
        # return root_categories

class Product(Document):
    title = StringField(max_length=255)
    description = StringField(max_length=1024)
    price = IntField(min_value=0)#будем хранить в копейках воизбежание  будующих проблем на стыках с fe и т.п.
    new_price = IntField(min_value=0)
    is_discount = BooleanField(default=False)
    properties = EmbeddedDocumentField(Properties)
    category = ReferenceField(Category)

    @property
    def get_price(self):
        if self.is_discount:
            return str(self.new_price / 100)
        return str(self.price / 100)

    @classmethod
    def get_discount_products(cls):
        return cls.objects(is_discount=True, **kwargs)
