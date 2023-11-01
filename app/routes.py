from flask import jsonify, request
from app import app, db
from flask_cors import CORS
from models import User


CORS(app)
@app.route('/')
def home():
    return 'Welcome to the api'
