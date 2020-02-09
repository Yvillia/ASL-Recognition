from flask import render_template, jsonify, request, redirect, url_for
import io
import json
import os
import sys
import cv2
import time
import requests

from app import app

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for("home"))

@app.route('/home')
def home():
    return render_template('home.html', title="Home")


@app.route('/home', methods=['GET', 'POST'])
@app.route('/pickup', methods=['GET', 'POST'])
def imgHandler():
    if request.method == 'POST':
        if request.form.get('returnBtn') == 'return':
            return redirect(url_for('home'))
        if request.form.get('photoBtn') == 'camera':
            response = requests.post("http://localhost:5000/predict",
                            files={"image": open(os.path.join(app.root_path, 'images/finalsign.jpg'), 'rb')})
            data_dict = response.json()
            # if os.path.exists(os.path.join(app.root_path, 'images/finalsign.jpg')):
            #     os.remove(os.path.join(app.root_path, 'images/finalsign.jpg'))
            # if os.path.exists(os.path.join(app.root_path, 'images/sign.jpg')):
            #     os.remove(os.path.join(app.root_path, 'images/sign.jpg'))
            return render_template('predicted.html', title="Prediction", 
                prediction=data_dict['class_name'])
    else: 
        return render_template('predicted.html', title="Error",
                prediction="Sorry Didn't Work")

