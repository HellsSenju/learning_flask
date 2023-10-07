from flask import Flask, render_template
import pandas as pd
import random
from pandas import DataFrame
import matplotlib.pyplot as plt

app = Flask(__name__)


def plot():
    data = pd.read_csv('jio_mart_items.csv')
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    d = data.groupby('category').agg(price=('price', 'mean')).reset_index()
    d['price'] = d['price'].apply(lambda x: round(x, 1))
    plt.xlabel('Категории')
    plt.ylabel('Средняя цена')
    # print(d)
    # print(d.index)
    # print(d.values)
    barplot = plt.bar(x=d['category'], height=d['price'])
    plt.bar_label(barplot, labels=d['price'])
    plt.show()


# plot()


def drop(data: DataFrame):
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    data.set_index('category', inplace=True)
    print(data.shape[0])
    data.drop(['Groceries'], axis=0, inplace=True)
    # data.drop(['Home & Kitchen'], axis=0, inplace = True)
    data.drop(['Fashion'], axis=0, inplace=True)
    data.drop(['Beauty'], axis=0, inplace=True)
    data.to_csv('updated.csv')
    print(data.shape[0])


def new_csv():
    data = pd.read_csv('jio_mart_items.csv')
    # drop(data)

    category = data['category'].value_counts().index[0]
    sub_category = data['sub_category'].value_counts().index[0]
    href = data['href'].value_counts().index[0]
    items = data['items'].value_counts().index[0]

    for i in range(data.shape[0], round(data.shape[0] * 1.1) + 1, 1):
        max_price = data['price'].max()
        min_price = data['price'].min()
        avg = data['price'].mean()  # ср знач по столбцу price
        new_price = round(avg + random.uniform(min_price - avg, max_price - avg), 1)

        new_row = [category, sub_category, href, items, new_price]
        data.loc[i] = new_row

    data.to_csv('updated.csv', index=False)

# new_csv()


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


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
