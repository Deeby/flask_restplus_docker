class Config:
    JWT_SECRET = 'john'
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'project1',
        'host': 'mongodb:27017'
    }


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'project1',
        'host': 'mongodb:27017'
    }
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)