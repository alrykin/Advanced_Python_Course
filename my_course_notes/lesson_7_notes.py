import sqlite3
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
# Создаем курсор - это специальный объект который делает
# запросы и получает их результаты

resp = cursor.execute("SELECT * FROM user")
# print(resp.fetchone())# как генератор
# print(resp.fetchall())# вернет в кортеже список из кортежей

for u in resp:
    (u_id, u_ligin, u_pass) = u
    print(u_id)
    print(u_ligin)
    print(u_pass)

conn.close()

# login = input("enter the login")
# password = input("enter the pass")
# sql = "INSERT INTO user (login, password) values (?, ?)"
# query_responce = cursor.execute(sql, [login, password])
