from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

import tensorflow as tf
import numpy as np
import pandas as pd
from joblib import load

cloth_model = load('cloth_size_prediction.sav')

"""
def get_cloth(w, a, h):
    sample_data = {'weight':[w], 'age':[a], 'height':[h]}
    clothdf = pd.DataFrame(data=sample_data)
    return clothdf
"""

def return_cloth(model, sample_data):
    weight = sample_data['cloth_weight']
    age = sample_data['cloth_age']
    height = sample_data['cloth_height']

    sample_data = {'weight':[weight], 'age':[age], 'height':[height]}

    clothdf = pd.DataFrame(data=sample_data)

    return model.predict(clothdf)[0]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class ClothSizePredictingForm(FlaskForm):

    weight = StringField("Weight")
    age = StringField("Age")
    height = StringField("Height")

    submit = SubmitField("Predict")

@app.route("/", methods=['GET','POST'])
def index():
    form = ClothSizePredictingForm()

    if form.validate_on_submit():
        session['weight'] = form.weight.data
        session['age'] = form.age.data
        session['height'] = form.height.data

        return redirect(url_for("prediction"))
    
    return render_template('index.html', form=form)

@app.route('/prediction')
def prediction():
    content = {}
    content['cloth_weight'] = float(session['weight'])
    content['cloth_age'] = float(session['age'])
    content['cloth_height'] = float(session['height'])

    results =  return_cloth(cloth_model, content)

    return render_template('predictions.html', results=results)
    
if __name__=="__main__":
    app.run()
