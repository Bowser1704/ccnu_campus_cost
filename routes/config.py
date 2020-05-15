import  os
import  sys

from routes import  app


SQLALCHEMY_DATABASE_URI = os.getenv('CAMPUS_DATABASE_URI')