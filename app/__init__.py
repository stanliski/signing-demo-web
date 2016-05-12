from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()


# mongo_db = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    print config[config_name]
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    mail.init_app(app)

    db.init_app(app)

    from .signing import main as beacon_blueprint
    app.register_blueprint(beacon_blueprint, url_prefix='/signing/api/v1.0')

    return app
