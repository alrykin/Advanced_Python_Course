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
    PERSON_DB = {}# list of objects ?))))

    @classmethod
    def insert_to_db(cls, **kwargs):
        cls.PERSON_DB

    @abstractmethod
    def get_persona_info(self):
        return "persona info"

    @abstractmethod
    def how_old(self):
        return "how old persons is"





class Abiturient(Persona):

    def __init__(self, name, date_of_birth, facultet):
        self._name = name
        self._date_of_birth = date_of_birth
        self._facultet = facultet

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

    def get_persona_info(self):
        age = str(self.how_old())
        return "\nName: " + self._name + "\nFacultet: " + self._facultet + "\nAge: " + age + "\nExperience: " + self._experience + "\n"

sasha = Abiturient("Sasha","1987-09-28","Data Science")
print(sasha.how_old())
print(sasha.get_persona_info())


vasya = Student("Vasya","1985-09-28","Filology", "4")
print(vasya.get_persona_info())

ivan_petrovich = Teacher("Ivan Petrovich","1970-10-10","Dana Science", "Decan", "20")
print(ivan_petrovich.how_old())
print(ivan_petrovich.get_persona_info())
