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



class User:

    def __init__(self, username):
        self._user = username
        self._register_date = USER_DB[username]["register_date"]
        self._is_admin = USER_DB[username]["admin"]

    @property
    def username(self):
        return self._user

    @property
    def is_admin(self):
        return self._is_admin



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



db = DB_Connector("students.db")
while True:
    init_auth = Authorization()
    Auth =  init_auth.to_login()
    if Auth:
        # user = User(init_auth.get_username)
        # interface_instance = Interface(user)
        # interface_instance.run()
        pass
    else:
        pass
