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
        return Student.objects(curator=self)


class Facultet(Document):
    facultet_name = StringField(max_length=128)

    def get_fac_a_students(self):
        return Student.get_a_students(self)

class Student(Document):
    name = StringField(max_length=128)
    study_group = IntField()
    curator = ReferenceField(Curator, reverse_delete_rule=1)
    facultet = ReferenceField(Facultet, reverse_delete_rule=1)

    @property
    def marks(self):
        return Marks.objects(student=self)

    def by_subject_marks(self, subject):
        return Marks.objects(student=self, subject=subject)

    def add_mark(self, **kwargs):
        kwargs.update(student=self)
        Marks(**kwargs).save()

    @classmethod
    def get_a_students(cls, facultet):
        """ Метод получения отличников по факультету """
        students_of_fac = cls.objects(facultet=facultet)
        a_students = []
        for i in students_of_fac:
            st_obj = i
            st_markavg = Marks.objects(student=i).average('mark')
            if st_markavg > 4.9:
                a_students.append(i)
        return a_students

class Marks(Document):
    subject = StringField(max_length=128)
    student = ReferenceField(Student, reverse_delete_rule=2)
    mark = IntField()
