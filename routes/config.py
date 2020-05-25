import  os
import  sys

from routes import  app


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CAMPUS_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('CAMPUS_TRACK_MODIFICATIONS')