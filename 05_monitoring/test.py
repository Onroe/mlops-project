import requests

ride = {
    "PULocationID": 22,
    "DOLocationID": 16,
    "trip_distance": 60
}

url = 'http://127.0.0.1:9696/predict'
response = requests.post(url, json=ride)
print(response.json())