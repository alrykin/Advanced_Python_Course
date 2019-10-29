import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.workers import Person
from schemes.workers_schema import PersonSchema

from flask_restful import Resource
from flask import request, jsonify

class WorkerResource(Resource):

    def get(self, id=None):
        if not id:
            objects = Person.objects
            return PersonSchema().dump(objects, many=True)
        return PersonSchema().dump(Person.objects(id=id).get())

    def put(self, id):
        obj = Person.objects(id=id).get()
        obj.update(**request.json)
        return PersonSchema().dump(obj.reload())

    def post(self):
        return jsonify(**{'method':'post'})

    def delete(self):
        return jsonify(**{'method':'delete'})
