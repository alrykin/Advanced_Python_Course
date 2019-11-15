# 1) Написать контекстный менеджер для работы с SQLite DB.

import sqlite3

class DBContextManager:

    def __init__(self, db):
        self._db = db

    def __enter__(self):
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self._conn.commit()
        self._conn.close()


with DBContextManager("lesson7_practical.db") as db_obj:
    result = db_obj.execute("select * from user")
    #print(result.fetchone())

# 2) Создать базу данных студентов. У студента есть факультет,
# группа, оценки, номер студенческого билета. Написать программу,
# с двумя ролями: Администратор, Пользователь. Администратор
# может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки,
# факультет)

import sys
import time
from getpass import getpass
import hashlib
# В данном проекте, я использую hash+salt для хранения паролей пользователей
# реальные пароли учетных записей - admin:111, user:222
salt = "salty_water_)"

logo_text = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~ STUDENTS DB ~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

class User:

    def __init__(self, username, db):
        self._db = db
        self._user = username
        with DBContextManager(self._db) as db_obj:
            sql = """SELECT u.username, ro.role_name, ri.can_read, ri.can_write
                     FROM users u
                        INNER JOIN role ro ON u.role_id = ro.id
                        INNER JOIN rights ri ON ro.rights_id  = ri.id
                     where u.username = ?"""
            request = db_obj.execute(sql, [username])
            result = request.fetchall()
        self._role_name = result[0][1]
        self._can_read = result[0][2] == True# конвертируем 1/0 в True/False, мне так больше нравится)
        self._can_write = result[0][3] == True# конвертируем 1/0 в True/False, мне так больше нравится)

    @property
    def get_username(self):
        return self._user

    @property
    def get_role_name(self):
        return self._role_name

    @property
    def get_can_read(self):
        return self._can_read

    @property
    def get_can_write(self):
        return self._can_write



class Authorization:
    """ Class for authorization. Check if username and password are in students.users table.
    I use hash+salt for password storing in this project"""
    def __init__(self, db):
        self._username = ""
        self._db = db
        self._auth = False

    @property
    def get_username(self):
        return self._username

    @property
    def get_auth(self):
        return self._auth

    @property
    def get_db_name(self):
        return self._db

    @property
    def login(self):
        self._auth = True

    @property
    def logoff(self):
        self._auth = False

    def to_login(self):
        print(logo_text)
        self._username = input("Введите логин: ")
        print(self._username)

        with DBContextManager(self._db) as db_obj:
            sql = "SELECT username, password FROM users where username = ?"
            request = db_obj.execute(sql, [self._username])
            result = request.fetchall()
            db_obj.close()
            registered_user = {}
            for i in result:
                registered_user[i[0]] = i[1]
        if self._username  not in registered_user:
            print("\nПользователя с таким логином не существует.\n")
            return self.to_login()
        else:
            password = salt + getpass("Введите пароль: ")
            hash_password = hashlib.md5(password.encode()).hexdigest()
            if hash_password == registered_user[self._username]:
                print("\n           Добро пожаловать в базу данных СТУДЕНТЫ!\n")
                self.login
                return True
            else:
                print("Пароль не верен")
                return False


