from marshmallow import Schema, fields, validates, ValidationError

ProductSchema, TextsSchema

class ProductSchema(Schema):
    pass


class CategorySchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    subcategory = fields.List()
    parent = fields.Nested(CategorySchema)


class ProductSchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    price = fields.Integer()
    new_price = fields.Integer()
    is_discount = field.Boolean()
    properties = fields.Nested(PropertiesSchema)
    category = fields.Nested(CategorySchema)

    photo = FileField()




class SubCategorySchema(Schema):
    name = fields.String()
    description = fields.String()

class ItemCategorySchema(Schema):
    name = fields.String(required=True)
    subcategory = fields.Nested(SubCategorySchema)

    #
    # @validates('age')
    # def validate_age(self, value):#название может быть любым
    #     if value > 65:
    #         raise ValidationError("The age must be less than 65")

class ItemSchema(Schema):
    id = fields.String()
    name = fields.String(required=True)
    intems_count = fields.Integer()
    category = fields.Nested(ItemCategorySchema)
    price = fields.Float()
    view_count = fields.Integer()
