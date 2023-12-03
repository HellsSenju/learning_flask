from flask import Flask, request, render_template, Response
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
from clustering import Clustering
import seaborn as sns
from io import BytesIO
import base64

app = Flask('__name__')

df = pd.read_csv('csv_files/csv_encoded.csv')
df.dropna(inplace=True)
kmeans = Clustering()
print(df[['category_mean_price', 'price']].iloc[0:3].to_numpy())
kmeans.do(df[['category_mean_price', 'price']].iloc[0:3].to_numpy())
# print(df[['category_mean_price', 'price']].to_numpy())


def before(_from, _to):
    plt.xlabel("средняя цена по категории")
    plt.ylabel("Цена товара")
    plt.scatter(df['category_mean_price'].iloc[_from:_to], df['price'].iloc[_from:_to], color='red')

    tmpfile = BytesIO()  # создание временного файла
    plt.title("До кластеризации")
    plt.savefig(tmpfile, format='png')
    plt.clf()
    plt.switch_backend('agg')
    pic = base64.b64encode(tmpfile.getvalue()).decode('utf-8')  # кодирование
    tmpfile.close()

    return pic
