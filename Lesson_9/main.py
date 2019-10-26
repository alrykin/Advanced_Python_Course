# 1) Создать базу данных студентов (ФИО, группа, оценки, куратор
# студента, факультет). Написать CRUD ко всем полям. Описать
# методы для вывода отличников по каждому факультету. Вывести
# всех студентов определенного куратора.

from flask import  Flask, render_template, request, redirect, url_for


app = Flask(__name__)
store_title = "CRUD"

@app.route("/")
def home():
    return "Hello"
    #return render_template("index.html", store_title=store_title, categories_dict=categories_dict)




if __name__ == "__main__":
    app.run(debug=True)
