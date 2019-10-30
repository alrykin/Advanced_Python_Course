from flask import  Flask, request, Response
from models.workers import Person
from schemes.workers_schema import PersonSchema
from flask_restful import Api
from resources.store_resource import StoreResource

app = Flask(__name__)
api = Api(app)
api.add_resource(StoreResource, '/workers', '/workers/<string:id>')


if __name__ == "__main__":
    app.run(debug=True)
