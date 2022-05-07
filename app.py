#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import sys


# In[37]:


# Load the Random Forest CLassifier model
filename = 'diabetes.pkl'
classifier = pickle.load(open(filename, 'rb'))


# In[44]:


app = Flask(__name__,static_url_path='', static_folder='./templates')

@app.route('/')
def home():
    try:
        return render_template('./home.html')
    except:
        ops = str(sys.exc_info())
        return('<h1>Oops!' + ops + 'occurred</h1>')


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
        ops = str(sys.exc_info())
        return('<h1>Oops!' + ops + 'occurred</h1>')

if __name__ == '__main__':
    app.run(debug=True)
