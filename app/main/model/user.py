import datetime
from .. import db
from mongoengine import *


class User(Document):
    no = SequenceField()
    userid = StringField(unique=True, required=True)
    userpw = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.now())

    def __repr__(self):
        return "<User '{}'>".format(self.userid)