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
