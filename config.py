# set up and organizing the applicatiuon file structure and configuration
# what secret variables does the app need
# and where is the base directory/root folder of the project:

# we are gonna need a little help from the os package
import os

# set up the base directory of the entire application - aka help our computer understand this app's file structure
basedir = os.path.abspath(os.path.dirname(__name__))

# set up a class for our configuration variables
class Config:
    FLASK_APP = os.environ.get('FlASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False