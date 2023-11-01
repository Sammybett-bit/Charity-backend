
from sqlalchemy.orm import validates
from datetime import datetime
from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phonenumber = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    @validates('username')
    def validate_username(self, key, username):
        if len(username) < 5:
            raise ValueError('Username must be at least 5 characters')
        return username

@validates('email')
def validate_email(self, key, email):
    if '@' not in email:
        raise ValueError('Invalid email format. Must contain "@"')
    return email

@validates('password')
def validate_password(self, key, password):
    if not any(char.isdigit() for char in password):
        raise ValueError('Password must contain at least one digit')
    if not any(char.isupper() for char in password):
        raise ValueError('Password must contain at least one uppercase letter')
    if not any(char.islower() for char in password):
        raise ValueError('Password must contain at least one lowercase letter')
    return password

@validates('phonenumber')
def validate_phonenumber(self, key, phonenumber):
    if not str(phonenumber).isdigit() or len(str(phonenumber)) != 10:
        raise ValueError('Phone number must be exactly 10 digits')
    return phonenumber