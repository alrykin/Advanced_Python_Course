#
# ~~~~ LAMBDA
#

# z = lambda obj: obj + 100
# print((lambda obj: obj + 100)(1))
#
# list_t = [1,2,3,4,5,6]
#
# ## map
# print(list(map(lambda value: value*2, list_t)))
#
# ## filter если тру то ...
# print(list(filter(lambda value: True if value % 2 == 0 else False, list_t)))
# print(list(filter(lambda value: value % 2 == 0, list_t)))
#
#
# def func1(a):
#     print(f"i am func1 my arg is {a}")
#     def func2(b):
#         print(f"i am func2 my arg is {b}")
#         def func3(c):
#             print(f"i am func3 my arg is {c}")
#         return func3
#     return func2
#
# func1(1)(2)(3)

################################################################################
#
# ~~~~ Decorators
#
#
# def my_decorator(func):
#
#     def wrapper():
#         print("started wrappind")
#         func()
#         print("started wrappind")
#
#     return wrapper
#
#
# def hello_world():
#     print("привет мир")
#
# # декорируем функцию hello_world
# my_decorator(hello_world)()
#
#
#

#
# def my_decorator(func):
#
#     def wrapper(name):
#         print("started wrappind")
#         result = func(name)
#         print("finished wrappind")
#         return (result, "wrapped")
#     return wrapper
#
#
# # def hello_world():
# #     return "Hello great world"
# #
# # # декорируем функцию hello_world
# # result = my_decorator(hello_world)()
# # print(result)
#
#
#
# # ну, а можно с помощью синтаксического сахара
#
#
#
#
# @my_decorator
# def hello_world(name):
#     return f"Hello, {name}"
#
# print(hello_world("NAMEEEE"))
#
#
#
#
#
#
# def my_decorator(func):
#
#     def wrapper(*args, **kwargs):
#         print("started wrappind")
#         result = func(*args, **kwargs)
#         print("finished wrappind")
#         return (result, "wrapped")
#     return wrapper
#
#
# @my_decorator
# def hello_world(name):
#     return f"Hello, {name}"
#
# print(hello_world("NAMEEEE"))
#
#







# def decorator(num_of_repeats=1):
#     def actual_decorator(func):
#
#         def wrapper(*args, **kwargs):
#             print("Started wrapping")
#             results = []
#             for i in range(num_of_repeats):
#                 result = func(*args, **kwargs)
#                 results.append(result)
#
#             print("Wrapped")
#             return (results, "Wrapped")
#
#         return wrapper
#     return actual_decorator
#
# @decorator(10)
# def say_hello(name):
#     return f"Hello, {name}"
#
# print(say_hello("Alex"))


#
#
### реализация паттерна программирования Sengletone только 1 экземпляр  класса
class SengletoneExample:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            raise Exception("instance already eists")
        return instance

    def __init__(self):
        self._x = 10
        self._y = 20

a = SengletoneExample()
#b = SengletoneExample()# будет ошибка

a._x = 100

print(a._x)
#print(b._x)
