# python-fastapi-and-r
A test projet which shows how to build a Python FastAPI + R sidecar

### Install dependencies

pip install -r requirements.txt

### Run tests

pytest

### Start application (port : 5000)

python -m main.app

### Request :

GET http://localhost:5000/crypto/eth-eur/stats
GET http://localhost:5000/crypto/eth-eur/predict

### Run R side car

1. Install dependencies from dependencies.r
2. Run the R script 'main.r'

You can test the R sidecar separatly

### Run the whole application

1. Run the R sidecar in background
2. Run the FastAPI application

Warning : Configuration comes with nice defaults but do not forget to check it