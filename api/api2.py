'''
Simple API for interfacing with the front-end
'''

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
filename = './data/data.csv'

'''
route: '/'
method: home
Generic home page for API
'''
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Automatic People Counting Camera</h1>
<p>A prototype API for that returns number of people at a specific time in a specific location</p>'''

'''
route: '/population/all'
method: api_all

'''
@app.route('/pop/')
def api_all():
    data = refresh_data()
    return data

def refresh_data():
    file = open(filename, 'r')
    return file.read()

app.run()