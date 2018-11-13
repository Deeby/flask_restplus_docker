import datetime
from .. import db
from mongoengine import *
from .user import User


class Comment(EmbeddedDocument):
    content = StringField(required=True)
    userid = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.now())