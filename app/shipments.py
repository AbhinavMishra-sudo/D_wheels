from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Shipment, User

shipments_bp = Blueprint('shipments', __name__)


@shipments_bp.route('/', methods=['POST'])
@jwt_required()
def create_shipment():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()

    new_shipment = Shipment(user_id=user.id, pickup_location=data['pickup_location'],
                            delivery_location=data['delivery_location'])
    db.session.add(new_shipment)
    db.session.commit()

    return jsonify({"message": "Shipment request created successfully"}), 201


@shipments_bp.route('/<int:shipment_id>', methods=['GET'])
@jwt_required()
def get_shipment(shipment_id):
    shipment = Shipment.query.get_or_404(shipment_id)
    return jsonify({
        "id": shipment.id,
        "pickup_location": shipment.pickup_location,
        "delivery_location": shipment.delivery_location,
        "status": shipment.status,
        "created_at": shipment.created_at
    }), 200


@shipments_bp.route('/match', methods=['POST'])
@jwt_required()
def match_shipment():
    # Here you would add logic to match shipments with drivers
    return jsonify({"message": "Shipment matched with a driver successfully"}), 200


'''Purpose: This file handles the creation, retrieval, and matching of shipments.
Blueprint: shipments_bp groups shipment-related routes.
/ Route (POST):
Purpose: Creates a new shipment request.
Functionality: Takes the pickup and delivery locations from the user, creates a new shipment record, and stores it in the database.
@jwt_required: This decorator ensures that only authenticated users can access this route.
/<int:shipment_id> Route (GET):
Purpose: Retrieves a specific shipment's details.
Functionality: Looks up the shipment by ID and returns its details.
/match Route (POST):
Purpose: Matches shipments with drivers. This is where you'd implement the logic to find a driver whose route matches the shipment's route.'''