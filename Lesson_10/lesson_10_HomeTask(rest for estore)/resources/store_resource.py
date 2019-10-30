import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.store import Item, ItemCategory, SubCategory
from schemes.store_schema import ItemSchema, ItemCategorySchema, SubCategorySchema
from flask_restful import Resource, abort
from flask import request, jsonify

class StoreTotalCostResource(Resource):
    def get(self):
        cost_and_count = Item.objects.only('price', 'intems_count')
        total_cost = 0
        for i in cost_and_count:
            total_cost = total_cost + i.price * i.intems_count
        return jsonify(**{"total_cost": total_cost})

class StoreResource(Resource):
    def get(self, id=None):
        # return jsonify(**{"metod": "post"})
        if not id:
            objects = Item.objects()
            return ItemSchema().dump(objects, many=True)
        obj = Item.objects(id=id).get()
        obj.view_count += 1
        obj.save()
        return ItemSchema().dump(Item.objects(id=id).get())

    def put(self, id):
        #return jsonify(**{"metod": "put"})
        obj = Item.objects(id=id).get()
        obj.update(**request.json)
        print(obj)
        return ItemSchema().dump(obj.reload())

    def post(self):
        # return jsonify(**{"metod": "post"})
        validity = ItemSchema().validate(request.json)
        if validity:
            return validity
        obj = Item(**request.json).save()
        return ItemSchema().dump(obj)

    def delete(self, id=None):
        # return jsonify(**{"metod": "delete"})
        if not id:
            abort(404, message="You have to specify id !")
        else:
            try:
                object = Item.objects.get(id=id)
                ItemSchema().dump(Item.objects(id=id).delete())
            except:
                abort(404, message="id does not exist !")
            ItemSchema().dump(Item.objects(id=id).delete())
            return '', 204
