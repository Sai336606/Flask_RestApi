from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask App'

@app.route('/home')
def home():
    return 'This is the home page'


@app.route('/about')
def about():
    return 'This is the about page'


from controller import *