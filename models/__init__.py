from flask_sqlalchemy import SQLAlchemy
from routes import app

db = SQLAlchemy(app)

class Cost(db.Model):
    db.Column(db.Integer, primary_key=True)
