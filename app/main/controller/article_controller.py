from flask import request
from flask_restplus import Resource, Namespace, fields

from ..service.article_service import save_new_article, get_all_articles, get_a_article

api = Namespace('Article', description='Article', path='/article')

# Swagger Parameter
article_fields = api.model('Article', {
    'subject': fields.String,
    'content': fields.String,
    'userid': fields.String,
})

@api.route('/')
class ArticleList(Resource):
    @api.doc('list_of_articles')
    def get(self):
        """List all registered articles"""
        return get_all_articles()

    @api.response(201, 'Article successfully created.')
    @api.doc('create a new article')
    @api.expect(article_fields, validate=True)
    def post(self):
        """Creates a new Article """
        data = request.json
        return save_new_article(data=data)


@api.route('/<no>')
@api.param('no', 'Article Number')
@api.response(404, 'Article not found.')
class Article(Resource):
    @api.doc('get a article')
    def get(self, no):
        """get a article given its identifier"""
        article = get_a_article(no)
        if not article:
            api.abort(404)
        else:
            return article