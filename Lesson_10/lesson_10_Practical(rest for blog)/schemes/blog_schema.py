from marshmallow import Schema, fields, validates, ValidationError

class AuthorSchema(Schema):
    id = fields.String()
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)

class TagSchema(Schema):
    id = fields.String()
    name = fields.String(required=True)

class PostSchema(Schema):
    id = fields.String()
    title = fields.String(required=True)
    post = fields.String(required=True)
    view_count = fields.Integer()
    date = fields.DateTime()
    tag = fields.Nested(TagSchema)
    author = fields.Nested(AuthorSchema)


    # @validates('age')
    # def validate_age(self, value):#название может быть любым
    #     if value > 65:
    #         raise ValidationError("The age must be less than 65")
