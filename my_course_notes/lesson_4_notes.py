# tup = tuple([1,2])
# print(type(str))
#
# my_class = type(
#         "ClassExammppll",
#         (),
#         {
#             "attr_1":100,
#             "attr_2": 200,
#             "get_attr_1": lambda self: self.attr_1,#self - можетбыть любое слово
#             "get_attr_2": lambda self: self.attr_2,
#         }
#     )
#
# obj = my_class()
# print(obj.attr_1)
# print(obj.get_attr_1())




# # Создадим свой метакласс . Для абсолютного контроля того , что происходит при создании пользовательского класса
# class MyMetaClass(type):
#     def __new__(mcs, name, base, attrs):
#         print(mcs, name, base, attrs)
#
#         if  "CLASS_FIELD3" in attrs:# например, мы не хотим чтобы пользователь мог создать такое поле
#             raise Exception("Unsupportable field")
#
#         if  attrs.get("CLASS_FIELD1", 0) < 100: # если CLASS_FIELD1 нет , то ставим 0 , если есть , и оно меньше 100 , то уснатовим ему 1000
#             attrs["CLASS_FIELD1"] = 1000
#
#         if  not attrs.get("very_well_field", 0):# если занчения , нет, то создать
#             attrs["very_well_field"] = "Some value"
#
#         return super().__new__(mcs, name, base, attrs)
#
# class OurClass(metaclass = MyMetaClass):
#     CLASS_FIELD1 = 101
#     CLASS_FIELD2 = 2
#     def __init__(self):
#         self._value = value
#
# print(OurClass.CLASS_FIELD1)
# print(OurClass.very_well_field)

# # обязуем пользователя созадвать метод move
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
# class Car(Vehicle):
#     def __init__(self, model):
#         self._model = model
# Car("BMW")# будет ошибка т.к. ждет определения метода move


# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
# class Car(Vehicle):
#     def __init__(self, model):
#         self._model = model
#     def move(self):
#         print("Move")
#
# Car("BMW")# теперь все будет ок

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         print("MOVING")
#
# class Car(Vehicle):
#     def __init__(self, model):
#         self._model = model
#     def move(self):
#         super().move()
#         #print("i am moving")
#
# x = Car("BMW")
# x.move()



# # можно и без сего , а так псевдо абстрактный класс
# class Vehicle():
#
#     def move(self):
#         raise NotImplementedError()
#
# class Car(Vehicle):
#     def __init__(self, model):
#         self._model = model
#
# x = Car("BMW")
# x.move()# то будет ошибка при вызове!



# property
class PropertyEx():
    def __init__(self, arg1):
        self._x = arg1

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value > 999:
            raise ValueError()
        else:
            self._x = value

print(PropertyEx.x)
obj = PropertyEx(1)
print(obj.x)
obj.x = 122
print(obj.x)

# # property без декораторов
# class PropertyEx():
#     def __init__(self, arg1):
#         self._x = arg1
#
#     def s_x(self,value):
#         self._x = value
#
#     def g_x(self):
#         return self._x
#
#     x = property(g_x, s_x)
#
#
#
# obj = PropertyEx(11)
# print(obj.x)
# obj.x = 100
# print(obj.x)
#


# class DecoratorsExample:
#     NUM = 0
#     def __init__(self):
#         self._value = 100
#
#     @classmethod
#     def increase_num(cls, num):
#         cls.NUM += num
#
#     @classmethod
#     def get_num(cls):
#         return cls.NUM
#
#     @classmethod# МЕТОДЫ ДЛЯ РАБОТЫ С КЛАССОМ , А ПРОСТЫЕ МЕТОДЫ ДЛЯ РАБОТЫ С ОБЬЕКТОМ
#     def create_one_more(cls):
#         return cls()
#
#     @staticmethod#МЕТОДЫ КОТОРЫЕ ПРОСТО ЕСТЬ
#     def my_func():
#         print("i am static metod")
#
# print(DecoratorsExample.get_num())
# DecoratorsExample.increase_num(100)
# print(DecoratorsExample.get_num())
# z = DecoratorsExample()
# z.get_num()
# print(DecoratorsExample.get_num())

# # Singletone на метаклассах
# class Singletone(type):
#     instance = {}
#
#     def __call__(cls,*args, **kwargs):
#         if cls not  in cls.instance:
#             cls.instance[cls] = super().__call__(*args, **kwargs)
#             return cls.instance[cls]
#         else:
#             raise Exception("already exists")
#
# class MyClass(metaclass=Singletone):
#     def __init__(self):
#         self._x = 100
#
# a = MyClass()
# b = MyClass()# тут уже будет raise Exception("already exists")
