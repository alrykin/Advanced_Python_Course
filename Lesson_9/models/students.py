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


# students = Student.objects()
# for i in students:
#     print(i.name)
#     mark_dict = {"subject":"Военная подготовка", "student": i, "mark": (random.randint(2,5))}
#     Marks(**mark_dict).save()

#
# x = Marks.objects().aggregate(
#   {"$group": { "_id": "$subject", "student": { "$push": "$student"}}}
#         )
# for i in x:
#     print("Предмет: " + i['_id'] + ":")
#     print(i['student'])
#     for s in i['student']:
#         xxx = Student.objects.get(id=s).by_subject_marks(i['_id'])
#         name = Student.objects.get(id=s).name
#         print(name, xxx[0].mark)

# x = Marks.objects().aggregate(
#   {"$group": { "_id": "$subject", "student": { "$push": "$student"}}}
#         )
# for i in x:
#     subject = i['_id']
#     subject_students_ids = i['student']
#     print(subject_students_ids)


# dict_to_template = {}
# marks_subjects = Marks.objects().distinct('subject')
# for subject in marks_subjects:
#     dict_to_template[subject] = {}
#     # print(subject)
#     ## studetns_with_marks_of_this_subjects
#     students = Marks.objects(subject=subject).distinct('student')
#     for student in students:
#         # print(student.name)
#         dict_to_template[subject][student.id] = {}
#         dict_to_template[subject][student.id]['name'] = student.name
#         dict_to_template[subject][student.id]['marks'] = {}
#         student_marks = student.by_subject_marks(subject)
#         for mark in student_marks:
#             # print(mark.mark)
#             dict_to_template[subject][student.id]['marks'][mark.id] = mark.mark
#
# print(dict_to_template)
# for i in dict_to_template:
#     print(i)
#     for s in dict_to_template[i]:
#         print(dict_to_template[i][s]['name'])
#         print(dict_to_template[i][s]['marks'])


# studentt = Student.objects.get(name='тест')
# print(studentt.name)
#
# studentt.delete_with_dependencys
# studentt = Student.objects.get(name='тест')
# print(studentt.name)
