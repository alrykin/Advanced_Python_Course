#TODO 4
# 1. Реализовать REST для, категорий, продуктов и текстов
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from marshmallow import Schema, fields, validates, ValidationError
from models.store import *



class PropertiesSchema(Schema):
    # id = fields.String()
    weight = fields.Float()

class CategorySchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    subcategory = fields.List(fields.Nested('CategorySchema', only=('id', )))
    parent = fields.String()

    @validates('parent')
    def validate_parent(self, value):
        сategory_ids_list = [str(i.id) for i in Category.objects()]
        if value not in сategory_ids_list:
            raise ValidationError(f"There is no such сategory with id {value}")

    @validates('subcategory')
    def validate_subcategory(self, value):
        if value:
            raise ValidationError(f"You cant add subcategory manual! It append's automatically then you create subcategory with this category as parent")



class ProductSchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    price = fields.Integer()
    new_price = fields.Integer()
    is_discount = fields.Boolean()
    properties = fields.Nested(PropertiesSchema)
    category = fields.String()
    #category = fields.Nested(CategorySchema)
    #photo =  fields.Field()

    @validates('category')
    def validate_category(self, value):
        сategory_ids_list = [str(i.id) for i in Category.objects()]
        if value not in сategory_ids_list:
            raise ValidationError(f"There is no such сategory with id {value}")



class TextsSchema(Schema):
    id = fields.String()
    title = fields.String()
    body = fields.String()
