from threading import Thread
import time

class MyCronManager():
    """Class for managing tasks in background, which can be performed at predetermined intervals.
    If you do not define a period, it will be set to the default value = 86400 seconds (24 hours)"""
    def __init__(self):
        self._tasks = []

    def add(self, task, task_parameters=None):
        """Function for adding tasks (functions) to be runned"""
        self._tasks.append([task, task_parameters])

    def run(self):
        """Function what run tasks (functions) in background previously added to list by 'add' function"""
        for i in self._tasks:
            if i[1]:
                Thread(target=i[0], args=i[1]).start()
            else:
                Thread(target=i[0]).start()

    def mycronmanager_deco(period=86400):
        """Function-decorator which determines the period of tasks to run"""
        def deco(func):
            def wrap(*args):
                while True:
                    func(*args)
                    time.sleep(period)
            return wrap
        return deco
