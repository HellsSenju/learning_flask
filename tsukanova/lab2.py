from flask import Flask, render_template
import pandas as pd
from pretty_html_table import build_table
import numpy as np

app = Flask(__name__)
data = pd.read_csv('jio_mart_items.csv')

category = data.groupby(['category']).agg({'price': ['min', 'max', 'mean']}).reset_index()
print(category.max().reset_index())

# print(data[ data['category'] == 'Groceries']['items'].head())


# category = data.groupby(['category']).agg({'price': ['min', 'max', 'mean']})
# sub_category = data.groupby(['sub_category']).agg({'price': ['min', 'max', 'mean']})
# max.rename(columns={'price' : 'max'}, inplace = True)
# print(category)
# print(sub_category)
# print(category.axes[0])
# print(category.axes[0].values) # закинуть в шаблон

description = 'В наборе данных хранить информации о продуктах JIO'

task1 = 'Минимальная, максимальная, средняя цена в разрезе категорий'
task2 = 'Минимальная, максимальная, средняя цена в разрезе подкатегорий'
task3 = 'Минимальная, максимальная, средняя цена за килограмм'


@app.route('/')
def home():
    data.dropna(inplace=True)

    category = data.groupby(['category']).agg({'price': ['min', 'max', 'mean']}).reset_index()
    category.columns = ['Категории:', 'Минимальная цена: ', 'Максимальная цена: ', 'Средняя цена: ']
    max_category = data['']

    sub_category = data.groupby(['sub_category']).agg({'price': ['min', 'max', 'mean']}).reset_index()
    sub_category.columns = ['Подкатегории:', 'Минимальная цена: ', 'Максимальная цена: ', 'Средняя цена: ']

    cat_table = build_table(category, 'red_light')
    sub_cat_table = build_table(sub_category, 'red_light')

    return '<h1 style="text-align: center; padding-top: 15px; font-size: 45px">' + description + '</h1><br>' \
    + '<h1 style="text-align: center; padding: 0.5%; font-size: 25px">' + task1 + '</h1>' \
    + '<div align="center">' + cat_table + '</div>' \
    + '<h1 style="text-align: center; padding: 0.5%; font-size: 25px">' + task2 + '</h1>' \
    + '<div align="center">' + sub_cat_table + '</div>'


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
