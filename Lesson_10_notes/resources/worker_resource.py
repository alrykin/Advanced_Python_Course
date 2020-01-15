import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.workers import Person
from schemes.workers_schema import PersonSchema

from flask_restful import Resource, abort
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
        validity = PersonSchema().validate(request.json)
        if validity:
            return validity
        obj = Person(**request.json).save()
        return PersonSchema().dump(obj)

    def delete(self, id=None):
        if not id:
            abort(404, message="You have to specify id !")
        else:
            try:
                object = Person.objects.get(id=id)
                PersonSchema().dump(Person.objects(id=id).delete())
            except:
                abort(404, message="Specifyed id does not exist !")
            PersonSchema().dump(Person.objects(id=id).delete())
            return '', 204
