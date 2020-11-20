from app import app
from flask import Flask, render_template


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')