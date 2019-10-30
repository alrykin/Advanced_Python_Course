from marshmallow import Schema, fields, validates, ValidationError


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
