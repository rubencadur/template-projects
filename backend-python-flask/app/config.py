from os import getenv

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False

    MYSQL_HOST = getenv("INT_MYSQL_HOST", default="localhost")
    MYSQL_USER = getenv("INT_MYSQL_USER", default='root')
    MYSQL_PASSWORD = getenv("INT_MYSQL_PASSWORD", default='')
    MYSQL_DB = getenv("INT_MYSQL_DB", default='')

    UPLOAD_FOLDER = getenv("INT_UPLOAD_FOLDER")

class DevelopmentConfig(Config):
    DEBUG = True

    HOST = getenv("INT_SERVER_HOST", default="127.0.0.1")
    PORT = getenv("INT_SERVER_PORT", default="5000")
    SERVER_NAME = getenv("INT_SERVER_NAME", default="127.0.0.1:5000")

class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}