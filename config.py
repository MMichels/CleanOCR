# CONFIGS FLASK
DEBUG = True
SECRET_KEY = "84ec997c-34e8-11eb-adc1-0242ac120002"
ENV = "development"
HOST = "localhost"
PORT = 5000


# CONFIG DB
SQLALCHEMY_DATABASE_URI = "sqlite:///resources/database.db"
SQL_HOST = "localhost"
SQL_PORT = 3306
SQL_BD = "CleanOCR"


# CONFIG RABBIT
RABBIT_HOST = "localhost"
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