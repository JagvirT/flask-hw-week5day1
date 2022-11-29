from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    favorite_teams = ['Las Vegas Raiders', 'Golden State Warriors', 'Oakland Athletics', 'San Francisco Giants', 'San Jose Sharks']
    return render_template('index.html', teams= favorite_teams)

@app.route('/raiders')
def raiders():
    return render_template('raiders.html')


@app.route('/giants')
def giants():
    return render_template('giants.html')

@app.route('/sharks')
def sharks():
    return render_template('sharks.html')

@app.route('/athletics')
def athletics():
    return render_template('athletics.html')

@app.route('/warriors')
def warriors():
    return render_template('warriors.html')