#############################################################
# 1) Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.
#############################################################
from threading import Thread
import time

def thr_decorator(is_daemon=False, name=None):
    def actual_decorator(func):
        def wrapper(var1):
            t = Thread(target=func, args=(var1,), name=name, daemon=is_daemon)
            t.start()
        return wrapper
    return actual_decorator

# @thr_decorator(False)
# def some_func(var1):
#     for i in range(var1):
#           print(i)
#           time.sleep(0.2)
#
# some_func(3)
# some_func(5)
# some_func(10)

#############################################################
# 2) Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё созданный декоратор. Создать список из 10
# ссылок, по которым будет происходить скачивание. Создать список
# потоков, отдельный поток, на каждую из ссылок. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.
#############################################################
import urllib.request

@thr_decorator(False)
def downloader(url):
    print("="*50 + f'\nBeginning file download for url:\n{url}\n' + "="*50 + '\n')
    name = url.split('/').pop()
    urllib.request.urlretrieve(url, name)
    print("="*50 + f'\nFile was successfully downloaded for url:\n{url}\n' + "="*50 + '\n')


list_of_urls = ['https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.2.32-summary.txt',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-11.0.0-rc1.tar.gz',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.2.39-summary.txt',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/ChangeLog-12.0.0',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.4.26-summary.txt',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.4.27-summary.txt',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.4.29-summary.txt',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.4.39.1-summary.txt',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.4.39.2-summary.txt',
                'https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-1.4.43-summary.txt']


for i in list_of_urls:
    downloader(i)


#############################################################
## 3) Написать свой контекстный менеджер для работы с файлами.
#############################################################
class MyFileClass:

    def __init__(self, file, rights):
        self._file = open(file, rights)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def write(self, text):
        self._file.write(text)

with MyFileClass('text.txt', 'w') as new_obj:
    new_obj.write("some text...")
