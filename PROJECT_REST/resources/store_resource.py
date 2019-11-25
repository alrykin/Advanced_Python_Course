#TODO 4
# 1. Реализовать REST для, категорий, продуктов и текстов
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.store import Category, Product, Texts
from schemes.store_schema import CategorySchema, ProductSchema, TextsSchema
from flask_restful import Resource, abort
from flask import request, jsonify

class TextsResource(Resource):
    def get(self, id=None):
        if not id:
            objects = Texts.objects()
            return TextsSchema().dump(objects, many=True)
        obj = Texts.objects(id=id).get()
        return TextsSchema().dump(Texts.objects(id=id).get())

    def post(self):
        validity = TextsSchema().validate(request.json)
        if validity:
            return validity
        obj = Texts(**request.json)
        obj.save()
        return TextsSchema().dump(obj)

    def put(self, id):
        validity = TextsSchema().validate(request.json)
        if validity:
            return validity
        obj = Texts.objects(id=id).get()
        obj.update(**request.json)
        return TextsSchema().dump(obj.reload())

    def delete(self, id=None):
        if not id:
            abort(404, message="You have to specify id !")
        else:
            try:
                object = Texts.objects.get(id=id)
                TextsSchema().dump(Texts.objects(id=id).delete())
            except:
                abort(404, message="id does not exist !")
            TextsSchema().dump(Texts.objects(id=id).delete())
            return '', 204



class CategoryResource(Resource):
    def get(self, id=None):
        if not id:
            objects = Category.objects()
            return CategorySchema().dump(objects, many=True)
        obj = Category.objects(id=id).get()
        return CategorySchema().dump(Category.objects(id=id).get())

    def post(self):
        validity = CategorySchema().validate(request.json)
        if validity:
            return validity
        obj = Category(**request.json)
        obj.save()
        if obj.parent:
            parebnt_obj = obj.parent
            parebnt_obj.subcategory.append(obj)
            parebnt_obj.save()
        return CategorySchema().dump(obj)

    def delete(self, id=None):
        if not id:
            abort(404, message="You have to specify id !")
        else:
            try:
                object = Category.objects.get(id=id)
                CategorySchema().dump(Category.objects(id=id).delete())
            except:
                abort(404, message="id does not exist !")
            CategorySchema().dump(Category.objects(id=id).delete())
            return '', 204

    def put(self, id):
        validity = CategorySchema().validate(request.json)
        if validity:
            return validity
        obj = Category.objects(id=id).get()
        obj.update(**request.json)
        return CategorySchema().dump(obj.reload())



class ProductResource(Resource):
    def get(self, id=None):
        if not id:
            objects = Product.objects()
            return ProductSchema().dump(objects, many=True)
        obj = Product.objects(id=id).get()
        return ProductSchema().dump(Product.objects(id=id).get())

    def post(self):
        validity = ProductSchema().validate(request.json)
        if validity:
            return validity
        obj = Product(**request.json)
        obj.save()
        product_photo = open('tmp/no_image.jpg', 'rb')
        obj.photo.put(product_photo, content_type = 'default_image/jpeg')
        obj.save()
        return ProductSchema().dump(obj)

    def delete(self, id=None):
        if not id:
            abort(404, message="You have to specify id !")
        else:
            try:
                object = Product.objects.get(id=id)
                ProductSchema().dump(Product.objects(id=id).delete())
            except:
                abort(404, message="id does not exist !")
            ProductSchema().dump(Product.objects(id=id).delete())
            return '', 204

    def put(self, id):
        validity = ProductSchema().validate(request.json)
        if validity:
            return validity
        if request.json["category"]:
            request.json["category"] = Category.objects.get(id=request.json["category"])
        obj = Product.objects(id=id).get()
        obj.update(**request.json)
        return ProductSchema().dump(obj.reload())
