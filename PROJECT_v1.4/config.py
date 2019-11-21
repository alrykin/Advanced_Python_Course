import hashlib
salt = "-s@LTratata-"
TOKEN = "919662946:AAGThahWZrlctw-PxGK1rQW6Sny838-HNaY"
host = "127.0.0.1"
#webhook_url = f'https://advanced-python-cource.tk/{TOKEN[::-1]}'
webhook_url = f'https://35.223.7.73/' + hashlib.md5(TOKEN+salt.encode()).hexdigest()
handle_url = '/' + hashlib.md5(TOKEN+salt.encode()).hexdigest()
