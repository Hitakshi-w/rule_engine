from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)

    with app.app_context():
        from . import routes, models  # Ensure models are imported
        db.create_all()
        print("Database initialized")

    return app