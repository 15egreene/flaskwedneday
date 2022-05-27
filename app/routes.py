# flask routes control what content is shown on what url
    # depending on how user is accessing url(what buttopns they've pressed, what their permissions are, what requests they have made etc.)

# these are our tools need to connect everthing together
from app import app
from flask import render_template, flash


import requests as r
from .services import getF1Drivers
from flask_login import login_required
from .models import User, Post, db


@app.route('/')

def home():
    greeting = 'Hello, Enrique'
    print(greeting)
    return render_template('home.html', g=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

# let's look at a more complex example of routing and using python code
@app.route('/services-list', methods=['GET'])
@login_required
def f1Drivers():
    # make an API call and utilize information from that API call in the HTML templating
    # in order to make an API call we need the requests package... let's install and import the requests package
    context = getF1Drivers() # sets the value of the context variable to a dictionary - the return value of the getF1Drivers function
    return render_template('f1.html', **context)


    # blog route #1 - profile page
@app.route('/blog/<string:username>', methods=['GET'])
def userProfile(username):
    # Is this an actual user?
    user = User.query.filter_by(username=username).first()
    # now we have our user - get their posts
    posts = Post.query.filter_by(author=user.id).all()
    # Maybe I want to change up how our timestamps look before they hit the page
    for p in posts:
        p.timestamp = str(p.timestamp)[:-7]
    # now that we have the user object and all of their posts, send that data over to the template to be rendered
    return render_template('profile.html', user=user, posts=posts)