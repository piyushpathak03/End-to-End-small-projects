import sys, os, glob, re
import numpy as np
from wsgiref import simple_server
from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
# Keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from Cloths_Predictions.predictions import Cloths_Classification
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        cloth = Cloths_Classification()
        cloth.list_and_delete_previous_files()

        f = request.files['file']
        basepath = os.path.dirname(__file__)
        if not os.path.exists('uploads'):
            os.mkdir('uploads')
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        result = cloth.get_prediction(file_path)
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)