from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .auth import auth_bp
    from .shipments import shipments_bp
    from .notification import notifications_bp
    from .payments import payments_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(shipments_bp, url_prefix='/shipments')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(payments_bp, url_prefix='/payments')

    return app

"""
Purpose: This file initializes the Flask application and integrates various components such as the database, JWT (for authentication), and migration tools.
db = SQLAlchemy(): Initializes SQLAlchemy, an ORM (Object-Relational Mapping) tool that makes it easy to interact with databases using Python classes.
migrate = Migrate(): Initializes Flask-Migrate, a tool that helps you manage database migrations.
jwt = JWTManager(): Initializes Flask-JWT-Extended, which handles JWT-based authentication.
create_app(): A factory function that creates and configures the Flask application.
Blueprints: The app.register_blueprint() calls register different modules (e.g., authentication, shipments) as blueprints. This modular approach helps in organizing code and makes it easier to maintain.
"""
