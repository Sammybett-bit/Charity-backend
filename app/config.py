import os 

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")

    SQLALCHEMY_TRACK_MODIFICATION =False
    #postgres://sammy:9jKGglIRSeWMrXEu0GlkjcbKPS8gsgzX@dpg-cl1mnbg310os73dfttkg-a.oregon-postgres.render.com/charity_udt5