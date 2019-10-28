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
    student_obj.delete_with_dependencys
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

@app.route("/marks")
def makrs_page():
    marks = Marks.objects.all()
    return render_template("marks.html", site_title=site_title, marks=marks)

@app.route("/curators")
def curators_page():
    curators = Curator.objects.all()
    return render_template("curators.html", site_title=site_title, curators=curators)

if __name__ == "__main__":
    app.run(debug=True)
