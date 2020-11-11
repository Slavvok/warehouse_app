import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_restful_swagger import swagger


class Config:
    DEBUG = True
    SECRET_KEY = 'dsasdfdfadfadsfa'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///main.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = datetime.timedelta(minutes=30)


class TestConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_db.db'
    TESTING = True


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = swagger.docs(Api(app), apiVersion='0.1')
# api = Api(app)
migrate = Migrate(app, db)


def create_app(conf=TestConfig):
    """Function for testing"""
    app = Flask(__name__)
    app.config.from_object(conf)
    db.init_app(app)
    return app


from app import models