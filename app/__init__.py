from flask.app import Flask
from flask_sqlalchemy.extension import SQLAlchemy


application = Flask(__name__)
application.config.from_object("config.Config")


database = SQLAlchemy(application)

from . import models, views

with application.app_context():
    database.create_all()
