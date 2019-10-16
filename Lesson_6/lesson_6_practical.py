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
my_list_obj.append(100)
print(my_list_obj)
print(my_list_obj.pop(2))
print(my_list_obj)
my_list_obj[0] = 111
print(my_list_obj)
print(my_list_obj[0])
print(my_list_obj.remove(10))
print(my_list_obj)
my_list_obj.clear()
print(my_list_obj)

my_list_obj = MyCustomList((10,20,30,40,50))
my_list_obj_2 = MyCustomList((1,2,3,4,5))

print(my_list_obj + my_list_obj_2)
