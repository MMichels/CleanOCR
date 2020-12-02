from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_session():
    global db
    session = db.create_scoped_session()
    return session
