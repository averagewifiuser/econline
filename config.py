import os


class BaseConfig(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    FLASK_APP = 'ec-online'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY =  os.getenv('EC_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =  "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECURITY_PASSWORD_SALT =  os.getenv('SECURITY_PASSWORD_SALT')


class TestingConfig(BaseConfig):
    DEBUG = True
    FLASK_ENV = 'testing'
    SECRET_KEY =  'test-secret-key'
    SQLALCHEMY_DATABASE_URI =  "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECURITY_PASSWORD_SALT =  'saltysalt'


class ProductionConfig(BaseConfig):
    DEBUG = False

