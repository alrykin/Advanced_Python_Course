# 1) Создать базу данных студентов (ФИО, группа, оценки, куратор
# студента, факультет). Написать CRUD ко всем полям. Описать
# методы для вывода отличников по каждому факультету. Вывести
# всех студентов определенного куратора.

from flask import  Flask, render_template, request, redirect, url_for
from models.students import *

app = Flask(__name__)
site_title = "CRUD"

@app.route("/")
def home():
    # return "Hello"
    students = Student.objects.all()
    return render_template("index.html", site_title=site_title, students=students)

@app.route("/add_student", methods = ['GET','POST'])
def add_student():
    if request.method == 'POST':
        student_name = request.form.get('student_name')
        student_group_number = request.form.get('student_group_number')
        student_curator = request.form.get('student_curator')
        student_facultet = request.form.get('student_facultet')
        dict_student = {"name": student_name,
         "study_group": student_group_number,
         "curator": student_curator,
         "facultet": student_facultet
         }
        Student(**dict_student).save()
        return redirect(url_for('home'))
    else:
        facultets = Facultet.objects.all()
        curators = Curator.objects.all()
        return render_template("add_student.html", site_title=site_title, curators=curators, facultets=facultets)

@app.route("/delete_student", methods = ['POST'])
def delete_student():
    student_obj_id = request.form.get('user_delete_form')
    student_obj = Student.objects.get(id=student_obj_id)
    student_obj.delete()
    return redirect(url_for('home'))

@app.route("/edit_student/<student_id>", methods = ['GET','POST'])
def edit_student(student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'GET':
        facultets = Facultet.objects.all()
        curators = Curator.objects.all()
        return render_template("edit_student.html", site_title=site_title, student=student, facultets=facultets, curators=curators)
    elif request.method == 'POST':
        student.name = request.form.get('student_name')
        student.study_group = request.form.get('student_group_number')
        print(Curator.objects.get(id=request.form.get('student_curator')))
        student.curator = Curator.objects.get(id=request.form.get('student_curator'))
        student.facultet = Facultet.objects.get(id=request.form.get('student_facultet'))
        student.save()
        return redirect(url_for('home'))
    else:
        return "else"


@app.route("/facultets")
def facultets_page():
    facultets = Facultet.objects.all()
    return render_template("facultets.html", site_title=site_title, facultets=facultets)

@app.route("/add_facultet", methods = ['GET','POST'])
def add_facultet():
    if request.method == 'GET':
        return render_template("add_facultet.html", site_title=site_title)
    elif request.method == 'POST':
        facultet_name = request.form.get('facultet_name')
        Facultet(**{'facultet_name' : facultet_name}).save()
        return redirect(url_for('facultets_page'))
    else:
        pass

@app.route("/edit_facultet/<facultet_id>", methods = ['GET','POST'])
def edit_facultet(facultet_id):
    facultet = Facultet.objects.get(id=facultet_id)
    if request.method == 'GET':
        return render_template("edit_facultet.html", site_title=site_title, facultet=facultet)
    else:
        facultet.facultet_name = request.form.get('facultet_name')
        facultet.save()
        return redirect(url_for('facultets_page'))

@app.route("/delete_facultet", methods = ['POST'])
def delete_facultet():
    facultet_obj_id = request.form.get('facultet_delete_form')
    facultet_obj = Facultet.objects.get(id=facultet_obj_id)
    facultet_obj.delete()
    return redirect(url_for('facultets_page'))

@app.route("/marks")
def makrs_page():
    dict_to_template = {}
    marks_subjects = Marks.objects().distinct('subject')
    for subject in marks_subjects:
        dict_to_template[subject] = {}

        students = Marks.objects(subject=subject).distinct('student')
        for student in students:
            dict_to_template[subject][student.id] = {}
            dict_to_template[subject][student.id]['name'] = student.name
            dict_to_template[subject][student.id]['marks'] = {}
            student_marks = student.by_subject_marks(subject)
            for mark in student_marks:
                dict_to_template[subject][student.id]['marks'][mark.id] = mark.mark
    return render_template("marks_new.html", site_title=site_title, dict_to_template=dict_to_template)

@app.route("/edit_mark/<mark_id>", methods = ['POST'])
def edit_mark(mark_id):
    mark_to_edit = Marks.objects.get(id=mark_id)
    # print(mark)
    mark_to_edit.mark = request.form.get('mark_value')
    mark_to_edit.save()
    return redirect(url_for('makrs_page'))

@app.route("/delete_mark/<mark_id>")
def delete_mark(mark_id):
    mark_to_delete = Marks.objects.get(id=mark_id)
    mark_to_delete.delete()
    return redirect(url_for('makrs_page'))

@app.route("/add_mark", methods = ['GET','POST'])
def add_mark():
    if request.method == 'GET':
        students = Student.objects()
        return render_template("add_mark.html", site_title=site_title, students=students)
    else:
        subject_name = request.form.get('subject_name')
        student = request.form.get('student')
        mark = request.form.get('mark')
        mark_dict = {"subject":subject_name, "student": student, "mark": mark}
        Marks(**mark_dict).save()
        return redirect(url_for('makrs_page'))

@app.route("/curators")
def curators_page():
    curators = Curator.objects.all()
    return render_template("curators.html", site_title=site_title, curators=curators)

@app.route("/add_curator", methods = ['GET','POST'])
def add_curator():
    if request.method == 'GET':
        return render_template("add_curator.html", site_title=site_title)
    elif request.method == 'POST':
        curator_name = request.form.get('curator_name')
        Curator(**{'curator_name' : curator_name}).save()
        return redirect(url_for('curators_page'))
    else:
        pass

@app.route("/edit_curator/<curator_id>", methods = ['GET','POST'])
def edit_curator(curator_id):
    curator = Curator.objects.get(id=curator_id)
    if request.method == 'GET':
        return render_template("edit_curator.html", site_title=site_title, curator=curator)
    else:
        curator.curator_name = request.form.get('curator_name')
        curator.save()
        return redirect(url_for('curators_page'))

@app.route("/delete_curator", methods = ['POST'])
def delete_curator():
    curator_obj_id = request.form.get('curator_delete_form')
    curator_obj = Curator.objects.get(id=curator_obj_id)
    curator_obj.delete()
    return redirect(url_for('curators_page'))


if __name__ == "__main__":
    app.run(debug=True)
