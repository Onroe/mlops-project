import requests

ride = {
    "PULocationID": 25,
    "DOLocationID": 16,
    "trip_distance": 60
}

url = 'http://localhost:5500/predict'
response = requests.post(url, json=ride)
print(response.json())