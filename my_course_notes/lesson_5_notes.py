# # использование метода __call__
#
# class Some:
#     """some documentation string"""
#     def __init__(self, a, b):
#         self._a = a
#         self._b = b
#     def __call__(self, *args, **kwargs):
#         print(self.__dict__)
#         print(self.__doc__)
#         return self._a + self._b
#
#
# obj = Some(1,2)
# print(obj(111))

# # вариант использование колл для декорирования
# class Dec:
#     def __init__(self, f):
#         self.f = f
#     def __call__(self,*args,**kwargs):
#         print("Start Decor")
#         self.f()
#         print("End Decor")
#
# @Dec
# def func():
#     print("hello")
# func()



# ####  LIST COMPREHANTIONS  #####
# # чтобы не итерировать для создания списков можно использовать это
# my_list = [i**2 for i in range(100)]
# print(my_list)
#
# # Пример с условием - только парные числа
# my_list = [i for i in range(100) if not i % 2 ]
# print(my_list)


# # Для словаря
# m_dict = dict(
#     key1 = "a",
#     key2 = "b"
# )
#
# new_dict = {key : value for key , value in m_dict.items() if value == "a"}
# print(new_dict)


################################################################
################################################################
####### ПОТОКИ
# threading это псевдо паралелизм,
#
#
#
# from threading import Thread
# import time, random
#
# def random_time_sleep(time_to_sl):
#     print("!!!!!!!!!!!!!!!!!!!Thread started")
#     time.sleep(random.randint(0, time_to_sl))
#     print("!!!!!!!!!!!!!!!!!!!Thread finished")
#
# t = Thread(target=random_time_sleep, args=(5,))
# t.start()
#
#
# print("\nMain thread process......")
#
# for _ in range(10):#aninumus var
#     print("works")
#     time.sleep(0.5)
#     print("Iteration ended")


# # чтобы сломать если основной поток помрет включаем демон режим
# from threading import Thread
# import time, random
#
# def random_time_sleep(time_to_sl):
#     print("!!!!!!!!!!!!!!!!!!!Thread started")
#     time.sleep(random.randint(0, time_to_sl))
#     print("!!!!!!!!!!!!!!!!!!!Thread finished")
#
# t = Thread(target=random_time_sleep, args=(5,), daemon = True)
# t.start()
#
#
# print("Main thread process......")
#
# for _ in range(10):#aninumus var
#     print("works")
#     time.sleep(0.5)
#     x = 100/0
#     print("Iteration ended")



# from threading import Thread
# import time, random
#
# def random_time_sleep(time_to_sl):
#     print("!!!!!!!!!!!!!!!!!!!Thread started")
#     time.sleep(random.randint(0, time_to_sl))
#     print("!!!!!!!!!!!!!!!!!!!Thread fitished")
#
# t = Thread(target=random_time_sleep, args=(5,),)
# t.start()
#
# print("Main thread process......")
#
# for _ in range(10):#aninumus var
#     print("works")
#     t.join()#обьединяем в один поток тогда  будем ждать выполнения первого
#     time.sleep(0.5)
#     print("Iteration ended")

# у потоков есть методы, например t.is_alive() , потоки можно именовать
# t = Thread(target=random_time_sleep, args=(5,), name = "MyMethodNameee")
# from threading import Thread
# import time, random

# def random_time_sleep(time_to_sl):
#     print("!!!!!!!!!!!!!!!!!!!Thread started")
#     time.sleep(random.randint(0, time_to_sl))
#     print("!!!!!!!!!!!!!!!!!!!Thread fitished")
#
# t = Thread(target=random_time_sleep, args=(5,),)
# t.start()
#
# print("Main thread process......")
#
# for _ in range(10):#aninumus var
#     print("works")
#     print(t.is_alive())
#     print(t.getName())
#     time.sleep(0.5)
#     print("Iteration ended")


## Потоки на классах
# from threading import Thread
# import time, random
#
# class MyThread(Thread):
#     def __init__(self, name, is_daemon):
#         super().__init__(name=name, daemon=is_daemon)
#
#     def run(self):
#         for  i in range(5):
#             print("i am class thread"+ self.name)
#             time.sleep(0.2)
#
# t = MyThread("NameT", False)
# z = MyThread("NameZ", False)
# t.start()
# z.start()

# with open("sadf", "w") as file:
#   afass;jd

# это синтакс сахар, ме его мжетс сами создать

# class ContextManagerExample:
#
#     def __init__(self, a):
#         self._a = a
#         self._state = "active"
#
#     def __enter__(self):
#         print("cm enter")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exit from cm")
#         self._state = "inactive"
#
#     def process(self):
#         print("Processing data")
#
# # obj = ContextManagerExample(10)
# # print(obj._state)
# # obj.process()
#
# with ContextManagerExample(10) as new_obj:
#     print(new_obj._state)
#     new_obj.process
#
# print(new_obj._state)
#
# #### SHELVE #####
# import shelve
#
# filename = "my_db"
#
# with shelve.open(filename) as db:
#     db["key"] = "1000"
#
# def create_user(username):
#     with shelve.open(filename) as db:
#         print(db.items())# вернет иретируемый  обьект
#         print(db["key"])
#         db.has_key(username)# если есть такой  юзер - ексепшн
#         db[f'{username}_posts'] = ['post_1', 'post2']
#
# def get_post(username):
#     with shelve.open(filename) as db:
#         user_posts = db.get(f'username_posts')
