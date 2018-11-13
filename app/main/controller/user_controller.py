from flask import request
from flask_restplus import Resource, Namespace, fields

from ..service.user_service import save_new_user, get_all_users, get_a_user

api = Namespace('User', description='User', path='v1/user')

# Swagger Parameter
user_fields = api.model('User', {
    'userid': fields.String,
    'userpw': fields.String,
})

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.expect(user_fields, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<no>')
@api.param('no', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    # @api.marshal_with(_user)
    def get(self, no):
        """get a user given its identifier"""
        user = get_a_user(no)
        if not user:
            api.abort(404)
        else:
            return user