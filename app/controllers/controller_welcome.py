from app import app
from flask import render_template, redirect


@app.route('/')
def index():
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title = 'Welcome')

