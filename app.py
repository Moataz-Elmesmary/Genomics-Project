#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
from pyngrok import ngrok
import sys


# In[37]:


# Load the Random Forest CLassifier model
filename = 'diabetes.pkl'
classifier = pickle.load(open(filename, 'rb'))


# In[44]:


app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('./index.html')
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            preg = request.form['pregnancies']
            glucose = request.form['glucose']
            bp = request.form['bloodpressure']
            st = request.form['skinthickness']
            insulin = request.form['insulin']
            bmi = request.form['bmi']
            dpf = request.form['dpf']
            age = request.form['age']
            
            data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
            my_prediction = classifier.predict(data)
            
            return render_template('./result.html', prediction=my_prediction)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")

if __name__ == '__main__':
    # Open a HTTP tunnel on the default port 80
    public_url = ngrok.connect()
    ssh_url = ngrok.connect(22, "tcp")
    print(public_url)
    app.run(port=80)