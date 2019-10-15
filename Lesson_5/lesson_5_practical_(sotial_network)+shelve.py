# Создать подобие социальной сети. Описать классы, которые должны
# выполнять соответствующие функции (Предлагаю насследовать класс
# авторизации от класса регистрации). Добавить проверку на валидность
# пароля (содержание символов и цифр), проверка на уникальность логина
# пользователя. Человек заходит, и имеет возможность зарегистрироваться
# (ввод логин, пароль, потдверждение пароля), далее входит в свою учетную
# запись. Добавить возможность выхода из учетной записи, и вход в новый
# аккаунт. Создать класс User, котоырй должен разделять роли обычного
# пользователя и администратора. При входе под обычным пользователем мы
# можем добавить новый пост, с определённым содержимим, так же пост
# должен содержать дату публикации. Под учётной записью администратора
# мы можем увидеть всех пользователей нашей системы, дату их регистрации,
# и их посты.

## Дополнение модулем shelve

from getpass import getpass
from datetime import datetime
import time
import shelve

logo_text = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~ С О Ц С Е Т Ь ~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


class Shelve_DB:
    """ class for working with shelve storage. Getters and setters """
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
    def USERS_ACCESS_DB(self, uname_pass_tuple):
            username, password = uname_pass_tuple
            with shelve.open(self._db) as db:
                USERS_ACCESS_DB = db["USERS_ACCESS_DB"]
                USERS_ACCESS_DB[username] = password
                db["USERS_ACCESS_DB"] = USERS_ACCESS_DB

    @property
    def POSTS(self):
        with shelve.open(self._db) as db:
            return db.get('POSTS')

    @POSTS.setter
    def POSTS(self, post):
        with shelve.open(self._db) as db:
            POSTS = db.get('POSTS')
            POSTS.append(post)
            db["POSTS"] = POSTS



class User:

    def __init__(self, username):
        USER_DB = db.USER_DB
        self._user = username
        self._register_date = USER_DB[username]["register_date"]
        self._is_admin = USER_DB[username]["admin"]

    @property
    def username(self):
        return self._user

    @property
    def register_date(self):
        return self._register_date

    @property
    def is_admin(self):
        return self._is_admin



class Register:
    """ Class for users registration """
    def __init__(self):
        pass

    def password_validator(self, password):
        if any(char.isdigit() for char in password):
            if any(char.isalpha() for char in password):
                return True
            else:
                return False
        else:
            return False

    def to_register(self):
        username = input("Введите логин, который будет использоваться для входа: ")
        if not username:
            print("Пользователь не может быть пустым")
            return self.to_register()
        elif username in db.USERS_ACCESS_DB:
            print("Пользователь с таким идентификатором уже существует")
            return self.to_register()
        else:
            self._username = username
            password = getpass("Введите пароль, который будет использоваться для входа: ")
            if self.password_validator(password):
                pass
            else:
                print("Пароль должен содержать минимум одну цифру и одну букву")
                return self.to_register()
            password_rep = getpass("Повторите пароль: ")
            if password == password_rep:
                db.USERS_ACCESS_DB = (username, password)
                db.USER_DB = username
                print("\n           Добро пожаловать в нашу соц.сеть!\n")
                return True
            else:
                print("Пароли не совпадают, повторите попытку")
                return self.to_register()

    @property
    def get_username(self):
        return self._username



class Authorization(Register):
    """ Class for authorization. Check if username and password are in USERS_ACCESS_DB """
    def __init__(self):
        self._username = ""

    def to_login(self):
        print(logo_text)
        print("Для входа, нажмите Enter")
        print("Для регистрации, введите 1\n")
        choice = input()
        if choice == "1":
            return super().to_register()
        username = input("Введите логин: ")
        self._username = username
        print(self._username)
        USERS_ACCESS_DB = db.USERS_ACCESS_DB
        if username  not in USERS_ACCESS_DB:
            print("\nПользователя с таким логином не существует.\n")
            return self.to_login()
        else:
            password = getpass("Введите пароль: ")
            if password == USERS_ACCESS_DB[username]:
                print("\n           Добро пожаловать в нашу соц.сеть!\n")
                return True
            else:
                print("Пароль не верен")
                return False

    @property
    def get_username(self):
        return self._username



class Interface():
    """ Class for user interface creation depending on the user rights (is_admin ?) """
    def __init__(self, user):
        self._register_date = user.register_date
        self._username = user.username
        self._is_admin = user.is_admin

    def create_post(self):
        post = input("\nВведите текст Вашего поста\n")
        if post:
            date = datetime.today().strftime('%Y-%m-%d')
            db.POSTS = {"date": date, "author": self._username, "post": post}
            print("Пост добавлен")

    def get_users_info(self):
        print("\nПользователи системы:\n")
        USER_DB = db.USER_DB
        for i in USER_DB:
            print("="*55)
            print("username: " + i + "\nдата регистрации: " + USER_DB[i]["register_date"])
            self.get_author_posts(i)
            print("="*55)

    def get_posts(self):
        print("\nРанее созданные посты:\n")
        for n in db.POSTS:
            print("post created " + n["date"] + " by " + n["author"] + "\n" + n["post"] + "\n")

    def get_author_posts(self, author):
        POSTS = db.POSTS
        for n in POSTS:
            if  n["author"] == author:
                print("post created " + n["date"] + " by " + n["author"] + "\n" + n["post"] + "\n")

    def run(self):
        if self._is_admin:
            user_input = input("\n~ Меню ~\nВведите 1 для выхода\nВведите 2 для создания поста\nВведите 3 для просмотра постов\nВведите 4 для просмотра информации о пользователях системы\n")
            if user_input == "1":
                pass
            elif user_input == "2":
                self.create_post()
                time.sleep(1)
                self.run()
            elif user_input == "3":
                self.get_posts()
                time.sleep(1)
                self.run()
            elif user_input == "4":
                self.get_users_info()
                time.sleep(1)
                self.run()
            else:
                time.sleep(1)
                self.run()
        else:
            user_input = input("\n~ Меню ~\nВведите 1 для выхода\nВведите 2 для создания поста\nВведите 3 для просмотра постов\n")
            if user_input == "1":
                pass
            elif user_input == "2":
                self.create_post()
                time.sleep(1)
                self.run()
            elif user_input == "3":
                self.get_posts()
                time.sleep(1)
                self.run()
            else:
                time.sleep(1)
                self.run()


db = Shelve_DB("sotial_network_db")
while True:
    init_auth = Authorization()
    Auth =  init_auth.to_login()
    if Auth:
        user = User(init_auth.get_username)
        interface_instance = Interface(user)
        interface_instance.run()
    else:
        pass
