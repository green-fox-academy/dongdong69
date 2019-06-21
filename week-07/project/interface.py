import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify, make_response
from get_loc import get_loc
from sklearn.externals import joblib
from data_to_df import data_to_df, result

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def hello_world():
    return render_template('predict.html')

@app.route("/doPost",methods=["post"])
def handPost():
    postcode = request.form.get('postcode')
    post_town = request.form.get('post_town')
    property_type = request.form.get('property_type')
    bathrooms = int(request.form.get('bathrooms'))
    floors = int(request.form.get('floors'))
    bedrooms = int(request.form.get('bedrooms'))
    recepts = int(request.form.get('recepts'))
    new_home = int(request.form.get('new_home'))

    data = data_to_df(property_type, bathrooms, bedrooms, floors, recepts, postcode, post_town, new_home)
    data = data[:-1]
    length = len(data)
    price = str(np.exp(result(data.reshape(1, length))))

    return "<h1>The price of your home:"+price+"</h1>"

if __name__ == '__main__':
    app.run()