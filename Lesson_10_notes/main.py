from flask import  Flask, request, Response
from models.workers import Person
from schemes.workers_schema import PersonSchema
from flask_restful import Api
from resources.worker_resource import WorkerResource

app = Flask(__name__)
api = Api(app)
api.add_resource(WorkerResource, '/workers', '/workers/<string:id>')


## Делали
# @app.route("/", methods = ["GET","POST"])
# def home():
#     if request.method == "GET":
#         obj = Person.objects.get()
#         return PersonSchema().dump(obj)
#     else:
#         validity = PersonSchema().validate(request.json)
#         if validity:
#             return validity
#         Person(**request.json).save()
#         return Response(status=201)



if __name__ == "__main__":
    app.run(debug=True)
