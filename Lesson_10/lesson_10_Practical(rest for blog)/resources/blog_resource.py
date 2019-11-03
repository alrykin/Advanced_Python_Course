import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.blog import Post, Tag, Author
from schemes.blog_schema import PostSchema, AuthorSchema, TagSchema, PostTesttSchema

from flask_restful import Resource, abort
from flask import request, jsonify


class AuthorResource(Resource):
    def get(self, id=None):
        if not id:
            objects = Author.objects()
            return AuthorSchema().dump(objects, many=True)
        obj = Author.objects(id=id).get()
        return AuthorSchema().dump(Author.objects(id=id).get())

    def put(self, id):
        #return jsonify(**request.json)
        obj = Author.objects(id=id).get()
        obj.update(**request.json)
        return AuthorSchema().dump(obj.reload())

    def post(self):
        # return jsonify(**{"metod": "post"})
        validity = AuthorSchema().validate(request.json)
        if validity:
            return validity
        obj = Author(**request.json).save()
        return AuthorSchema().dump(obj)

    def delete(self, id=None):
        # return jsonify(**{"metod": "delete"})
        if not id:
            abort(404, message="You have to specify id !")
        else:
            try:
                object = Author.objects.get(id=id)
                AuthorSchema().dump(Author.objects(id=id).delete())
            except:
                abort(404, message="id does not exist !")
            AuthorSchema().dump(Author.objects(id=id).delete())
            return '', 204



class TagResource(Resource):
    def get(self, id=None):
        if not id:
            objects = Tag.objects()
            return TagSchema().dump(objects, many=True)
        obj = Tag.objects(id=id).get()
        return TagSchema().dump(Tag.objects(id=id).get())

    def put(self, id):
        obj = Tag.objects(id=id).get()
        obj.update(**request.json)
        return TagSchema().dump(obj.reload())

    def post(self):
        validity = TagSchema().validate(request.json)
        if validity:
            return validity
        obj = Tag(**request.json).save()
        return TagSchema().dump(obj)

    def delete(self, id=None):
        if not id:
            abort(404, message="You have to specify id !")
        else:
            try:
                object = Tag.objects.get(id=id)
                TagSchema().dump(Tag.objects(id=id).delete())
            except:
                abort(404, message="id does not exist !")
            TagSchema().dump(Tag.objects(id=id).delete())
            return '', 204



class PostResource(Resource):
    def get(self, id=None):
        if not id:
            objects = Post.objects()
            return PostSchema().dump(objects, many=True)
        obj = Post.objects(id=id).get()
        obj.view_count += 1
        obj.save()
        return PostSchema().dump(Post.objects(id=id).get())

    def put(self, id):
        obj = Post.objects(id=id).get()
        obj.update(**request.json)
        return PostSchema().dump(obj.reload())

    def post(self):
        validity = PostTesttSchema().validate(request.json)
        if validity:
            return validity
        obj = Post(**request.json).save()
        return PostSchema().dump(obj)

    def delete(self, id=None):
        if not id:
            abort(404, message="You have to specify id !")
        else:
            try:
                object = Post.objects.get(id=id)
                PostSchema().dump(Post.objects(id=id).delete())
            except:
                abort(404, message="id does not exist !")
            PostSchema().dump(Post.objects(id=id).delete())
            return '', 204



class AuthorPostsResource(Resource):
    """ Class for get all posts by author last name"""
    def get(self, last_name=None):
        if not last_name:
            return jsonify(**{"error": "You have to specify author last name!"})
        last_name_avaiable = Author.objects().distinct('last_name')
        if last_name not in last_name_avaiable:
            abort(404, message=f"Not found posts with {last_name} last name")
        last_name_obj = Author.objects(last_name=last_name).get()
        posts = Post.objects(author=last_name_obj)
        return PostSchema().dump(posts, many=True)



class Post_by_tag_Resource(Resource):
    """ Class for get all posts by tag name"""
    def get(self, tag=None):
        if not tag:
            return jsonify(**{"error": "You have to specify tag!"})
        tags_avaiable = Tag.objects().distinct('name')
        if tag not in tags_avaiable:
            abort(404, message=f"Not found posts with {tag} tag")
        tag_obj = Tag.objects(name=tag).get()
        posts = Post.objects(tag=tag_obj)
        return PostSchema().dump(posts, many=True)
