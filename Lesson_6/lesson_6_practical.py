# 1) Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop, append, insert, remove, clear. Перегрузить
# операцию сложения для списков, которая возвращает новый расширенный
# объект.

class MyList:

    def __init__(self, *args):
        self._list = list(*args)

    def __str__(self):
        return str(self._list)

    # def __setitem__(self, position, value):
    #     self._list[position] = value

    #
    # def __getitem__(self, index):
    #     if  isinstance(index , int) and item <= len(self)-1:
    #         return self._list[index]
    #     raise IndexError("index out if range")

    def __len__(self):
        return len(self._list)

    def append(self, value):
        self._list = self._list + [value]
        return

    def clear(self):
        self._list = []

    def pop(self, index=-1):
        value_to_return = self._list[index]
        if index == -1:
            self._list = self._list[0:-1]
            return value_to_return
        elif index > len(self._list) - 1:
            raise IndexError("ho-ho, your  index out of range")
        else:
            new_list = []
            for i in self._list:
                if self._list.index(i) == index:
                    pass
                else:
                    new_list.append(i)
            self._list = new_list
            return value_to_return


my_list_obj = MyList((1,2,3,4,5))

# print(my_list_obj)
# my_list_obj.append(100)
print(my_list_obj)
print(my_list_obj.pop(4))
print(my_list_obj)
my_list_obj.clear()
print(my_list_obj)
