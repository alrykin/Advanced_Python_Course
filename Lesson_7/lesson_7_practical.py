# 1) Написать контекстный менеджер для работы с SQLite DB.

import sqlite3

class DBContextManager:

    def __init__(self, db):
        self._db = db

    def __enter__(self):
        #print("db context manager enter")
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        #print("exit from db context manager, closing db")
        self._conn.commit()
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
# Наследуемся от ранее созданного контекст менеджера
# DBContextManager и добавляем некоторые propertys для удобства работы с БД
class DB_Connector(DBContextManager):
    # задать вопрос, нужрно ли вообще инициализировать инит если он уже наследоварн ???
    def __init__(self, db):
        super().__init__(db)

    def get_registered_user(self, username):
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        sql = "SELECT username, password FROM users where username = ?"
        request = self._cursor.execute(sql, [username])
        result = request.fetchall()
        self._conn.close()
        registered_user = {}
        for i in result:
            registered_user[i[0]] = i[1]
        return registered_user



# class User:
#
#     def __init__(self, username):
#         self._user = username
#         self._role_name = "admin"
#         self._can_read = True
#         self._can_write = True
#
#     @property
#     def get_username(self):
#         return self._user
#
#     @property
#     def get_role_name(self):
#         return self._role_name
#
#     @property
#     def get_can_read(self):
#         return self._can_read
#
#     @property
#     def get_can_write(self):
#         return self._can_write



class Authorization:
    """ Class for authorization. Check if username and password are in students.users table.
    I use hash+salt for password storing in this project"""
    def __init__(self):
        self._username = ""

    def to_login(self):
        print(logo_text)
        self._username = input("Введите логин: ")
        print(self._username)
        registered_user = db.get_registered_user(self._username)
        if self._username  not in registered_user:
            print("\nПользователя с таким логином не существует.\n")
            return self.to_login()
        else:
            password = salt + getpass("Введите пароль: ")
            hash_password = hashlib.md5(password.encode()).hexdigest()
            if hash_password == registered_user[self._username]:
                print("\n           Добро пожаловать в базу данных СТУДЕНТЫ!\n")
                return True
            else:
                print("Пароль не верен")
                return False



class Interface():
    """ Class for user interface creation """
    def __init__(self):
        pass
        # self._username = user.get_username
        # self._get_role_name = user._get_role_name
        # self._can_read = user._can_read
        # self._can_write = user._can_write


    def form_student_name(self):
        student_name = input("Введите имя студента: ")
        print(student_name)
        if not student_name:
            print("Ошибка. Имя пользователя не может быть пустым")
            self.run()
        return student_name


    def form_student_facultet(self):
        facultets_available = []
        with DBContextManager("students.db") as db_obj:
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
            self.run()
        return student_facultet


    def form_student_group_number(self):
        student_group_number = input("Введите номер группы студента: ")
        print(student_group_number)
        if not student_group_number:
            print("Ошибка. Номер группы не может быть пустым")
            self.run()
        return student_group_number


    def add_student(self):
        print("Меню создания новой записи студента")
        student_number = input("Cистема использует номер студентческого билета как уникальный идентифиатор студета\nвведите номер студентческого билета: ")
        print(student_number)
        with DBContextManager("students.db") as db_obj:
            sql = "SELECT student_number FROM students where student_number = ?"
            request = db_obj.execute(sql, [studen_number])
            result = request.fetchall()
        if result:
            prtin("Ошибка. Пользователь с таким студентческим номером уже существует")
            self.run()
        student_name = self.form_student_name()
        student_facultet = self.form_student_facultet()
        student_group_number = self.form_student_group_number()
        with DBContextManager("students.db") as db_obj:
            sql = "insert into students ('name', 'facultet', 'study_group', 'student_number') values (?, ?, ?, ?)"
            db_obj.execute(sql, [student_name, int(student_facultet), student_group_number, student_number])
            print("Запись добавлена")


    def edit_student(self):
        print("Меню редактирования записи студента")
        student_number = input("Введите номер студентческого билета для редактирования: ")
        with DBContextManager("students.db") as db_obj:
            sql = "select students.name, students.facultet, facultets.facultet_name, students.study_group from students inner join facultets on students.facultet = facultets.id where student_number = ?"
            request = db_obj.execute(sql, [student_number])
            result = request.fetchall()
        if not result:
            print("Ошибка. Пользователь с таким студентческим номером не найден")
            self.run()
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
            self.run()

        print("Текущее значение факультет: " + student_facultet_name)
        print("Для изменения введите Y, оставить прежнее значение - введите Enter\nДля выхода в главное меню - введите любой символ")
        answer = input("Выберите один из вариантов: ")
        if answer == "Y":
            student_facultet = self.form_student_facultet()
        elif answer == "":
            pass
        else:
            self.run()

        print("Текущее значение группа: " + student_group_number)
        print("Для изменения введите Y, оставить прежнее значение - введите Enter\nДля выхода в главное меню - введите любой символ")
        answer = input("Выберите один из вариантов: ")
        if answer == "Y":
            student_group_number = self.form_student_group_number()
        elif answer == "":
            pass
        else:
            self.run()

        with DBContextManager("students.db") as db_obj:
            sql = "update students set 'name' = ?, 'facultet' = ?, 'study_group' = ?  where student_number = ?"
            db_obj.execute(sql, [student_name, int(student_facultet), student_group_number, student_number])
            print("Запись изменена")

        self.run()


    def show_students(self, student_group_number=None):
         with DBContextManager("students.db") as db_obj:
             if not student_group_number:
                 request = db_obj.execute("select name,  student_number  from students")
             else:
                 sql = "select name,  student_number, from students where student_group_number = ?"
                 request = db_obj.execute(sql, [student_group_number])
             result = request.fetchall()
             print(result)
         self.run()


    def run(self):
        # if self._is_admin:
        user_input = input("\n~ Меню ~\nВведите 1 для выхода\nВведите 2 для просмотра списка всех студентов\nВведите 3 для поиска студента по номеру студентческого билета\nВведите 4 для просмотра подробной информации о студенте\nВведите 5 чтобы просмотреть список отличников\n")
        if user_input == "1":
            pass
        elif user_input == "2":
            self.show_students()
            time.sleep(1)
            self.run()
        elif user_input == "3":
            pass
            time.sleep(1)
            self.run()
        elif user_input == "4":
            pass
            time.sleep(1)
            self.run()
        elif user_input == "5":
            pass
            time.sleep(1)
            self.run()





while True:
    db = DB_Connector("students.db")
    init_auth = Authorization()
    Auth =  init_auth.to_login()
    if Auth:
        #user = User(init_auth.get_username)
        interface_instance = Interface()
        interface_instance.run()
    else:
        pass
