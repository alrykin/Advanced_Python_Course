#TODO 4
# 1. Реализовать REST для, категорий, продуктов и текстов

from flask import  Flask, request, Response, jsonify
from models.store import *
from schemes.store_schema import *
from flask_restful import Api
from resources.store_resource import CategoryResource, TextsResource, ProductResource
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "tmp"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

api = Api(app)
api.add_resource(CategoryResource, '/category', '/category/<string:id>')
api.add_resource(TextsResource, '/texts', '/texts/<string:id>')
api.add_resource(ProductResource, '/product', '/product/<string:id>')



@app.route('/file-upload/<id>', methods=['POST'])
def upload_file(id):
    product_ids = [str(i.id) for i in Product.objects()]
    print(product_ids)
    if not id in product_ids:
        resp = jsonify({'message' : 'id wrong or not specified'})
        resp.status_code = 404
        return resp
	# check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = id + "." + file.filename.rsplit('.', 1)[1].lower()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product_photo = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb')
        product_obj = Product.objects.get(id=id)
        if product_obj.photo:
            product_obj.photo.replace(product_photo, content_type = 'image/jpeg')
            product_obj.save()
        else:
            product_obj.photo.put(product_photo, content_type = 'image/jpeg')
            product_obj.save()
        resp = jsonify({'message' : 'File successfully uploaded and aplyed to the product'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp




if __name__ == "__main__":
    app.run(debug=True)
