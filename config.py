import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///d_wheels.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-string')


'''
Purpose: This file holds the configuration settings for your Flask application.
SECRET_KEY: A secret key used by Flask to manage sessions and tokens. It's essential for security.
SQLALCHEMY_DATABASE_URI: The URI of the database. In this case, it's set to use SQLite by default, but you can change it to any other database like PostgreSQL or MySQL.
SQLALCHEMY_TRACK_MODIFICATIONS: Disables the SQLAlchemy feature that tracks modifications of objects and emits signals. It's generally set to False to save resources.
JWT_SECRET_KEY: A secret key used by Flask-JWT-Extended to create JSON Web Tokens (JWT) for secure authentication 
'''