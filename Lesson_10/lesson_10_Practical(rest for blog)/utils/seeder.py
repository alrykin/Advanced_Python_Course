# from my_course_notes.Lesson_10_notes.models.workers import Person, Location
# print(sys.path)
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.blog import Author, Post, Tag


author_obj = Author(first_name="Aleksandr", last_name="Yaremenko").save()
tag_obj = Tag(name="OOP").save()
post_text = """
(ООП) — методология программирования, основанная на представлении
программы в виде совокупности объектов, каждый из которых является экземпляром
определённого класса, а классы образуют иерархию наследования.
"""
post_dict = {
    "title" : "Основы ООП",
     "post" : post_text,
     "view_count": 0,
     "author" : author_obj,
     "tag" : tag_obj,
}
Post(**post_dict).save()

post_text = """
Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).
Инкапсуляция делает некоторые из компонент доступными только внутри класса.
"""
post_dict = {
    "title" : "Инкапсуляция",
     "post" : post_text,
     "view_count": 0,
     "author" : author_obj,
     "tag" : tag_obj,
}
Post(**post_dict).save()


author_obj = Author(first_name="Miguel", last_name="Grinberg").save()
tag_obj = Tag(name="Flask").save()
post_text = """
Welcome!
You are about to start on a journey to learn how to create web applications with Python and the Flask framework.
By the end of this chapter you are going to have a simple Flask web application running on your computer!
"""
post_dict = {
    "title" : "The Flask Mega-Tutorial Part I: Hello, World!",
     "post" : post_text,
     "view_count": 0,
     "author" : author_obj,
     "tag" : tag_obj,
}
Post(**post_dict).save()
