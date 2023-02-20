ROM python:3.8.3-slim

RUN pip install -U pip
RUN pip install pipenv 

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "predict.py", "linear_reg.bin", "./" ]

EXPOSE 5500

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:5500", "predict:app" ]
