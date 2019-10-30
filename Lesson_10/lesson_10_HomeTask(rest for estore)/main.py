# 1) Реализовать REST интернет магазина. Модель товар (цена,
# доступность, кол-во доступных единиц, категория, кол-во просмотров),
# Категория (описание, название). При обращении к конкретному товару
# увеличивать кол-во просмотров на 1. Добавить модуль для заполнения
# БД валидными данными. Реализовать подкатегории ( доп. Бал). Добавить
# роут, который выводят общую стоимость товаров в магазине.

from flask import  Flask, request, Response
from models.store import *
from schemes.store_schema import *
from flask_restful import Api
from resources.store_resource import StoreResource, StoreTotalCostResource

app = Flask(__name__)
api = Api(app)
api.add_resource(StoreResource, '/store', '/store/<string:id>')
api.add_resource(StoreTotalCostResource, '/total_cost')

if __name__ == "__main__":
    app.run(debug=True)
