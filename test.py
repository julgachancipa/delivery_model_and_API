import requests
import pprint

res = requests.post(
    url='http://localhost:5000/predict',
    json=[
            {
                'order_id': 14364873,
                'store_id': 30000009,
                'to_user_distance': 29.4781006757058885,
                'to_user_elevation': -72.71936035156295,
                'total_earning': 5000,
                'created_at': '2017-09-09T20:02:17Z',
            },
            {
                'order_id': 14370258,
                'store_id': 900014452,
                'to_user_distance': 2.6714317179354317,
                'to_user_elevation': 1.72265625,
                'total_earning': 4400,
                'created_at': '2017-09-07T20:15:19Z',
            }
        ]
)

pprint.pprint(res.json())
