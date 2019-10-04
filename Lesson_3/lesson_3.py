## Practice
# Создать декоратор с аргументами. Который будет вызывать функцию, определенное кол-во раз,
# будет выводить кол-во времени затраченного на выполнение данной функции и её название. Practice.


import time

def decorator(num_of_repeats=1):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            results_in_dict = {}
            for i in range(num_of_repeats):
                results_in_dict[f"result for iteration {i}"] = {}
                start_time = time.time()
                func()
                func_time = time.time() - start_time
                result = "function name is: " + func.__name__ + ". Time for its extcution = " + str(func_time)
                results_in_dict[f"result for iteration {i}"]["function name"] = func.__name__
                results_in_dict[f"result for iteration {i}"]["time for its extcution: "] = str(func_time)
            print("decoration finished")
            return results_in_dict
        return wrapper
    return actual_decorator

@decorator(5)
def some_func():
    # some logic
    time.sleep(0.2)


print(some_func())




##Home Work
# Создать класс структуры данных Стек, Очередь.
# Создать класс комплексного числа и реализовать для него арифметические операции.
