# list_a = [1,2,3]
# list_b = [4,5,6]
#
# new_obj = zip(list_a, list_b)
# print(new_obj)
#
# # print(dict(new_obj))
# print(tuple(new_obj))
#
# # zip врщвращает обьект , который есть итератор
#
# iter_obj = iter(list_b)
# print(iter_obj)
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))


# # создадим свой Iterator
# class SimpleIterator:
#     def __init__(self, start, end, step):
#         self._start = start
#         self._end = end
#         self._step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self._start < self._end:
#             self._start += self._step
#             print(self._start)
#             return self._start
#         raise StopIteration
#
# obj = SimpleIterator(0,100,1)
# iterator_obj = iter(obj)
# next(iterator_obj)
# next(iterator_obj)
# next(iterator_obj)

# теперь можем применять к обьекту for
# class SimpleIterator:
#     def __init__(self, start, end, step):
#         self._start = start
#         self._end = end
#         self._step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self._start < self._end:
#             self._start += self._step
#             return self._start
#         raise StopIteration
#
# obj = SimpleIterator(0,5,1)
# for i in obj:
#     print(i)


####
#### ГЕНЕРАТОРЫ
####
def gen_func(start, end ,step):
    while start < end:
        start +=step
        yield start
    raise StopIteration

obj = gen_func(0,3,1)
print(obj)
iter_obj = iter(obj)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

# # можно выражением , это не лист компрех!!!!!!
# gen_expression = (x**2 for x in range(100))
# print(gen_expression)
# print(next(gen_expression))

# # Убеждаемся что он замораживается до вызова следующей функции next
# def gen_func(start, end ,step):
#     while start < end:
#         print("marker")
#         start +=step
#         yield start
#         yield "i am generator"
#     # raise StopIteration# Можно не рейсить
#
# obj = gen_func(0,2,1)
# print(obj)
# iter_obj = iter(obj)
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# ## создадим свои типы данных , например маcсив
# class Arry:
#
#     TYPES = (int, str, float)
#
#     def __init__(self , size, default_val):
#         self._arry = [default_val] * size
#
#     def __setitem__(self, key, value):
#         if  isinstance(value, Arry.TYPES) and key <= len(self)-1:
#             self._arry[key] = value
#             return None
#         raise ValueError("Out of range")
#
#     def __getitem__(self, item):
#         if  isinstance(item , int) and item <= len(self)-1:
#             return self._arry[item]
#             return
#         raise ValueError("Some error")
#
#     def __str__(self):
#         return str(self._arry)
#
#     def __len__(self):
#         return len(self._arry)
#
# arry = Arry(100,0)
# arry[0] = 12
# arry[99] = 13
# #arry[100] = 13# будет ошибка ибо невыполниться условие
# print(arry[0])
#
# print(arry)
# print(len(arry))


# # а можно унаследоваться от списка...
# class Arry(list):
#
#     TYPES = (int, str, float)
#
#     def __init__(self , size, default_val):
#         elems = [default_val] * size
#         super().__init__(elems)
#
#
# arry = Arry(100,0)
# arry[0] = 12
# arry[99] = 13
# #arry[100] = 13# будет ошибка ибо невыполниться условие
# print(arry[0])
#
# print(arry)
# print(len(arry))
