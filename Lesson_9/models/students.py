# 1) Создать базу данных студентов (ФИО, группа, оценки, куратор
# студента, факультет). Написать CRUD ко всем полям. Описать
# методы для вывода отличников по каждому факультету. Вывести
# всех студентов определенного куратора.
from mongoengine import *
import random

connect('students_mgdb')

class Curator(Document):
    curator_name = StringField(max_length=128)

    def get_curator_students(self):
        """get all curators students"""
        return Student.objects(curator = self)

class Facultet(Document):
    facultet_name = StringField(max_length=128)

    # def get_fac_A_students():
    #     return Student.objects(facultet=self, marks.mark=)

class Student(Document):
    name = StringField(max_length=128)
    study_group = IntField()
    curator = ReferenceField(Curator)
    facultet = ReferenceField(Facultet)

    @property
    def marks(self):
        return Marks.objects(student=self)

    def add_mark(self, **kwargs):
        kwargs.update(student=self)
        Marks(**kwargs).save()

    # @property
    # def get_A_students(self):
    #     return Marks.objects(student=self)

    # @property
    # def curator(self):
    #     return Curators.objects(student=self)
    #
    # def add_curator(self, **kwargs):
    #     kwargs.update(student=self)
    #     Curators(**kwargs).save()
    #
    # @property
    # def facultet(self):
    #     return Facultets.objects(student=self)
    #
    # def add_facultet(self, **kwargs):
    #     kwargs.update(user=self)
    #     Curators(**kwargs).save()

class Marks(Document):
    subject = StringField(max_length=128)
    student = ReferenceField(Student)
    mark = IntField()


curator = Curator.objects.get(curator_name="Кись Олег Олегович")
print(curator.get_curator_students)
# student = Student.objects.get(name="Кукла Юрий Владимирович")
