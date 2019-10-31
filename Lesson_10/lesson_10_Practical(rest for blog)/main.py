from flask import  Flask#, request, Response
# from models.blog import Author, Tag, Post
# from schemes.blog_schema import AuthorSchema, TagSchema, PostSchema
from flask_restful import Api
from resources.blog_resource import PostResource, AuthorResource, Post_by_tag_Resource

app = Flask(__name__)
api = Api(app)
api.add_resource(PostResource, '/post', '/post/<string:id>')
api.add_resource(Post_by_tag_Resource, '/tag', '/tag/<string:tag>')
api.add_resource(AuthorResource, '/author', '/author/<string:last_name>')

if __name__ == "__main__":
    app.run(debug=True)
