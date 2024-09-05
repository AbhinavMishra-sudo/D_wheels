from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password, role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    return jsonify(access_token=access_token), 200

'''Purpose: This file handles user authentication, including registration and login.
Blueprint: auth_bp is a Flask blueprint that groups authentication-related routes.
/register Route:
Purpose: Registers a new user.
Functionality: Receives user data (username, password, role), hashes the password, and stores the user in the database.
/login Route:
Purpose: Authenticates a user.
Functionality: Receives login data, verifies the password, and returns a JWT access token if successful.
JWT: JSON Web Tokens are used for secure user authentication. The token is returned to the client, which can use it for accessing protected resources'''