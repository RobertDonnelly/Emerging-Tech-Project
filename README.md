# Emerging-Tech-Project 
## Robert Donnelly
## G00358931

A Web Application that uses a trained machine learning model using data from 'powerproduction.txt' to make predictions on the power a wind turbine will produce depending on the speed of the wind which will be input by a user.

# Contents of repository
'index.html' - located inside static folder, is the is the basic user interface of application. <br/>
'webService.py' - takes in the trained model 'model.h5' and handles 'index.html' requests.<br/>
'myModel.ipynb' - JupyterNotebook which trains the mdoel and saves it<br/> 
'requirements.txt' - file which tells docker what files to install

# Running the App
## Linux
```bash
export FLASK_APP=webService.py
python3 -m flask run
```

## Windows
```bash
set FLASK_APP=webService.py
python -m flask run
```

```bash
docker build . -t webService-image
docker run --name webService-container -d -p 5000:5000 webService-image
```
