from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, feature_extraction
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

#  Зависимость цены от категории
# Home & Kitchen    60329
# Groceries         46043
# Fashion           26087
# Electronics       19018
# Beauty            10733
# Jewellery            70


def encoding():
    data = pd.read_csv('csv_files/jio_mart_items.csv', sep=',')
    data.dropna(inplace=True)

    data['category_mean_price'] = data['category'].map(data.groupby('category')['price'].mean().round())
    data.to_csv('csv_files/csv_encoded.csv', index=False)


# encoding()


def linear_regression():
    data = pd.read_csv('csv_files/csv_encoded.csv', sep=',')
    data.dropna(inplace=True)
    lr: pd.DataFrame
    # X - независимая переменная
    x = data['category_mean_price']
    # lr['X'] = data['category_mean_price']

    # Y - зависимая переменная
    y = data['price']
    # lr['Y'] = data['price']

    # добавление константы b_0
    x = sm.add_constant(x, prepend=False)

    model = OLS(y, x)
    # вычисление наилучшей регрессионной линии
    res = model.fit()
    print(res.summary())


linear_regression()


def scatter_plot():
    data = pd.read_csv('csv_files/csv_normalize_and_standardize.csv')

    # d = DataFrame({'category': data['category'], 'price': data['price']})
    # categories = data['category'].drop_duplicates().reset_index().index.values

    color = ['lightcoral', 'darkorange', 'olive', 'teal', 'violet', 'skyblue']
    categories = data['category'].drop_duplicates().values

    # print(categories)
    # plt.scatter(data['category'], data['price'], c=categories)

    for i in range(len(categories)):
        # print(data[data['category'] == categories[i]]['category'])
        x = data[data['category'] == categories[i]]['category']
        y = data[data['category'] == categories[i]]['price']
        print(x)
        print(y)
        plt.scatter(x, y, c=color[i])

    # ax = plt.gca()
    # ax.yaxis.set_major_locator(plt.MultipleLocator(0.01))

    plt.ylim(-1, 1)
    # plt.ticklabel_format(style='plain')
    plt.show()


# scatter_plot()


@app.route('/')
def home():
    data = pd.read_csv('csv_files/updated.csv')
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
                      old=pd.read_csv('csv_files/jio_mart_items.csv').shape[0],
                      new=pd.read_csv('csv_files/updated.csv').shape[0],
                      table_head=data.head(5).to_html(
                        classes='table-sm table align-middle table-bordered',
                        justify='center'),
                      table_tail=data.tail(5).to_html(
                        classes='table-sm table align-middle table-bordered',
                        justify='center'))


# if __name__ == '__main__':
#     app.run(debug=True, threaded=True)
