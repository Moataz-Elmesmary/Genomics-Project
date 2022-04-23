#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np


# In[37]:


# Load the Random Forest CLassifier model
filename = 'diabetes.pkl'
classifier = pickle.load(open(filename, 'rb'))


# In[41]:


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
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
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)


# In[39]:


env FLASK_ENV=development


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




