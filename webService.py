import flask 
from tensorflow import keras
import numpy as np
from flask import jsonify

app = flask.Flask(__name__)


@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route("/predict/<input>")
def predict(input):
    model = keras.models.load_model('./model.h5')
    input = float(input)
    result = model.predict([input])
    return jsonify({"value":result.item(0)})


app.run(host="0.0.0.0")
