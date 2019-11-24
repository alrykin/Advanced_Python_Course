#TODO 4
# 1. Реализовать REST для, категорий, продуктов и текстов

from flask import  Flask, request, Response
from models.store import *
from schemes.store_schema import *
from flask_restful import Api
from resources.store_resource import StoreResource

app = Flask(__name__)
api = Api(app)
api.add_resource(StoreResource, '/store', '/store/<string:id>')
api.add_resource(StoreTotalCostResource, '/total_cost')

if __name__ == "__main__":
    app.run(debug=True)
