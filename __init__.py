import os
from flask import Flask
from api import api
from models import db

try:
    os.mkdir("./resources")
except:
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    api.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
