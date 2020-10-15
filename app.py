import pandas as pd

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from modeler.Modeler import Modeler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Order

app = Flask(__name__)
api = Api(app)


def load_session():
    """
    It loads the SQLAlquemy session
    :return: session
    """
    db_path = 'db.sqlite'
    engine = create_engine('sqlite:///%s' % db_path, echo=True)

    session = sessionmaker(bind=engine)
    session = session()
    return session


def order_to_db(order_data, prediction):
    session = load_session()

    order = (
        session.query(Order)
        .filter_by(order_id=order_data['order_id'])
        .first()
    )

    if order is None:
        order = Order(order_id=order_data['order_id'])

    order.store_id = order_data['store_id']
    order.to_user_distance = order_data['to_user_distance']
    order.to_user_elevation = order_data['to_user_elevation']
    order.total_earning = order_data['total_earning']
    order.created_at = order_data['created_at']
    order.taken = prediction

    session.add(order)
    session.commit()
    session.commit()
    session.close()


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

            order_info = [store_id, to_user_distance, to_user_elevation,
                          total_earning, day_of_year, day_of_week, minutes]
            prediction = modeler.predict(order_info)

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
            order_to_db(order, prediction)

        return jsonify(predictions)


api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(port=5000)
