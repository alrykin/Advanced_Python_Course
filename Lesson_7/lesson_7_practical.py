# 1) Написать контекстный менеджер для работы с SQLite DB.
# 2) Создать базу данных студентов. У студента есть факультет,
# группа, оценки, номер студенческого билета. Написать программу,
# с двумя ролями: Администратор, Пользователь. Администратор
# может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки,
# факультет)

import sqlite3

class DBContextManager:

    def __init__(self, db):
        self._db = db

    def __enter__(self):
        print("db context manager enter")
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit from db cm")
        self._conn.close()


with DBContextManager("mydb.db") as db_obj:
    result = db_obj.execute("insert into user (login, password) values ('a', '111')")
    
