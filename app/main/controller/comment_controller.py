from flask import request
from flask_restplus import Resource, Namespace, fields

from ..service.comment_service import save_new_comment, get_all_comments, get_a_comment

api = Namespace('Comment', description='Comment', path='/comment')

# Swagger Parameter
comment_fields = api.model('Comment', {
    'no': fields.Integer,
    'content': fields.String,
    'userid': fields.String,
})

@api.route('/')
class CommentList(Resource):
    @api.doc('list_of_comments')
    def get(self):
        """List all registered comments"""
        return get_all_comments()

    @api.response(201, 'Comment successfully created.')
    @api.doc('create a new comment')
    @api.expect(comment_fields, validate=True)
    def post(self):
        """Creates a new Comment """
        data = request.json
        return save_new_comment(data=data)


@api.route('/<no>')
@api.param('no', 'Article Number')
@api.response(404, 'Comment not found.')
class Comment(Resource):
    @api.doc('get a comment')
    def get(self, no):
        """get a comment given its identifier"""
        comment = get_a_comment(no)
        if not comment:
            api.abort(404)
        else:
            return comment