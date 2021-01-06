import flask
from tensorflow import  keras
import numpy as np
import json
from flask import request

app = flask.flask(__name__)

model = keras.models.load_model("./model.h5")

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/predict',methods =["POST"])
def predict():
    data = {"success":False}
    print(model)
    #get param
    params = flask.request.form 
    if(params == None):
        params = flask.request.form 
    if(params != None):
        pValue = params['value']
        myArray = np.array([pValue])
        x = model.predict(myArray)
        list = x.tolist()
        jsonString = json.dumps(list)
        data["response"] = jsonString
        data["success"] = True
    return flask.jsonify(data)#return in json


app.run(host="0.0.0.0")
