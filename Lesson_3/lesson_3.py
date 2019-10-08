## Practice
# Создать декоратор с аргументами. Который будет вызывать функцию, определенное кол-во раз,
# будет выводить кол-во времени затраченного на выполнение данной функции и её название. Practice.

# import time
#
# def decorator(num_of_repeats=1):
#     def actual_decorator(func):
#         def wrapper(*args, **kwargs):
#             results_in_dict = {}
#             for i in range(num_of_repeats):
#                 results_in_dict[f"result for iteration {i}"] = {}
#                 start_time = time.time()
#                 func_results = func()
#                 func_time = time.time() - start_time
#                 result = "function name is: " + func.__name__ + ". Time for its extcution = " + str(func_time)
#                 results_in_dict[f"result for iteration {i}"]["function name"] = func.__name__
#                 results_in_dict[f"result for iteration {i}"]["time for its extcution: "] = str(func_time)
#                 results_in_dict[f"result for iteration {i}"]["result of  function extcution: "] = func_results
#             print("decoration finished")
#             return results_in_dict
#         return wrapper
#     return actual_decorator
#
# @decorator(5)
# def some_func():
#     time.sleep(0.2)
#     return "VALUE"
#
# print(some_func())
#
#
#
#
# # #Home Work
# # Создать класс структуры данных Стек, Очередь.
# # Создать класс комплексного числа и реализовать для него арифметические операции.
# # ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: предусмотреть pop при пустом стеке,  ограничить размер стека
# class MyStack():
#
#     def __init__(self):
#         self._STACK_LIST = []
#
#     def push(self, var):
#         if len(self._STACK_LIST) > 100:
#             raise Exception("The stack is full")
#         else:
#             self._STACK_LIST.append(var)
#
#     def get_stack(self):
#         return self._STACK_LIST
#
#     def pop(self):
#         if self._STACK_LIST:
#             return self._STACK_LIST.pop()
#         else:
#             raise Exception("The stack is empty")
#
# stack_test = MyStack()
# stack_test.push(1)
# stack_test.push(2)
# stack_test.push(3)
# print(stack_test.pop())
#
#
#
#
# class MyQueue():
#
#     def __init__(self):
#         self._QUEUE_LIST  = []
#
#     def enqueue(self, var):
#         if len(self._QUEUE_LIST) > 100:
#              raise Exception("The Queue is full")
#         self._QUEUE_LIST.insert(0, var)
#
#     def dequeue(self):
#         if self._QUEUE_LIST:
#             return self._QUEUE_LIST.pop()
#         else:
#             raise Exception("The Queue is empty")
#
#
# some_queue = MyQueue()
# some_queue.enqueue(1)
# some_queue.enqueue(2)
# some_queue.enqueue(3)
# print(some_queue.dequeue())
#
#



class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        if self.real == 0 and self.imag == 0:
            return str(0)
        elif self.real == 0 and self.imag != 0:
            return str(self.imag)+"i"
        elif self.imag == 0:
            return str(self.real)
        else:
            return f'{self.real}{sign}{self.imag}i'

    def __add__(self,other):
        z_real = self.real+other.real
        z_imag = self.imag+other.imag
        return Complex(z_real, z_imag)


    def __sub__(self,other):
        z_real = self.real-other.real
        z_imag = self.imag-other.imag
        return Complex(z_real, z_imag)


    def __mul__(self,other):
        z1 = (self.real*other.real)
        z2 = (self.real*other.imag)
        z3 = (self.imag*other.real)
        z4 = (self.imag*other.imag)*-1
        z_real = z4 + z1
        z_imag = z2 + z3
        z_imag = z2 - z3*-1
        return Complex(z_real, z_imag)


    def __truediv__(self, other):
        other_sopr = Complex(other.real , other.imag*-1)
        divisor = self * other_sopr
        divided = (other.real * other.real) + (other.imag * other.imag)
        return Complex(divisor.real/divided, divisor.imag/divided)


x = Complex(2,5)
y = Complex(4,-1)
print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
