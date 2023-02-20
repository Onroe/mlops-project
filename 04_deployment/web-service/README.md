Create a virtual environment
Create a script for prediction(predict.py)
Create a script to call model(test.py)


Put the script into a Flask app

Run Flask app using Gunicorn
gunicorn --bind=0.0.0.0:5500 predict:app


Dockerize Flask app

#Build the image
docker build -t ride-duration-prediction-service:v1 .

#Run 
docker run -it --rm -p 5500:5500 ride-duration-prediction-service:v1
