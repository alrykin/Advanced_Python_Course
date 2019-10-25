from mongoengine import *
import datetime

# подключаемся
connect('test_db')

class User(Document):
    first_name = StringField(max_length=128)
    surname = StringField(max_length=128)
    email = EmailField()
    dirth_of_year = IntField()

    @property
    def posts(self):
        return Post.objects(user=self)

    @classmethod
    def create(cls, **kwargs):
        if kwargs.get("dirth_of_year") < 2005:
            return ValidationError()
        cls(**kwargs).save()

    def create_post(self, **kwargs):
        kwargs.update(user=self)
        Post(**kwargs).save()


class Post(Document):
    title = StringField(max_length=128)
    body = StringField(max_length=4096)
    added_at = DateTimeField(default=datetime.datetime.now())
    user = ReferenceField(User)
#
# dict_user = {
#     "first_name":"",
#     "surname":"Andry",
#     "email" : "Andry@aAndry.com",
#     "dirth_of_year": 1987
# }
#
# user =  User(**dict_user).save()
#
# dict_post = {"title":"new_post",
#  "body":"text",
#  "user": user
#  }
#
# Post(**dict_post).save()
#
# #User.objects - возвращает квери сет
# user = User.objects(first_name="Sasha").first()
# print(user.posts)

user = User.objects(first_name="John").first()
# примеры выборок
user = User.objects(dirth_of_year__gt=1000).first()
user = User.objects(first_name__in=['John', 'Andry']).first()
print(user.posts)


print(user.to_json())# превратит в json, можно и к кверисету, вернет список

for p in user.posts:
    print(p.title)
    print(p.body)
    print(p.id)
    print(p.added_at)

# #Пример увеличения значений итерируя
# users = User.objects(first_name__in=['John', 'Andry'])
# for u in users:
#     u.dirth_of_year +=1000
#     u.save()

# Пример апдейта применяя к кверисету
users = User.objects(first_name__in=['John', 'Andry']).update(dirth_of_year=1980)

user  = User.objects.first()
user.create_post(**{"title": "new", "body":"new"})
user.create_post(**{"title": "newest", "body":"newest"})
