## 2) Создать модуль, который будет заполнять базу данных
## случайными валидными значениями (минимум 100 студентов)

from mongoengine import *
from models.students import *

import random

def names_generator(number):
    """Функция для генерации имени и отчества. Передайте параметр number. Функция вернет список  с этим количеством случайных имен"""
    first_names = {"Александр", "Сергей", "Петр", "Алексей", "Дмитрий", "Валентин", "Леонид", "Игорь", "Юрий", "Иван", "Андрей", "Богдан", "Борис", "Виктор", "Генадий", "Олег", "Виталий", "Николай", 'Эдуард', "Вано", "Грегор", "Юлий", "Карл", "Люк", "Антон", "Владислав", "Вячеслав"}
    last_names = {"Иванов", "Петров", "Сидоров", "Мельник", "Шевченко", "Котляревский", "Гоголь", "Ершов", "Егоров", "Пилипенко", "Бобень", "Жуков", "Петрович", "Кокорин","Гармаш","Сидорчук", "Волков", "Старк", "Таргариен", "Подолян","Штирлиц","Колобков"}

    names_list=[]
    i=number
    while len(names_list) < number:
        first = random.sample(first_names, 1)[0]
        last = random.sample(last_names - {first}, 1)[0]
        name = last + " " + first
        if name not in names_list:
             names_list.append(name)
             # print(name)
        i-=1
    return names_list


def facultets_generator():
    """функция для создания факультетов"""
    facultet =  Facultet(**{"facultet_name": "telecommunications"}).save()
    facultet =  Facultet(**{"facultet_name": "informatization"}).save()
    facultet =  Facultet(**{"facultet_name": "electronic"}).save()
    facultet =  Facultet(**{"facultet_name": "biomedical engineering"}).save()
    facultet =  Facultet(**{"facultet_name": "radio-engineering"}).save()

def curators_generator():
    """функция для создания кураторов"""
    Curator(**{'curator_name' : 'Мельник Петр Сергеевич'}).save()
    Curator(**{'curator_name' : "Котляревский Олег Григорович"}).save()
    Curator(**{'curator_name' : "Шевченко Тарас Григорович"}).save()
    Curator(**{'curator_name' : "Гоголь Вадим Анатолиевич"}).save()


# Создаем студентов !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def student_creator(names_list):
    """Функция для создания студентов"""

    curators_set = set()
    curators = Curator.objects()
    for curator in curators:
        curators_set.add(curator)

    facultets_set = set()
    facultets = Facultet.objects()
    for facultet in facultets:
        facultets_set.add(facultet)

    for name in names_list:
        dict_student = {"name": name,
         "study_group": (random.randint(1,4)),
         "curator": (random.sample(curators_set,1)[0]),
         "facultet": (random.sample(facultets_set,1)[0])
         }

        Student(**dict_student).save()


def some_marks_generator():
    subjects_set = { "Высшая математика", "Физика", "Теория електрическиx цепей", "Военная подготовка"}
    students = Student.objects()
    for subj in subjects_set:
        for i in students:
            mark_dict = {"subject": subj, "student": i, "mark": (random.randint(3,5))}
            Marks(**mark_dict).save()

def otlichnic_create():
    student_first = Student.objects().first()
    his_marks = student_first.marks
    print(student_first.name + " set all marks to 5")
    for i in his_marks:
        i.mark = 5
        i.save()

print("Сгенерировать данные ?")
answer = input("Введите Yes для генерации: ")
if answer == "Yes":
    number_to_generate = input("Введите требуемое количество студентов: ")
    if not number_to_generate:
        number_to_generate = 5
    else:
        print("Вы не определили количество студентов. Использую дефолтное значение 5")
        number_to_generate = int(number_to_generate)
    print("Начинаю геренировать данные")
    facultets_generator()
    curators_generator()
    names_list = names_generator(number_to_generate)
    student_creator(names_list)
    some_marks_generator()
    otlichnic_create()
    print("Готово")
else:
    print("Выхожи из программы без каких либо действий.")
