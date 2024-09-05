from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import db, Payment, Shipment

payments_bp = Blueprint('payments', __name__)


@payments_bp.route('/', methods=['POST'])
@jwt_required()
def create_payment():
    data = request.get_json()
    shipment = Shipment.query.get_or_404(data['shipment_id'])

    new_payment = Payment(shipment_id=shipment.id, amount=data['amount'])
    db.session.add(new_payment)
    db.session.commit()

    return jsonify({"message": "Payment created successfully"}), 201


@payments_bp.route('/<int:payment_id>', methods=['GET'])
@jwt_required()
def get_payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    return jsonify({
        "id": payment.id,
        "shipment_id": payment.shipment_id,
        "amount": payment.amount,
        "status": payment.status,
        "created_at": payment.created_at
    }), 200

''''Purpose: Handles the payment processing for shipments.
Blueprint: payments_bp groups payment-related routes.
/<int:shipment_id> Route (POST):
Purpose: Processes a payment for a specific shipment.
Functionality: Creates a new payment record associated with the shipment and stores it in the database.'''