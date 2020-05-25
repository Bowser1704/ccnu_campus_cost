from flask_sqlalchemy import SQLAlchemy
from routes import app,db

class Cost(db.Model):
    __tablename__ = 'stu3'
    
    stunum = db.Column(db.String, primary_key=True)
    time = db.Column(db.String, primary_key=True)
    place = db.Column(db.String, primary_key=True)
    restaurant = db.Column(db.String, primary_key=False)
    cost = db.Column(db.Float, default = 0.0, primary_key=False)

