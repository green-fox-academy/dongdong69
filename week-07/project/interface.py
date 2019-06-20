import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify, make_response
from get_loc import get_loc
from sklearn.externals import joblib

app = Flask(__name__, static_url_path="/static")

k_model = joblib.load("k_model.m")
rf = joblib.load("random_forest.m")

@app.route('/')
def hello_world():
    return render_template('predict.html')

@app.route("/doPost",methods=["post"])
def handPost():
    postcode = request.form.get('postcode')
    post_town = request.form.get('post_town')
    property_type = request.form.get('property_type')
    bathrooms = request.form.get('bathrooms')
    floors = request.form.get('floors')
    bedrooms = request.form.get('bedrooms')
    recepts = request.form.get('recepts')
    new_home = request.form.get('new_home')

    return "<h1>username:"+postcode+", password:"+new_home+"</h1>"

if __name__ == '__main__':
    app.run()