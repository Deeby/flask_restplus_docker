import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.serializer import UsersSchema, UserSchema
import mongoengine


def save_new_user(data):
    try:
        user = User.objects.get(userid=data['userid'])

        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409       

    except mongoengine.DoesNotExist:
        new_user = User(
            userid=data['userid'],
            userpw=data['userpw'],
            created_at=datetime.datetime.now(),
        ).save()

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201


def get_all_users():
    users = User.objects.all()
    data, errors = UsersSchema(many=True).dump(users)
    return data


def get_a_user(no):
    user = User.objects.get(no=no)
    data, errors = UserSchema().dump(user)
    return data