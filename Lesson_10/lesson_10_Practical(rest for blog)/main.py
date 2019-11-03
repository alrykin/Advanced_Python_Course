from flask import  Flask
from flask_restful import Api
from resources.blog_resource import PostResource, TagResource, AuthorResource, Post_by_tag_Resource, AuthorPostsResource

app = Flask(__name__)
api = Api(app)
# route to CRUD posts records
api.add_resource(PostResource, '/post', '/post/<string:id>')
# route to CRUD author records
api.add_resource(AuthorResource, '/author', '/author/<string:id>')
# route to CRUD tag records
api.add_resource(TagResource, '/tag', '/tag/<string:id>')
# route to get all posts with specific tag
api.add_resource(Post_by_tag_Resource, '/tag/posts/<string:tag>')
# route to get all posts with specific Author last name
api.add_resource(AuthorPostsResource, '/author/posts/<string:last_name>')

if __name__ == "__main__":
    app.run(debug=True)
