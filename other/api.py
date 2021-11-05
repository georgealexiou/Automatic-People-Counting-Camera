from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

# /population
population_path = './data/data.csv'

class Population(Resource):
    def get(self):
        data = pd.read_csv(population_path)
        data = data.to_dict()
        return {'data': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('time', required=True, type=str)
        parser.add_argument('people', required=True, type=int)
        args = parser.parse_args()

        data = pd.read_csv(population_path)

        if args['time'] in data['time']:
            return {
                'message': f"{args['time']} already exists"
            }, 409
        else:
            data = data.append({
                'time': args['time'],
                'people': args['people']
            }, ignore_index=True)

            data.to_csv(population_path, index=False)
            return {'data': data.to_dict()}, 200

api.add_resource(Population, '/population')

if __name__ == "__main__":
    app.run()