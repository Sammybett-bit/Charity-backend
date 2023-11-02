from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app)
from routes import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':

    app.run(debug=True)