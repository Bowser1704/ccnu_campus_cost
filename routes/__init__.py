from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from routes import config

db = SQLAlchemy(app)

from routes import index, wc, api
