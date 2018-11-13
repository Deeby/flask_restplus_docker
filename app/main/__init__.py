from flask import Flask
from flask_mongoengine import MongoEngine
from .config import config_by_name

db = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    return app