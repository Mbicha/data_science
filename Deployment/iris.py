from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

import tensorflow as tf
from keras.models import load_model
import numpy as np
import joblib

def return_prediction(model, scaler, sample_json):
    s_len = sample_json['sepal_length']
    s_wid = sample_json['sepal_width']
    p_len = sample_json['petal_length']
    p_wid = sample_json['petal_width']
    
    flower = [[s_len, s_wid, p_len, p_wid]]
    
    classes = np.array(['setosa', 'versicolor', 'virginica'])
    
    flower = scaler.transform(flower)
    
    #(model.predict(x) > 0.5).astype("int32")---when using sigmoid
    class_ind = np.argmax(model.predict(flower), axis=1)[0]
    
    return classes[class_ind]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class FlowerForm(FlaskForm):

    sep_len = StringField("Sepal Length")
    sep_wid = StringField("Sepal Width")
    pet_len = StringField("Petal Length")
    pet_wid = StringField("Petal Width")

    submit = SubmitField("Predict")

@app.route("/", methods=['GET','POST'])
def index():
    form = FlowerForm()

    if form.validate_on_submit():
        session['sep_len'] = form.sep_len.data
        session['sep_wid'] = form.sep_wid.data
        session['pet_len'] = form.pet_len.data
        session['pet_wid'] = form.pet_wid.data

        return redirect(url_for("prediction"))
    
    return render_template('home.html', form=form)

flower_model = load_model('final_iris_model.h5')
flower_sacler = joblib.load("iris_scaler.pkl")

@app.route('/prediction')
def prediction():
    content = {}
    content['sepal_length'] = float(session['sep_len'])
    content['sepal_width'] = float(session['sep_wid'])
    content['petal_length'] = float(session['pet_len'])
    content['petal_width'] = float(session['pet_wid'])

    results =  return_prediction(flower_model,flower_sacler, content)

    return render_template('prediction.html', results=results)
    
if __name__=="__main__":
    app.run()
