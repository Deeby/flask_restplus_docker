import uuid
import datetime

from app.main import db
from app.main.model.article import Article
from app.main.model.comment import Comment
from app.main.model.serializer import CommentSchema, CommentListSchema
import mongoengine


def save_new_comment(data):
    try:
        new_comment = Comment(
            content=data['content'],
            userid=data['userid'],
        )
        article = Article.objects(no=data['no']).get()
        article.comments.append(new_comment)
        article.save()

        response_object = {
            'status': 'success',
            'message': 'Comment successfully created.'
        }
        return response_object, 201

    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Comment create fail'
        }
        return response_object, 201


def get_all_comments():
    comments = Comment.objects.all()
    data, errors = CommentListSchema(many=True).dump(comments)
    return data


def get_a_comment(no):
    comment = Comment.objects.get(no=no)
    data, errors = CommentSchema().dump(comment)
    return data