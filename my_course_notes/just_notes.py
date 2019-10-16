#
# import shelve
# from datetime import datetime
#
#
# class Shelve_DB:
#
#     def __init__(self, filename):
#         self._db = filename
#
#     @property
#     def USER_DB(self):
#         with shelve.open(self._db) as db:
#             USER_DB = db.get('USER_DB')
#             return USER_DB
#
#     @USER_DB.setter
#     def USER_DB(self, username):
#             with shelve.open(self._db) as db:
#                 register_date = datetime.today().strftime('%Y-%m-%d')
#                 USER_DB = db.get('USER_DB')
#                 USER_DB[username] = {"admin": False, "register_date":register_date}
#                 db["USER_DB"] = USER_DB
#
#     @property
#     def USERS_ACCESS_DB(self):
#         with shelve.open(self._db) as db:
#             USERS_ACCESS_DB = db.get('USERS_ACCESS_DB')
#             return USERS_ACCESS_DB
#
#     @USERS_ACCESS_DB.setter
#     def USERS_ACCESS_DB(self, username_password):
#         username, password = username_password
#         with shelve.open(self._db) as db:
#             USERS_ACCESS_DB = db["USERS_ACCESS_DB"]
#             USERS_ACCESS_DB[username] = password
#             db["USERS_ACCESS_DB"] = USERS_ACCESS_DB
#
# class SomeClass:
#     USER_DB = Shelve_DB.USER_DB
#     def __init__(self):
#         pass
#
#     def set_user(self, user):
#         SomeClass.USER_DB = user
#
#     def get_user(self):
#         return SomeClass.USER_DB
#
#
# db = Shelve_DB("test_db")
# obj = SomeClass()
#
# # print(db.USER_DB)
# # print(db.USER_DB)
# # obj.set_user("asdfasddfasdfasdf")
# # print(obj.get_user())
# # print(db.USER_DB)
#
#
#
#
#
# #
# # filename = "test_db"
# #
# # with shelve.open(filename) as db:
# #     db["USER_DB"] = {"admin": {"admin": "True", "register_date": "2019-10-09"}, "vasya":{"admin": False, "register_date": "2019-10-09"}}
# #     db["USERS_ACCESS_DB"] = {"admin":"111", "vasya":"q1"}
# #     db["POSTS"] = [{"date":"2000-01-31", "author": "vasya", "post": "some interesting  info"},
# #                  {"date":"2019-10-10", "author": "vasya", "post": "some other interesting  info"},
# #                  {"date":"2018-04-10", "author": "petya", "post": "text text text"}
# #                  ]
# # import shelve
# # filename = "test_db"
# # with shelve.open(filename) as db:
# #     USER_DB = db["USER_DB"]
# # print(USER_DB)






#
# from threading import Thread
# import time
# import random
#
# some_list = []
#
# def random_time_sleep(time_to_sl):
#     print("!!!!!!!!!!!!!!!!!!!Thread started")
#     time.sleep(random.randint(0, time_to_sl))
#     some_list.append(random.randint(0, time_to_sl))
#     print("!!!!!!!!!!!!!!!!!!!Thread finished")
#
# t = Thread(target=random_time_sleep, args=(5,))
# t.start()
#
#
#
# print("\nMain thread process......")
#
# for _ in range(10):#aninumus var
#     print("works")
#     some_list.append(str(random.randint(1, 10))
#     time.sleep(0.5)
#     print("Iteration ended")
#
#
# print(some_list)

def gen_func(start, end ,step):
    while start < end:
        start +=step
        yield start
    raise StopIteration

obj = gen_func(0,10,1)
print(obj)
iter_obj = iter(obj)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
