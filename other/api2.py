import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Data
filename = './data/data.csv'

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Automatic People Counting Camera</h1>
<p>A prototype API for that returns number of people at a specific time in a specific location</p>'''

@app.route('/pop/')
def api_all():
    data = refresh_data()
    return data

def refresh_data():
    file = open(filename, 'r')
    return file.read()

app.run()