# pip install timeloop
# import time
# from datetime import timedelta
# from timeloop import Timeloop

# tl = Timeloop()
#
# @tl.job(interval=timedelta(seconds=2))
# def check():
#     print("test")
#
# tl.start()
#
# while True:
#     pass


#sendChatAction
# send Typing ...

# print(timedelta(hours=12))



## РЕШЕНИЕ !!!#####################
# import time
# import threading
#
# secs = 2
#
# print("111")
#
# def foo():
#     print("Hello")
#     threading.Timer(secs, foo).start()
#
#
# foo()
#
# print("222")
###############################

#### решение 2
import time
from threading import Thread

def some_f(x):
    while True:
        print(x)
        time.sleep(x)

Thread(target=some_f, args=(3,)).start()
