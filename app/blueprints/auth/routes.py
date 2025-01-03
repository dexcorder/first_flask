from flask import Blueprint, request, jsonify, render_template, Response
from app.services.user_service import UserService
from app.blueprints.auth import auth_bp
from app import bcrypt

user_service = UserService()

@auth_bp.route('/register', methods=['GET'])
def register():
    return render_template('auth/register.html')

@auth_bp.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if not email or not password:
        return jsonify({'message': 'All fields are required!'}), 400

    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match!'}), 400

    if user_service.user_exists(email):
        return jsonify({'message': 'Email already registered!'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user_service.add_user(email, hashed_password)

    print(f"User {email} registered with hashed password: {hashed_password}")
    return Response(status=204)
    #return jsonify({'message': 'User registered successfully!'}), 201
