MYSQL_DB_USERNAME = 'root'
MYSQL_DB_PASSWORD = 123
MYSQL_DB_NAME = ''
MYSQL_DB_ADDRESS = ''
MYSQL_DB_PORT = ''

class Config:

    DEBUG = False
    import os
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/signing_db'
    SECRER_KEY = "hello secret  key"
    SESSION_TYPE = 'memcached'
    SECRET_KEY = 'super secret key'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    # connect('test')
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1:3306/ibeacon'
    SECRER_KEY = "hello secret  key"

config = {
    'online': DevelopmentConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}
