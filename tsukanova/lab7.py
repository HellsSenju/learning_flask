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

# kmeans = Clustering()
# print(df[['category_mean_price', 'price']].iloc[0:3].to_numpy())
# kmeans.do(df[['category_mean_price', 'price']].iloc[0:3].to_numpy())
# print(df[['category_mean_price', 'price']].to_numpy())


@app.route('/')
def home():
    return render_template("lab7_home.html")


@app.route('/plot_clustering', methods=['GET'])
def plot_clustering():
    data = request.args
    _from = int(data['_from'])
    _to = int(data['_to'])
    if _from > _to:
        _from, _to = _to, _from

    cluster_count = int(data['k'])
    encoded1 = before(_from, _to)
    encoded2 = clustering(_from, _to, cluster_count)
    return render_template("lab7_clustering.html",
                           before=encoded1, after=encoded2)


def clustering(_from, _to, k):
    data = df[['category_mean_price', 'price']].iloc[0:3].to_numpy()

    kmeans = Clustering(k)
    kmeans.do(data)

    centroids, centroid_id = kmeans.adds(data)
    sns.scatterplot(x=[i[0] for i in data],
                    y=[i[1] for i in data],
                    hue=centroid_id,
                    style=centroid_id,
                    palette="deep",
                    legend=None
                    )

    plt.plot([x for x, i in kmeans.centroids],
             [y for i, y in kmeans.centroids],
             markersize=10)

    plt.xlabel("Средняя цена по категории")
    plt.ylabel("Цена товара")

    tmpfile = BytesIO()  # создание временного файла
    plt.title("После кластеризации")
    plt.savefig(tmpfile, format='png')
    plt.clf()
    plt.switch_backend('agg')
    pic = base64.b64encode(tmpfile.getvalue()).decode('utf-8')  # кодирование
    tmpfile.close()

    return pic


def before(_from, _to):
    plt.xlabel("Средняя цена по категории")
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


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=30000)