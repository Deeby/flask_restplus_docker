import uuid
import datetime

from app.main import db
from app.main.model.article import Article
from app.main.model.serializer import ArticleSchema, ArticleListSchema
import mongoengine


def save_new_article(data):
    try:
        new_article = Article(
            subject=data['subject'],
            content=data['content'],
            userid=data['userid'],
        ).save()

        response_object = {
            'status': 'success',
            'message': 'Article successfully created.'
        }
        return response_object, 201

    except:
        response_object = {
            'status': 'fail',
            'message': 'Article create fail'
        }
        return response_object, 201


def get_all_articles():
    articles = Article.objects.all()
    data, errors = ArticleListSchema(many=True).dump(articles)
    return data


def get_a_article(no):
    article = Article.objects.get(no=no)
    data, errors = ArticleSchema().dump(article)
    return data