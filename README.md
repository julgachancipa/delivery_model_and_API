# Delivery model

## The Challenge

Train a classification model and expose it using an API, the model can predict the taken rate of and
order depending of the order transactional features. The model should be trained using
the attached dataset (orders.csv)

## Deployed version

https://taken-model.herokuapp.com/

## Run the project locally using Docker Compose

Create and initialize the database running:
```
python db_setup.py
```

Build image and start container:
```
docker-compose up --build
```

## Documentation

NOTE: if you are running it locally the url will be http://0.0.0.0:5000/

### GET: stored estimations

https://taken-model.herokuapp.com/

#### Example
Response:
```
[{"created_at":"2017-09-07T20:15:19Z","order_id":14370258,"store_id":900014452,"taken":1,"to_user_distance":2.6714317179354317,"to_user_elevation":1.72265625,"total_earning":4600},{"created_at":"2017-12-09T20:02:17Z","order_id":18764800,"store_id":300000179,"taken":1,"to_user_distance":300.4781006757059,"to_user_elevation":500.71936035156295,"total_earning":7000}]
```

### POST: make one or multiple estimations

https://taken-model.herokuapp.com/predict

#### Example

```
import requests
import pprint

res = requests.post(
    url='https://taken-model.herokuapp.com/predict',
    json=[
            {
                'order_id': 143648070,
                'store_id': 30000009,
                'to_user_distance': 29.4781006757058885,
                'to_user_elevation': 872.71936035156295,
                'total_earning': 4300,
                'created_at': '2017-12-09T20:02:17Z',
            },
            {
                'order_id': 36780258,
                'store_id': 900014452,
                'to_user_distance': 2.6714317179354317,
                'to_user_elevation': 1.72265625,
                'total_earning': 5400,
                'created_at': '2017-09-07T20:15:19Z',
            }
        ]
)

pprint.pprint(res.json())

```

Response:

```
{'143648070': {'input': {'created_at': '2017-12-09T20:02:17Z',
                         'order_id': 143648070,
                         'store_id': 30000009,
                         'to_user_distance': 29.47810067570589,
                         'to_user_elevation': 872.719360351563,
                         'total_earning': 4300},
               'taken': 1},
 '36780258': {'input': {'created_at': '2017-09-07T20:15:19Z',
                        'order_id': 36780258,
                        'store_id': 900014452,
                        'to_user_distance': 2.6714317179354317,
                        'to_user_elevation': 1.72265625,
                        'total_earning': 5400},
              'taken': 1}}
```
