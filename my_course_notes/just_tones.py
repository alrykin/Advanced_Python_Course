


import shelve
from datetime import datetime


class Shelve_DB:

    def __init__(self, filename):
        self._db = filename

    @property
    def USER_DB(self):
        with shelve.open(self._db) as db:
            USER_DB = db.get('USER_DB')
            return USER_DB

    @USER_DB.setter
    def USER_DB(self, username):
            with shelve.open(self._db) as db:
                register_date = datetime.today().strftime('%Y-%m-%d')
                USER_DB = db.get('USER_DB')
                USER_DB[username] = {"admin": False, "register_date":register_date}
                db["USER_DB"] = USER_DB

    @property
    def USERS_ACCESS_DB(self):
        with shelve.open(self._db) as db:
            USERS_ACCESS_DB = db.get('USERS_ACCESS_DB')
            return USERS_ACCESS_DB

    @USERS_ACCESS_DB.setter
    def USERS_ACCESS_DB(self, username_password):
        username, password = username_password
        with shelve.open(self._db) as db:
            USERS_ACCESS_DB = db["USERS_ACCESS_DB"]
            USERS_ACCESS_DB[username] = password
            db["USERS_ACCESS_DB"] = USERS_ACCESS_DB

class SomeClass:

    def __init__(self, db):
        self.USER_DB = db["USER_DB"]

    def set_user(self, user):
        self.USER_DB = user

    def get_user(self):
        return self.USER_DB


db = Shelve_DB("test_db")
obj = SomeClass(db)
print(obj.get_user())
print(db.USER_DB)
obj.set_user("asdfasddfasdfasdf")
print(obj.get_user())
print(db.USER_DB)





#
# filename = "test_db"
#
# with shelve.open(filename) as db:
#     db["USER_DB"] = {"admin": {"admin": "True", "register_date": "2019-10-09"}, "vasya":{"admin": False, "register_date": "2019-10-09"}}
#     db["USERS_ACCESS_DB"] = {"admin":"111", "vasya":"q1"}
#     db["POSTS"] = [{"date":"2000-01-31", "author": "vasya", "post": "some interesting  info"},
#                  {"date":"2019-10-10", "author": "vasya", "post": "some other interesting  info"},
#                  {"date":"2018-04-10", "author": "petya", "post": "text text text"}
#                  ]
# import shelve
# filename = "test_db"
# with shelve.open(filename) as db:
#     USER_DB = db["USER_DB"]
# print(USER_DB)
