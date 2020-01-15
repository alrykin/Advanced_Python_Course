
from threading import Thread
import time

# пример  декоратора двойной глубины
def CronManager(period=86400):
    import time
    def deco(func):
        def wrap(*args):
            while True:
                func(*args)
                time.sleep(period)
            print("stop wrapping")
        return wrap
    return deco






class MyCronManager():
    def __init__(self):
        self._tasks = []

    def add(self, task, task_parameters=None):
        self._tasks.append([task, task_parameters])

    def to_run(self):
        for i in self._tasks:
            if i[1]:
                Thread(target=i[0], args=i[1]).start()
            else:
                Thread(target=i[0]).start()

    def mycronmanager_deco(period=86400):
        def deco(func):
            def wrap(*args):
                while True:
                    func(*args)
                    time.sleep(period)
                print("stop wrapping")
            return wrap
        return deco


cm = MyCronManager()
@MyCronManager.mycronmanager_deco(3)
def some():
    print(f"Hello some")

@MyCronManager.mycronmanager_deco(1)
def foo(var):
    print(f"Goodbye {var}")

cm.add(some)
cm.add(foo, ("fooo", ))
cm.to_run()
