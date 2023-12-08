from flask import Flask, request, render_template, Response
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from clustering import Clustering
import seaborn as sns
from io import BytesIO
import base64

app = Flask('__name__')

df = pd.read_csv('csv_files/for_tree.csv')
df.dropna(inplace=True)


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
    pic1 = before(_from, _to)
    pic2, pic3 = clustering(_from, _to, cluster_count)

    return render_template("lab7_clustering.html",
                           before=pic1, after=pic2,
                           lib=pic3)


def clustering(_from, _to, k):

    data = df[['category_mean_price', 'price']].iloc[_from:_to].copy()
    data = StandardScaler().fit_transform(data)
    # data = df[['category_mean_price', 'price']].iloc[_from:_to].to_numpy()

    kmeans = Clustering(k)
    try:
        kmeans.fit(data)
    except Exception as e:
        print(e)
    predicted = kmeans.predict(data)
    sns.scatterplot(x=[i[0] for i in data],
                    y=[i[1] for i in data],
                    hue=predicted,
                    style=predicted,
                    palette="deep",
                    legend=None
                    )

    plt.plot([x for x, i in kmeans.centroids],
             [y for i, y in kmeans.centroids],
             'k+',
             markersize=10)

    plt.title("После кластеризации")
    plt.xlabel("Средняя цена по категории")
    plt.ylabel("Цена товара")

    tmpfile = BytesIO()  # создание временного файла
    plt.savefig(tmpfile, format='png')
    plt.clf()
    plt.switch_backend('agg')
    pic1 = base64.b64encode(tmpfile.getvalue()).decode('utf-8')  # кодирование
    tmpfile.close()

    # БИБЛИОТЕЧНАЯ
    kmeans = KMeans(k, n_init=10, max_iter=300)
    kmeans.fit(data)
    # Получение меток кластеров для каждого элемента
    labels = kmeans.labels_

    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='rainbow')

    plt.title("После кластеризации")
    plt.xlabel("Средняя цена по категории")
    plt.ylabel("Цена товара")

    tmpfile = BytesIO()  # создание временного файла
    plt.savefig(tmpfile, format='png')
    plt.clf()
    plt.switch_backend('agg')
    pic2 = base64.b64encode(tmpfile.getvalue()).decode('utf-8')  # кодирование
    tmpfile.close()

    return pic1, pic2


def before(_from, _to):
    plt.xlabel("Средняя цена по категории")
    plt.ylabel("Цена товара")
    plt.scatter(df['category_mean_price'].iloc[_from:_to], df['price'].iloc[_from:_to], color='red')

    tmpfile = BytesIO()  # создание временного файла
    plt.title("До кластеризации")
    plt.savefig(tmpfile, format='png')
    plt.clf()
    plt.close('all')
    plt.switch_backend('agg')
    pic = base64.b64encode(tmpfile.getvalue()).decode('utf-8')  # кодирование
    tmpfile.close()

    return pic


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=30000)
