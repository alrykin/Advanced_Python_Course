from marshmallow import Schema, fields, validates, ValidationError
from models.blog import *

class AuthorSchema(Schema):
    id = fields.String()
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)


class TagSchema(Schema):
    id = fields.String()
    name = fields.String(required=True)

    @validates('name')
    def validate_name(self, value):#название может быть любым
        if len(value) > 15 or len(value) < 2:
            raise ValidationError("The length of tag must be from 2 to 15 symbols")

class PostSchema(Schema):
    id = fields.String()
    title = fields.String(required=True)
    post = fields.String(required=True)
    view_count = fields.Integer()
    date = fields.DateTime()
    tag = fields.Nested(TagSchema)
    author = fields.Nested(AuthorSchema)


    @validates('post')
    def validate_post(self, value):#название может быть любым
        if len(value) < 20:
            raise ValidationError("The length of post must be greater than 20 symbols")


class PostTesttSchema(Schema):
    """ This schema created for ability to save the author and title as string.
    and now we can use ReferenceField in db structure """
    id = fields.String()
    title = fields.String(required=True)
    post = fields.String(required=True)
    view_count = fields.Integer()
    date = fields.DateTime()
    tag = fields.String()
    author = fields.String()

    @validates('author')
    def validate_author(self, value):
        author_ids_list = [str(i.id) for i in Author.objects()]
        if value not in author_ids_list:
            raise ValidationError(f"There is no such author with id {value}")

    @validates('tag')
    def validate_tag(self, value):
        tag_ids_list = [str(i.id) for i in Tag.objects()]
        if value not in tag_ids_list:
            raise ValidationError(f"There is no such tag with id {value}")
