from flask import Flask, render_template
import pandas as pd
from bloomFilter import BloomFilter
import random
from pandas import DataFrame
import matplotlib.pyplot as plt

app = Flask(__name__)

data = pd.read_csv('jio_mart_items.csv')
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

keys = data['category'].drop_duplicates().tolist() + data['sub_category'].drop_duplicates().tolist()

bf = BloomFilter(len(keys) * 2, len(keys))
for i in range(len(keys)):
    BloomFilter.add_to_filter(keys[i])


@app.route('/')
def home():
    return render_template("lab4_home.html")


@app.route('/bloomFilter', methods=['GET'])
def bloom_filter():

    return render_template("home.html")


# if __name__ == '__main__':
#     app.run(debug=True, threaded=True)
