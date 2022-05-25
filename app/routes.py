from app import app
from flask import render_template, flash
import requests as r
from flask_login import login_required
@app.route('/')

def home():
    greeting = 'Hello, Enrique'
    print(greeting)
    return render_template('home.html', g=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services-list')
def services():
    return render_template('services.html')