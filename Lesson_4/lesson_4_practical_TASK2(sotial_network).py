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

from getpass import getpass
from datetime import datetime

logo_text = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~ С О Ц С Е Т Ь ~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

class User:

    USER_DB = {"admin":{"admin": "True", "register_date": "2019-10-09"}, "vasya":{"admin": False, "register_date": "2019-10-09"}}

    def __init__(self, username):
        self._user = username
        self._register_date = User.USER_DB[username]["register_date"]
        self._is_admin = User.USER_DB[username]["admin"]

    @property
    def username(self):
        return self._user

    @property
    def register_date(self):
        return self._register_date

    @property
    def is_admin(self):
        return self._is_admin

    @classmethod
    def user_register(cls, username, admin=False):
        register_date = datetime.today().strftime('%Y-%m-%d')
        cls.USER_DB[username] = {"admin":admin, "register_date":register_date}



class Register:

    USERS_ACCESS_DB = {"admin":"111"}

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
            #return self.to_register()
        elif username in Register.USERS_ACCESS_DB:
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
                Register.USERS_ACCESS_DB[username] = password
                User.user_register(username)
                print("\n           Добро пожаловать в нашу соц.сеть!\n")
                return True
            else:
                print("Пароли не совпадают, повторите попытку")
                return self.to_register()

    @property
    def get_username(self):
        return self._username



class Authorization(Register):

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
        if username  not in super().USERS_ACCESS_DB:
            print("\nПользователя с таким логином не существует.\n")
            return self.to_login()
        else:
            password = getpass("Введите пароль: ")
            if password == super().USERS_ACCESS_DB[username]:
                print("\n           Добро пожаловать в нашу соц.сеть!\n")
                return True
            else:
                print("Пароль не верен")
                return False

    @property
    def get_username(self):
        return self._username



class Interface():

    POSTS = [{"date":"2000-01-31", "author": "vasya", "post": "some interesting  info"},
             {"date":"2019-10-10", "author": "vasya", "post": "some other interesting  info"},
             {"date":"2018-04-10", "author": "petya", "post": "text text text"}
             ]

    def __init__(self, user):
        self._register_date = user.register_date
        self._username = user.username
        self._is_admin = user.is_admin

    def create_post(self):
        post = input("\nВведите текст Вашего поста\n")
        date = datetime.today().strftime('%Y-%m-%d')
        Interface.POSTS.append({"date": date, "author": self._username, "post": post})
        print("Пост добавлен")

    def get_users_info(self):
        print("\nПользователи системы:\n")
        for i in User.USER_DB:
            print("=======================================================")
            print("username: " + i + "\nдата регистрации: " + User.USER_DB[i]["register_date"] + "\n")
            self.get_author_posts(i)
            print("=======================================================")

    def get_posts(self):
        print("\nРанее созданные посты:\n")
        for n in Interface.POSTS:
            print("post created " + n["date"] + " by " + n["author"] + "\n" + n["post"] + "\n")

    def get_author_posts(self, author):
        for n in Interface.POSTS:
            if  n["author"] == author:
                print("post created " + n["date"] + " by " + n["author"] + "\n" + n["post"] + "\n")

    def run(self):
        if self._is_admin:
            user_input = input("\nМеню\nВведите 1 для выхода\nВведите 2 для создания поста\nВведите 3 для просмотра постов\nВведите 4 для просмотра информации о пользователях системы\n")
            if user_input == "1":
                pass
            elif user_input == "2":
                self.create_post()
                self.run()
            elif user_input == "3":
                self.get_posts()
                self.run()
            elif user_input == "4":
                self.get_users_info()
                self.run()
            else:
                self.run()
        else:
            user_input = input("\nМеню\nВведите 1 для выхода\nВведите 2 для создания поста\nВведите 3 для просмотра постов\n")
            if user_input == "1":
                pass
            elif user_input == "2":
                self.create_post()
                self.run()
            elif user_input == "3":
                self.get_posts()
                self.run()
            else:
                self.run()


while True:
    init_auth = Authorization()
    Auth =  init_auth.to_login()
    if Auth:
        user = User(init_auth.get_username)
        interface_instance = Interface(user)
        interface_instance.run()
    else:
        pass
