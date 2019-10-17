## ДОМАШНЯЯ РАБОТА
# 1) Создать консольную программу-парсер, с выводом прогноза погоды. Дать
# возможность пользователю получить прогноз погоды в его локации ( по
# умолчанию) и в выбраной локации, на определенную пользователем дату.
# Можно реализовать, как консольную программу, так и веб страницу.
# Используемые инструменты: requests, beatifulsoup, остальное по желанию.
# На выбор можно спарсить страницу, либо же использовать какой-либо API.

import json
import requests
from datetime import datetime


# my test key, will be removed afrer some period of time
api_key = "38fe51e3bff48ca92ee2a92297354c73"
city_name_id = {"Kyiv":703448, "Kharkiv":706483}


def city_id_by_name(name):
    if name in city_name_id:
        return city_name_id[name]
    url = f"http://api.openweathermap.org/data/2.5/find?q={name}&type=like&APPID={api_key}"
    res = requests.get(url)
    data = res.json()
    if data['list']:
        city_id =  data['list'][0]['id']
    else:
        raise NameError(f"can't find city {name}")
    return city_id


def get_weather(city="Kyiv", period=None):
    """
    Function to get weather information. By default, when calling a function without parameters,
    you will receive the current weather state of Kiev.

    If you want to get weather information for another city - set the name of the city in the first function agrument.
    For example:
    get_weather("London")

    Also, you can define the second parameter - the date for the weather forecast? for example:
    get_weather("London", "2019-10-20")

    """

    city_id = city_id_by_name(city)

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': api_key})
        data = res.json()
        text = "Состояние: " + data['weather'][0]['description'] + "\n"
        text = text + "Температура: " + str(data['main']['temp']) + "\n"
        text = text + "Варьируется от "+ str(data['main']['temp_min']) + " до " + str(data['main']['temp_max']) + "\n"
        text = "\nТекущее состояние погоды для " + city + ":\n" + text
    except Exception as e:
        text = "\nОшибка. Текущее состояние погоды не может быть определено.\n"

    if not period:
        period = register_date = datetime.today().strftime('%Y-%m-%d')

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': api_key})

        data = res.json()

        prognoz = ""

        for i in data['list']:
            if i['dt_txt'][0:10] == period:
                prognoz = prognoz + i['dt_txt'] + " " + '{0:+3.0f}'.format(i['main']['temp']) + " " + i['weather'][0]['description'] + "\n"
            else:
                pass

        if prognoz:
            text = text  + "\nПрогноз погоды\n" + prognoz
        else:
            text = text  + "\nПрогноз погоды не может быть определен. Вам доступен период до +5 суток от текущей даты.\nФормат даты YYYY-MM-DD\n"
    except Exception as e:
        text = text + "Ошибка. Прогноз погоды не может быть определен."

    return text


print(get_weather())
print("#"*80)
print(get_weather( "London",'2019-10-20'))
