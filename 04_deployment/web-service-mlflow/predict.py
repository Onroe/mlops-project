import pickle

from flask import Flask, request, jsonify

MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
RUN_ID = 'ea60e6e130e144d385161c8836084824'

logged_model = f'http://127.0.0.1:5000/api/2.0/mlflow-artifacts/artifacts/1/{RUN_ID}/artifacts/model'

# logged_model = f'runs:/{RUN_ID}/model'
model = mlflow.pyfunc.load_model(logged_model)


def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def predict(features):
    X = dv.transform(features)
    preds = model.predict(X)
    return float(preds[0])


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5500)