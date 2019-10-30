from mongoengine import *

connect("blog_mgdb")


class Author(Document):
    first_name = StringField(max_length=100)
    last_name = StringField(max_length=100)


class Post(Document):
    title = StringField(max_length=64)
    post = StringField(max_length=255)
    author = ReferenceField(Author, reverse_delete_rule=1)
    tag = StringField(max_length=20)



# xcx = Person.objects().distinct('id')
# print(Person5db9a868cad3393209c323e3' in xcx)
