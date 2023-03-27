from flask import Flask


app = Flask(__name__)

WELCOME_TO = {
    'home': 'welcome home',
    'back': 'welcome back'
}


@app.route('/welcome')
def welcome():
    return "welcome"


@app.route('/welcome/<page>')
def welcome_home_back(page):
    page = WELCOME_TO.get(page, '404 not found')
    return page
