from flask import jsonify, request
from app import app, db
from flask_cors import CORS
from models import User, Donation


CORS(app)
@app.route('/')
def home():
    return 'Welcome to the api'

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()

    # Ensure required data is provided
    if 'username' not in user_data or 'email' not in user_data or 'password' not in user_data:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    # Check if the user already exists
    existing_user = User.query.filter_by(email=user_data['email']).first()
    if existing_user:
        return jsonify({'message': 'User with this email already exists'}), 400

    new_user = User(
        username=user_data['username'],
        email=user_data['email'],
        password=user_data['password'],
        phonenumber=user_data.get('phonenumber')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201

@app.route('/donations', methods=['POST'])
def create_donation():
    donation_data = request.get_json()

    # Ensure required data is provided
    if 'user_id' not in donation_data or 'amount' not in donation_data:
        return jsonify({'message': 'User ID and donation amount are required'}), 400

    # Check if the user exists
    user = User.query.get(donation_data['user_id'])
    if not user:
        return jsonify({'message': 'User not found'}), 404

    new_donation = Donation(
        user_id=donation_data['user_id'],
        amount=donation_data['amount']
    )

    db.session.add(new_donation)
    db.session.commit()

    return jsonify({'message': 'Donation created successfully', 'donation_id': new_donation.id}), 201

@app.route('/donations/<user_id>', methods=['GET'])
def get_user_donations(user_id):
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404

    donations = Donation.query.filter_by(user_id=user.id).all()
    donation_details = [{'id': donation.id, 'amount': donation.amount, 'created_at': donation.created_at} for donation in donations]

    return jsonify({'user_id': user.id, 'donations': donation_details}), 200


if __name__=='__main__':
    app.run(debug=True) 