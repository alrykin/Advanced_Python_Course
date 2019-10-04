## Practice
# Создать декоратор с аргументами. Который будет вызывать функцию, определенное кол-во раз,
# будет выводить кол-во времени затраченного на выполнение данной функции и её название. Practice.


import time

def decorator(num_of_repeats=1):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(num_of_repeats):
                start_time = time.time()
                func()
                func_time = time.time() - start_time
                result = "function name is: " + func.__name__ + " time for its extcution = " + str(func_time)
                results.append(result)
            print("decoration finished")
            return (results)
        return wrapper
    return actual_decorator

@decorator(5)
def some_func():
    time.sleep(1)


print(some_func())
