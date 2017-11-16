
class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user@localhost/foo'  # just sample uri. change it later


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE = 'tenhash.db'
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'default'


class TestingConfig(Config):
    TESTING = True
