from marshmallow import Schema, fields


class UsersSchema(Schema):
    class Meta:
        fields = ('no', 'userid', 'userpw', 'created_at')


class UserSchema(Schema):
    class Meta:
        fields = ('no', 'userid', 'userpw', 'created_at')


class CommentSchema(Schema):
    content = fields.String()
    userid = fields.String()
    created_at = fields.DateTime()
    

class CommentListSchema(Schema):
    class Meta:
        fields = ('content', 'userid', 'created_at')


class ArticleSchema(Schema):
    no = fields.Integer()
    subject = fields.String()
    content = fields.String()
    userid = fields.String()
    comments = fields.Nested(CommentSchema, many=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class ArticleListSchema(Schema):
    no = fields.Integer()
    subject = fields.String()
    content = fields.String()
    userid = fields.String()
    comments = fields.Nested(CommentSchema, many=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()