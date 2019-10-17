# 1) Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop, append, insert, remove, clear. Перегрузить
# операцию сложения для списков, которая возвращает новый расширенный
# объект.

class MyCustomList:

    def __init__(self, *args):
        self._list = list(*args)

    def __str__(self):
        return str(self._list)

    def __setitem__(self, index, value):
        self.insert(index, value)

    def __getitem__(self, index):
        if  isinstance(index , int) and index <= len(self)-1:
            return self._list[index]
        raise IndexError("index out if range")

    def __len__(self):
        value = 0
        for i in self._list:
            value += 1
        return value

    def append(self, value):
        self._list = self._list + [value]

    def remove(self, value):
        if value not in  self._list:
            raise ValueError(f"ho-ho, {value} not in mycustomlist")
        else:
            for i in self._list:
                if i == value:
                    index = self._list.index(i)
                    del self._list[index]
                    break

    def insert(self, index, value):
        if index == 0:
            self._list = [value] + self._list
        elif index > len(self._list)-1 or -index < -len(self._list)-1:
            raise IndexError("ho-ho, your  index out of range")
        elif index == len(self._list) - 1:
            self._list = self._list + [value]
        else:
            self._list = self._list[:index] + [value] + self._list[index:]

    def clear(self):
        self._list = []

    def pop(self, index=-1):
        if index == -1:
            value_to_return = self._list[-1]
            self._list = self._list[0:-1]
            return value_to_return
        elif index > len(self._list)-1 or -index < -len(self._list)-1:
            raise IndexError("ho-ho, your  index out of range")
        else:
            value_to_return = self._list[index]
            del self._list[index]
            return value_to_return

    def __add__(self, other):
        return self._list + other._list
        # # если задачей подразумевалось не использовать конструкцию выше, то можно, к примету так:
        # new_list = []
        # for i in self._list:
        #     new_list.append(i)
        # for i in other._list:
        #     new_list.append(i)
        # return new_list



my_list_obj = MyCustomList((10,20,30,40,50))
# append
my_list_obj.append(100)
print(my_list_obj)
# pop
print(my_list_obj.pop(2))
print(my_list_obj)
# insert
my_list_obj[0] = 111
print(my_list_obj)
print(my_list_obj[0])
# remove
print(my_list_obj.remove(10))
print(my_list_obj)
# clear
my_list_obj.clear()
print(my_list_obj)

my_list_obj = MyCustomList((10,20,30,40,50))
my_list_obj_2 = MyCustomList((1,2,3,4,5))
# __add__
print(my_list_obj + my_list_obj_2)





# 2) Создать свою структуру данных Словарь, которая поддерживает методы, get, items, keys, values.
# Так же перегрузить операцию сложения для словарей, которая возвращает новый расширенный объект.


class MyCustomDict:
    def __init__(self, **kwargs):
        self._dict = kwargs

    def __str__(self):
        return str(self._dict)

    def __getitem__(self, key):
        if key not in self._dict:
            raise KeyError(f"ho-ho, there is no {key} in mycustomdict")
        else:
            return self._dict[key]

    def items(self):
        return_list = []
        for i in self._dict:
            return_list.append((i, self._dict[i]))
        return return_list

    def keys(self):
        return_list = []
        for i in self._dict:
            return_list.append(i)
        return return_list

    def values(self):
        return_list = []
        for i in self._dict:
            return_list.append(self._dict[i])
        return return_list

    def __add__(self, other):
        for i in self._dict:
            if i in other._dict:
                raise KeyError("Ho-ho. Keys from 'left' odject intersect with keys from 'right' odject")
        dict_to_return = self._dict
        for i in other._dict:
            dict_to_return[i] = other._dict[i]
        return dict_to_return



my_dict_obj = MyCustomDict(a=1,b=2,c=3)
print(my_dict_obj)
#get
print(my_dict_obj['c'])
#items
print(my_dict_obj.items())
#keys
print(my_dict_obj.keys())
#values
print(my_dict_obj.values())
# __add__
my_dict_obj2 = MyCustomDict(g=4,f=5)
print(my_dict_obj + my_dict_obj2)
