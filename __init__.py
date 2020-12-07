import os
from flask import Flask
from api import api
from models import Base, engine

print(os.getcwd())
try:
    os.mkdir("./resources")
except:
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    api.init_app(app)
    Base.metadata.create_all(engine)
    return app
