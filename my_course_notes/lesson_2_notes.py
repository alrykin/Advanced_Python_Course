# mlist = [1,2,3,4,5]
# dictt = {'a':1,'b':2}
#
# def test(*args, **kwargs):
#     # хороший  метод словаря !!!
#     name = kwargs.get("name", 0)
#     #print(kwargs)
#     print(args)
#     #print(name)
# test(*mlist,**dictt)

# class Cat:
#     CATS_CREATED = 0
#     def __init__(self, name, color):
#         self._name = name
#         self.color = color
#         Cat.CATS_CREATED += 1
#
#     def say_meow(self):
#         print("meow")
#
#     def walk_around(self):
#         print("The cat walks around")
#
#     def eat(self):
#         print("The cat eats")
#
#     def whoami(self):
#         print(f"I'am {self.name}")
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         self._name = name
#
#
# cat = Cat("Alex","black")
# print(Cat.CATS_CREATED)
# cat = Cat("Bob","black")
# print(Cat.CATS_CREATED)

# class GlobalVarExampleClass:
#     GLOBAL_VAR_VALUE = 100
#     def check_access_to_class_var(self):
#         return self.GLOBAL_VAR_VALUE
#     def set_class_var_value(self, var):
#         self.GLOBAL_VAR_VALUE = var
#
# obj = GlobalVarExampleClass()
# print(obj.check_access_to_class_var())
# obj.set_class_var_value(10)
# print(obj.check_access_to_class_var())
#
#print(GlobalVarExampleClass.GLOBAL_VAR_VALUE)

# class Vehicle:
#
#     NUM_OF_DOORS = 4
#     FUEL_TYPE = "Gas"
#
#     def move(self):
#         return("Vehicle drives")
#
#     def add_fuell(self,value):
#         self._fuel += value
#
#     def set_brand(self,brand):
#         self._brand = brand
#
#     def set_engine(self,engine):
#         self._engine = engine
#
#     def get_brand(self):
#         return self._brand
#
#     def get_engine(self):
#         return self._engine
#
#     def __str__(self):
#         return f"Brand is {self._brand} and engine is {self._engine}"
#
# class Car(Vehicle):
#     def __init__(self, brand,  engine):
#         self._brand = brand
#         self._engine = engine
#         self._fuel = 0
#     def move(self):
#         return("move about 100 kmph")
#
#
# car = Car("bmw","v8")
#
# print(car)



# пример ограничения добавления
class Example:

    __slots__ = ("_name")

    def __init__(self,name):
        self._name = name

    def some_fuu(self):
        print("tessssssssssssssssssssstr")
qqq = Example("teeeeest")
qqq._name = "asdfadsfad"
#qqq._my_cool_var = 10
