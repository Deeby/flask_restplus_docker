import datetime
from .. import db
from mongoengine import *
from .comment import Comment
from .user import User


class Article(Document):
    no = SequenceField()
    subject = StringField(required=True)
    content = StringField(required=True)
    userid = StringField(required=True)
    comments = ListField(EmbeddedDocumentField(Comment))
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())