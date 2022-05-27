# backbone of flask app
# all pieces must connect here
# hub of all communication between independent pieces of the flask app

from flask import Flask
from config import Config

# blueprints for registration
from .auth.routes import auth
from .api.routes import api

# imports for database stuff and login system
from .models import db, login
from flask_migrate import Migrate

# most important line
app = Flask(__name__)

app.config.from_object(Config)

# link of communication between blueprints and app
app.register_blueprint(auth)
app.register_blueprint(api)

# set up ORM and Migrate communication with app and eachother
db.init_app(app) # if this isnt here, our app and our database don't know how to talk to eachother (for queries, adding data, etc.)
migrate = Migrate(app, db) # this is actually giving us the ability to modify database structure from our flask app (aka create tables, etc.)

# set up for LoginManager
login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to see this page.'
login.login_message_category = 'danger'

# our flask app is really dumb. if we do not tell it about the existence of other files, it will assume they do not exist
# import the routes file here so that our Flask app knows the routes exist
# this is one of the only scenarios where imports will be at the bottom of a file 
    # these imports MUST be after the instantiation of the flask app (line 11) and the configuration (line 14)
from . import routes # from the app folder (this folder), import the entire routes file