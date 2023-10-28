from flask import Flask, render_template
import pandas as pd
import random
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import preprocessing

app = Flask(__name__)


def scatter_plot():
    data = pd.read_csv('jio_mart_items.csv')
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    price = preprocessing.normalize([np.asarray(data['price'])])
    data['price'] = pd.DataFrame(price[0])
    data = data.astype({'price': str})
    # d = DataFrame({'category': data['category'], 'price': data['price']})
    # categories = data['category'].drop_duplicates().reset_index().index.values
    color = ['lightcoral', 'darkorange', 'olive', 'teal', 'violet', 'skyblue']
    categories = data['category'].drop_duplicates().values
    print(categories)
    # plt.scatter(data['category'], data['price'], c=categories)

    for i in range(len(categories)):
        # print(data[data['category'] == categories[i]]['category'])
        x = data[data['category'] == categories[i]]['category']
        y = data[data['category'] == categories[i]]['price']
        plt.scatter(x, y, c=color[i])

    # ax = plt.gca()
    # ax.yaxis.set_major_locator(plt.MultipleLocator(0.005))

    plt.ylim(0, 10)
    plt.show()


scatter_plot()


@app.route('/')
def home():
    data = pd.read_csv('updated.csv')
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    html = """""
    <div class="container mt-4">
          <div class="card">
                <h1 class="text-center"> {task} </h1>
                <br>
                <h3 class="text-center"> Было строк данных - {old} </h3>
                <h3 class="text-center"> Стало строк данных - {new} </h3>
                <br>
                <div class="container mt-4">
                    <div class="table align-middle table-bordered">
                        {table_head}
                    </div>
                </div>
                <div class="container mt-4">
                    <div class="table align-middle table-bordered">
                        {table_tail}
                    </div>
                </div>
          </div>
    </div>
    """""

    return render_template("base.html") \
        + html.format(task="Расширенный датасет",
                      old=pd.read_csv('jio_mart_items.csv').shape[0],
                      new=pd.read_csv('updated.csv').shape[0],
                      table_head=data.head(5).to_html(
                        classes='table-sm table align-middle table-bordered',
                        justify='center'),
                      table_tail=data.tail(5).to_html(
                        classes='table-sm table align-middle table-bordered',
                        justify='center'))


# if __name__ == '__main__':
#     app.run(debug=True, threaded=True)
