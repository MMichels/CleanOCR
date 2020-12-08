# CONFIGS FLASK
import os

DEBUG = True
SECRET_KEY = "84ec997c-34e8-11eb-adc1-0242ac120002"
ENV = "development"
HOST = "localhost"
PORT = 5000

# CONFIG DB
SQLALCHEMY_DATABASE_URI = "sqlite:///resources/database.db"

# CONFIG RABBIT
RABBIT_HOST = "host.docker.internal" if os.getenv("HOST") == "docker" else "localhost"
RABBIT_PORT = 5672
RABBIT_USER = "guest"
RABBIT_PASS = "guest"

RABBIT_QUEUES = {
    "IMG.Clean": {
        "exchange": "IMG",
        "queue": "clean",
        "routing_key": "IMG.Clean"
    }
}
