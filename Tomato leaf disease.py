# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 01:10:19 2020

@author: Ajay
"""

import numpy as np
import os
import pickle
import cv2
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model


app = Flask(__name__)

upload_folder = ''

pkl_file = pickle.load(open('diseases.pkl', 'rb'))

MODEL_PATH = 'Tomato_prediction_model.h5'
model = load_model(MODEL_PATH)

def model_predict(image_path):
  x = cv2.imread(image_path)
  gray = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
  p = cv2.resize(gray, (224,224))
  y = np.expand_dims(p, a/xis=0)
  probab = model.predict(y)
  result = np.argmax(probab)
  if result==7:
      return 'Leaf is healthy'
  else:
      return 'Leaf is infected with {}'.format(pkl_file[result])
@app.route('/',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            file_path = os.path.join(upload_folder, image_file.filename)
            image_file.save(file_path)
            preds = model_predict(file_path)
            return render_template("app.html", prediction=preds)
    return render_template("app.html", prediction='NAN')

if __name__ == "__main__":
    app.run(port=12000)