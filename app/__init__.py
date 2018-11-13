from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.article_controller import api as article_ns
from .main.controller.comment_controller import api as comment_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Appeal API v1',
          version='1.0',
          description='Appeal API v1'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(article_ns, path='/article')
api.add_namespace(comment_ns, path='/comment')