import os
import joblib
import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from modeler.Modeler import Modeler

app = Flask(__name__)
api = Api(app)


class Predict(Resource):
    @staticmethod
    def post():
        predictions = {}
        orders = request.get_json()
        modeler = Modeler()

        for order in orders:
            order_id = order['order_id']
            store_id = order['store_id']
            to_user_distance = order['to_user_distance']
            to_user_elevation = order['to_user_elevation']
            total_earning = order['total_earning']
            created_at = order['created_at']

            date = pd.to_datetime(created_at)
            day_of_year = date.dayofyear
            day_of_week = date.dayofweek
            minutes = date.hour * 60 + date.minute

            prediction = modeler.predict([store_id, to_user_distance, to_user_elevation,
                                          total_earning, day_of_year, day_of_week, minutes])

            predictions[order_id] = {
                'input': {
                    'order_id': order_id,
                    'store_id': store_id,
                    'to_user_distance': to_user_distance,
                    'to_user_elevation': to_user_elevation,
                    'total_earning': total_earning,
                    'created_at': created_at
                },
                'taken': prediction
            }

        return jsonify(predictions)


api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
