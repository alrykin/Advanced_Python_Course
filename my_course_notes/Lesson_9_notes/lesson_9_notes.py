import json

dict_to_json = {
    "date_last" : ['data1', 'data2', 'data3'],
    "simple_data_int": 1,
    "simple_data_string": "one",
    "embeded_dict" : {
    'one': 1,
    'two': 2
    }
}


print(type(dict_to_json))
json_dict = json.dumps(dict_to_json, indent=2)#теперь это строка. indent добавить отступы для выводы
print(type(json_dict))#теперь это строка
print(json_dict)


# пример преобр с json в python object
new_obj = '{"data1":1}'# as json object
python_object = json.loads(new_obj)
print(type(python_object))
