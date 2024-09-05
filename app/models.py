from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'user' or 'driver'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pickup_location = db.Column(db.String(200), nullable=False)
    delivery_location = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'matched', 'delivered'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey('shipment.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'completed'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

'''
Purpose: This file defines the database schema using SQLAlchemy ORM. Each class represents a table in the database.
User Model: Represents users of the application, who can be either customers (user) or drivers (driver).
Fields: id, username, password, role, created_at.
id: Primary key, unique identifier.
username: The user's login name, must be unique.
password: The hashed password.
role: Defines whether the user is a customer or a driver.
created_at: Timestamp of when the user was created.
Shipment Model: Represents a shipment in the system.
Fields: id, user_id, pickup_location, delivery_location, status, created_at.
user_id: Foreign key linking to the User model, indicating who created the shipment.
pickup_location: Where the shipment is to be picked up.
delivery_location: Where the shipment is to be delivered.
status: The current status of the shipment.
Payment Model: Represents payment records.
Fields: id, shipment_id, amount, status, created_at.
shipment_id: Foreign key linking to the Shipment model, indicating the related shipment.
amount: The amount paid or due for the shipment.
status: Status of the payment, such as 'pending' or 'completed'.

'''