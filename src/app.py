import pickle
import pandas as pd
from flask import Flask, request, render_template

# Load the model
model_file='../models/model.pkl'

with open(model_file, 'rb') as input_file:
    model=pickle.load(input_file)

# Define the flask application
app=Flask(__name__)

class_dict = {
    "0": "Not Diabetic",
    "1": "Diabetic"
    
}


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':


        val1 = float(request.form["Glucose"])
        val2 = float(request.form["Insulin"])
        val3 = float(request.form["BMI"])
        val4 = float(request.form["Age"])
        
        data = [[val1, val2, val3, val4]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
        
        # Get the data from the form - take a look at the tutorial
        # for a hint on how to do this. Also, if you are using the model
        # supplied above, you need to send it four features: Glucose,
        # Insulin, BMI and Age

        # Next format the data for input into the model. For the model
        # Supplied above, it should be a Pandas dataframe with four
        # columns, one for each feature and one row.

        # Then do the prediction and covert the class number that the
        # model returns to a human readable string, like 'diabetic' etc.

    # Return the result to flask
    return render_template('index.html', prediction=pred_class)