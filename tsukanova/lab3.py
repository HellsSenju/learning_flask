from flask import Flask, render_template
import pandas as pd
import random
from pandas import DataFrame

app = Flask(__name__)


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

    max_price = data['price'].max()
    min_price = data['price'].min()
    for i in range(data.shape[0], round(data.shape[0] * 1.1) + 1, 1):
        new_category = data['category'].value_counts().index[0]
        new_sub_category = data['sub_category'].value_counts().index[0]
        new_href = data['href'].value_counts().index[0]
        new_items = data['items'].value_counts().index[0]

        avg = data['price'].mean()  # ср знач по столбцу price
        new_price = avg + random.uniform(-avg, max_price - avg)

        new_row = [new_category, new_sub_category, new_href, new_items, new_price]
        data.loc[i] = new_row

    data.to_csv('updated.csv')


new_csv()

# @app.route('/')
# def home():
#     data = pd.read_csv('jio_mart_items.csv')
#     data.dropna(inplace=True)
#     data.drop_duplicates(inplace=True)
#
#     max_price = data['price'].max()
#     min_price = data['price'].min()
#     for i in range(data.shape[0], round(data.shape[0] * 1.1) + 1, 1):
#         new_category = data['category'].value_counts().index[0]
#         new_sub_category = data['sub_category'].value_counts().index[0]
#         new_href = data['href'].value_counts().index[0]
#         new_items = data['items'].value_counts().index[0]
#
#         avg = data['price'].mean()  # ср знач по столбцу price
#         new_price = avg + random.uniform(-avg, max_price - avg)
#
#         new_row = [new_category, new_sub_category, new_href, new_items, new_price]
#         data.loc[i] = new_row
#
#     html = """""
#     <div class="container mt-4">
#           <div class="card">
#                 <h1 class="text-center"> {task} </h1>
#                 <div class="container mt-4">
#                     <div class="table align-middle table-bordered">
#                         {table}
#                     </div>
#                 </div>
#           </div>
#     </div>
#     """""
#
#     return render_template("base.html") \
#         + html.format(task="Расширенный датасет", table=data.to_html(
#             classes='table-sm table align-middle table-bordered',
#             justify='center'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True, threaded=True)
