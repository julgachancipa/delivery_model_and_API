# Delivery model

## The Challenge

Train a classification model and expose it using an API, the model can predict the taken rate of and
order depending of the order transactional features. The model should be trained using
the attached dataset (orders.csv)

## Deployed version

[https://taken-model.herokuapp.com/](https://taken-model.herokuapp.com/)

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

NOTE: if you are running it locally the url will be [http://0.0.0.0:5000/](http://0.0.0.0:5000/)

### GET: stored estimations

https://taken-model.herokuapp.com/
