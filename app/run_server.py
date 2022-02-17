# USAGE
# Start the server:
# python run_front_server.py
# Submit a request via Python:
# python simple_request.py

# import the necessary packages
import dill
import pandas as pd
import os
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
dill._dill._reverse_typemap['ClassType'] = type


# initialize our Flask application
app = flask.Flask(__name__)
handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = dill.load(f)
        print(model)
    return model


@app.route("/", methods=["GET"])
def general():
    return """Welcome to prediction process. Please use 'http://<address>/predict' to POST"""


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    model_path = "/app/app/models/choco_pipeline.dill"

    
    data = {"success": False}
    dt = strftime("[%Y-%b-%d %H:%M:%S]")
    sample_json = dict()
    required_keys = {"Company (Manufacturer)", "Company Location", "Review Date", "Country of Bean Origin",
                     "Specific Bean Origin or Bar Name", "Cocoa Percent", "Ingredients",
                     "Most Memorable Characteristics"}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        sample_json = flask.request.get_json()

    if set(sample_json.keys()) == required_keys:
        logger.info(f'{dt} Data: {sample_json}')
        choco_model = load_model(model_path)
        try:
            sample_df = pd.DataFrame(sample_json, index=[0])
            preds = choco_model.predict(sample_df)
        except AttributeError as e:
            logger.warning(f'{dt} Exception: {str(e)}')
            data['predictions'] = str(e)
            data['success'] = False
            return flask.jsonify(data)
        except Exception as e:
            logger.error(f'Exception: {str(e)}')
        print(preds)
        data["predictions"] = preds[0]
        # indicate that the request was a success
        data["success"] = True
    # return the data dictionary as a JSON response
    return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading the model and Flask starting server... please wait until server has fully started"))
    port = int(os.environ.get('PORT', 8180))
    # app.run(debug=True, port=port)
    app.run(host='0.0.0.0', debug=True, port=port)
    # app.run(host='127.0.0.1', debug=True, port=port)