class Interface():
    """ Class for user interface creation """
    def __init__(self, user, auth_instance):
        self._auth_instance = auth_instance
        self._db = auth_instance.get_db_name
        self._user = user

    def logoff(self):
        self._auth_instance.logoff


    def get_auth(self):
        self._auth_instance.get_auth


    def form_student_name(self):
        student_name = input("Введите имя студента: ")
        print(student_name)
        if not student_name:
            print("Ошибка. Имя пользователя не может быть пустым")
            return None
        return student_name


    def form_student_facultet(self):
        facultets_available = []
        with DBContextManager(self._db) as db_obj:
            request = db_obj.execute("SELECT * FROM facultets")
            result = request.fetchall()
        input_message = ""
        facultet_id_list = []
        for i in result:
            input_message = input_message + "введите " + str(i[0]) + " для выбора факультета " + i[1] + "\n"
            facultet_id_list.append(str(i[0]))
        input_message = input_message + "выберите один из вариантов: "
        student_facultet = input(input_message)
        print(student_facultet)
        if not student_facultet or student_facultet not in facultet_id_list:
            print("Ошибка. Неверное значение факультета")
            return None
        return student_facultet


    def form_student_group_number(self):
        student_group_number = input("Введите номер группы студента: ")
        print(student_group_number)
        if not student_group_number:
            print("Ошибка. Номер группы не может быть пустым")
            return None
        return student_group_number


    def add_student(self):
        print("Меню создания новой записи студента")
        student_number = input("Cистема использует номер студентческого билета как уникальный идентифиатор студета\nвведите номер студентческого билета: ")
        if not student_number:
            print("Ошибка. Вы ничего не ввели")
            return None
        with DBContextManager(self._db) as db_obj:
            sql = "SELECT student_number FROM students where student_number = ?"
            request = db_obj.execute(sql, [student_number])
            result = request.fetchall()
        if result:
            print("Ошибка. Пользователь с таким студентческим номером уже существует")
            return None
        student_name = self.form_student_name()
        if not student_name:
            return None
        student_facultet = self.form_student_facultet()
        if not student_facultet:
            return None
        student_group_number = self.form_student_group_number()
        if not student_group_number:
            return None
        with DBContextManager(self._db) as db_obj:
            sql = "insert into students ('name', 'facultet', 'study_group', 'student_number') values (?, ?, ?, ?)"
            db_obj.execute(sql, [student_name, int(student_facultet), student_group_number, student_number])
            db_obj.execute('commit')
            print("Запись добавлена")


    def edit_student(self):
        print("Меню редактирования записи студента")

        student_number = input("Введите номер студентческого билета для редактирования: ")
        if not student_number:
            print("Ошибка. Вы ничего не ввели")
            return None
        with DBContextManager(self._db) as db_obj:
            sql = "select students.name, students.facultet, facultets.facultet_name, students.study_group from students inner join facultets on students.facultet = facultets.id where student_number = ?"
            request = db_obj.execute(sql, [student_number])
            result = request.fetchall()
        if not result:
            print("Ошибка. Пользователь с таким студентческим номером не найден")
            return None

        student_name, student_facultet, student_facultet_name, student_group_number = result[0]
        print(f"Меню изненения записи для студента c номером {student_number}\n")
        print("Текущее значение имени: " + student_name)
        print("Для изменения введите Y, оставить прежнее значение - введите Enter\nДля выхода в главное меню - введите любой символ")
        answer = input("Выберите один из вариантов: ")
        if answer == "Y":
            student_name = self.form_student_name()
        elif answer == "":
            pass
        else:
            return None

        print("Текущее значение факультет: " + student_facultet_name)
        print("Для изменения введите Y, оставить прежнее значение - введите Enter\nДля выхода в главное меню - введите любой символ")
        answer = input("Выберите один из вариантов: ")
        if answer == "Y":
            student_facultet = self.form_student_facultet()
        elif answer == "":
            pass
        else:
            return None

        print("Текущее значение группа: " + student_group_number)
        print("Для изменения введите Y, оставить прежнее значение - введите Enter\nДля выхода в главное меню - введите любой символ")
        answer = input("Выберите один из вариантов: ")
        if answer == "Y":
            student_group_number = self.form_student_group_number()
        elif answer == "":
            pass
        else:
            return None

        with DBContextManager(self._db) as db_obj:
            sql = "update students set 'name' = ?, 'facultet' = ?, 'study_group' = ?  where student_number = ?"
            db_obj.execute(sql, [student_name, int(student_facultet), student_group_number, student_number])
            db_obj.execute('commit')
            print("Запись изменена")


    def show_students(self, student_number=None, mark5=None):
        with DBContextManager(self._db) as db_obj:
            if mark5:
                sql = """select name, student_number from
                (select students.name, students.student_number, st_marks.subject, min(st_marks.mark) as min_mark from students
                inner join st_marks
                on students.id = st_marks.student_id
                group by students.name) as t
                where min_mark = 5"""
                request = db_obj.execute(sql)
            elif student_number:
                sql = 'select name,  student_number from students where student_number like ?'
                request = db_obj.execute(sql, ['%'+student_number+'%'])
            else:
                request = db_obj.execute("select name,  student_number  from students")
            result = request.fetchall()
        print("-"*70)
        for i in result:
            print("Имя: " + i[0], " | Номер студентческого билета: " + i[1])
        print("-"*70)


    def show_student_detail(self, student_number):
        with DBContextManager(self._db) as db_obj:
            sql = """select students.name, students.student_number, students.study_group, facultets.facultet_name
            from students
            inner join facultets
            on students.facultet = facultets.id
            where student_number = ?"""
            sql_marks = """select st_marks.subject, GROUP_CONCAT(st_marks.mark) from students
            inner join st_marks
            on students.id =  st_marks.student_id
            where student_number = ?
            GROUP BY subject
            """
            request = db_obj.execute(sql, [student_number])
            result = request.fetchall()
            request_marks = db_obj.execute(sql_marks, [student_number])
            result_marks = request_marks.fetchall()
        print("="*70)
        print("Имя: " + result[0][0])
        print("Номер студентческого: " + result[0][1])
        print("Номер группы: " + result[0][2])
        print("Факультет: " + result[0][3])
        print("Оценки:")
        for i in result_marks:
            print(i[0], ":", i[1])
        print("="*70)


    def search_student(self, detail_search=False):
        student_number = input("Укажите параметры поиска (номер студентческого билета): ")
        if not student_number:
            print("Вы не указали параметры поиска (номер студентческого билета)")
        elif detail_search == True:
            self.show_student_detail(student_number)
        else:
            self.show_students(student_number)


    def run(self):
        print("\n~ Меню ~")
        print("Введите 1 для выхода из учетной записи")
        print("Введите 2 для просмотра списка всех студентов")
        print("Введите 3 для поиска студента по номеру студентческого билета")
        print("Введите 4 для просмотра подробной информации о студенте")
        print("Введите 5 чтобы просмотреть список отличников")
        print("Введите exit для выхода из программы")
        print("~ Админ меню ~ (ограничение по доступам роли пользователя)")
        print("Введите add чтобы добавить нового студента")
        print("Введите edit чтобы изменить существующего студента")
        user_input = input()
        if user_input == "1":
            self.logoff()
        elif user_input == "2":
            self.show_students()
        elif user_input == "3":
            self.search_student()
        elif user_input == "4":
            self.search_student(True)
        elif user_input == "5":
            self.show_students(None, True)
        elif user_input == "add":
            if self._user.get_can_write:
                self.add_student()
            else:
                print("!!! У Вас нет прав на добавление записей !!!")
        elif user_input == "edit":
            if self._user.get_can_write:
                self.edit_student()
            else:
                print("!!! У Вас нет прав на изменение записей !!!")
        elif user_input == "exit":
            sys.exit()
        else:
            print("Данной опции не существует")




db = "students.db"
while True:
    auth_instance = Authorization(db)
    auth_instance.to_login()
    Auth = auth_instance.get_auth
    while Auth:
        user = User(auth_instance.get_username, auth_instance.get_db_name)
        interface_instance = Interface(user, auth_instance)
        interface_instance.run()
        Auth = auth_instance.get_auth
