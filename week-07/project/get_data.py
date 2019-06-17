import requests as re
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize

def get_data():
    zed_index = '?'
    include_sold = '1'
    page_number = 1
    listing_status = 'sale'
    page_size = '20'
    order_by = 'age'
    area = 'somerset'
    api_key = 'jwttfkz79asz2d9h8sms7tuu'

    url = 'http://api.zoopla.co.uk/api/v1/property_listings.js?zed_index=?&include_sold=1&page_number=3&listing_status=sale&page_size=10&order_by=age&area=somerset&api_key=jwttfkz79asz2d9h8sms7tuu'
    response = re.get(url)
    json_normalize(response)    