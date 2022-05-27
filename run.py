# purpose of this file is to give my terminal and flask shell access to my app
# so that i can test through the shell

# when you want to do this method
# change the FLASK_APP variable to .env to run.py

# import the things we need
from app import app
from app.models import db, Animal, User, Post


# creating the shell context processor
@app.shell_context_processor
def shell_context():
    return {'db': db, 'Animal': Animal, 'User': User, 'Post':Post}