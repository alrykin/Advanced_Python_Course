# 1) Создать базу данных студентов (ФИО, группа, оценки, куратор
# студента, факультет). Написать CRUD ко всем полям. Описать
# методы для вывода отличников по каждому факультету. Вывести
# всех студентов определенного куратора.
from mongoengine import *

connect('students_mgdb')

# facultet =  Facultet(**{"facultet_name": "telecommunications"}).save()
# facultet =  Facultet(**{"facultet_name": "informatization"}).save()
# facultet =  Facultet(**{"facultet_name": "electronic"}).save()
# facultet =  Facultet(**{"facultet_name": "biomedical engineering"}).save()
# facultet =  Facultet(**{"facultet_name": "radio-engineering"}).save()


# Curator(**{'curator_name' : 'Иванов Петр Сергеевич'}).save()
# Curator(**{'curator_name' : "Бахмет Олег Григорович"}).save()
# Curator(**{'curator_name' : "Ахметов Агабала Аглы"}).save()
# Curator(**{'curator_name' : "Шкода Вадим Анатолиевич"}).save()
# Curator(**{'curator_name' : "Кузьмин Андрей Викторович"}).save()




curator = Curator.objects.get(curator_name="Воловик Владимир Владимирович")
facultet = Facultet.objects.get(facultet_name="Многоканальная связь")
dict_student = {"name":"Некоз Василий Владимирович",
 "study_group":1,
 "curator": curator,
 "facultet": facultet
 }

Student(**dict_student).save()


# students = Student.objects()
# for i in students:
#     print(i.name)
#     mark_dict = {"subject":"Военная подготовка", "student": i, "mark": (random.randint(2,5))}
#     Marks(**mark_dict).save()
