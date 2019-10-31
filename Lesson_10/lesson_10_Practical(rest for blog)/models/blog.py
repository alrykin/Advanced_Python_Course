from mongoengine import *
import datetime

connect("blog_mgdb")


class Author(Document):
    first_name = StringField(max_length=100)
    last_name = StringField(max_length=100)
    # post_count = IntField(default=0)
    # post_count = Post.objects(author=self).count()
    def get_post_count(self):
        return Post.objects(author=self).count()

class Tag(Document):
    name = StringField(max_length=20)


class Post(Document):
    title = StringField(max_length=64)
    post = StringField(max_length=255)
    view_count = IntField(default=0)
    author = ReferenceField(Author, reverse_delete_rule=1)
    date = DateTimeField(default=datetime.datetime.now())
    tag = ReferenceField(Tag, reverse_delete_rule=1)
