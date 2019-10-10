# Создайте класс ПЕРСОНА с абстрактными методами, позволяющими
# вывести на экран информацию о персоне, а также определить ее возраст (в
# текущем году). Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата
# рождения, факультет), СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# со своими методами вывода информации на экран и определения возраста.
# Создайте список из n персон, выведите полную информацию из базы на
# экран, а также организуйте поиск персон, чей возраст попадает в заданный
# диапазон.

from abc import ABC, abstractmethod
import datetime

class Persona(ABC):

    PERSON_DB = []

    @classmethod
    def get_db(cls, *args, **kwargs):
        return cls.PERSON_DB

    @classmethod
    def get_db_detail(cls, *args, **kwargs):
        for i in cls.PERSON_DB:
            print(i.get_persona_info())
        #return cls.PERSON_DB

    @classmethod
    def get_list_persons(cls, **kwargs):
         n_person = []
         for i in cls.PERSON_DB:
             n_person.append(i._name)
         return n_person

    @classmethod
    def age_search(cls, var1, var2):
        list_of_persons = []
        for i in cls.PERSON_DB:
            if i.how_old() >= var1 and i.how_old() <= var2:
                 print(i._name)
                 list_of_persons.append(i)
        if list_of_persons: return list_of_persons

        #return cls.PERSON_DB

    @abstractmethod
    def get_persona_info(self):
        return "persona info"

    @abstractmethod
    def how_old(self):
        return "how old persons is"

    def __str__(self):
        return self._name



class Abiturient(Persona):

    def __init__(self, name, date_of_birth, facultet):
        self._name = name
        self._date_of_birth = date_of_birth
        self._facultet = facultet
        #super().PERSON_DB.append(dict(name = name))
        super().PERSON_DB.append(self)

    def how_old(self):
        year_of_birth = self._date_of_birth.split("-")[0]
        return (datetime.datetime.now().year) - int(year_of_birth)

    def get_persona_info(self):
        age = str(self.how_old())
        return "\nName: " + self._name + "\nFacultet: " + self._facultet + "\nAge: " + age + "\n"


class Student(Abiturient):
    def __init__(self, name, date_of_birth, facultet, course):
        self._name = name
        self._date_of_birth = date_of_birth
        self._facultet = facultet
        self._course = course
        super().PERSON_DB.append(self)

    def get_persona_info(self):
        age = str(self.how_old())
        return "\nName: " + self._name + "\nFacultet: " + self._facultet + "\nAge: " + age + "\nCourse: " + self._course + "\n"



class Teacher(Abiturient):
    def __init__(self, name, date_of_birth, facultet, position, experience):
        self._name = name
        self._date_of_birth = date_of_birth
        self._facultet = facultet
        self._position = position
        self._experience = experience
        super().PERSON_DB.append(self)

    def get_persona_info(self):
        age = str(self.how_old())
        return "\nName: " + self._name + "\nFacultet: " + self._facultet + "\nAge: " + age + "\nExperience: " + self._experience + "\n"



sasha = Abiturient("Aleksandr Yaremenko","1987-09-28","Data Science")
print(sasha.how_old())
print(sasha.get_persona_info())


vasya = Student("Vasiliy Pupkin","1985-09-28","Filology", "4")
print(vasya.how_old())
print(vasya.get_persona_info())

ivan_petrovich = Teacher("Ivan Petrovich","1970-10-10","Dana Science", "Decan", "20")
print(ivan_petrovich.how_old())
print(ivan_petrovich.get_persona_info())


# список имен
print(Persona.get_list_persons())

# Вывод "БД" в "сыром" виде ибо база в виде списка объектов
print(Persona.get_db())

# Вывод инфо из "БД"
Persona.get_db_detail()

# печатаю имя возвращаю список обьектов персон, возраст которой входит в диапазон от и до
list_of_age_diapazon_persons = Persona.age_search(10,90)
