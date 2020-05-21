from scasBackend.models import db
import os
import logging

# Configs

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    # sqlite :memory: identifier is the default if no filepath is present
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '123'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'scasBackend.log'
    LOGGING_LEVEL = logging.DEBUG
    SECURITY_CONFIRMABLE = False
    SUPPORTED_LANGUAGES = {'en': 'English'}

# Development
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///scasBackend.sqlite3'
    SECRET_KEY = '456'

# Testing
class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://scasBackend.sqlite3'
    SECRET_KEY = '789'

config = {
    "development": "scasBackend.config.DevelopmentConfig",
    "testing": "scasBackend.config.TestingConfig",
    "default": "scasBackend.config.DevelopmentConfig"
}

def configure_app(app):
    # Configure above configuraton
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True) # if it exists (for production)
    
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)