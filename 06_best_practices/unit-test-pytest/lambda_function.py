import os

import model

PREDICTIONS_STREAM_NAME = os.getenv('PREDICTIONS_STREAM_NAME', 'ride_predictions')
#RUN_ID = os.getenv('RUN_ID')
RUN_ID = '0df9d76e965b481e9e5cefe26aa2eb24'
TEST_RUN = os.getenv('TEST_RUN', 'False') == 'True'


model_service = model.init(
    prediction_stream_name=PREDICTIONS_STREAM_NAME,
    run_id=RUN_ID,
    test_run=TEST_RUN,
)


def lambda_handler(event, context):
    # pylint: disable=unused-argument
    return model_service.lambda_handler(event)