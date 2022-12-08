from config import SQLALCHEMY_DATABASE_URI

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app, database_path=SQLALCHEMY_DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push()
    db.app = app
    db.init_app(app)
    db.create_all()
