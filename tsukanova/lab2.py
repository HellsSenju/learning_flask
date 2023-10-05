from flask import Flask, request, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

data = pd.read_csv('jio_mart_items.csv')
data.dropna(inplace=True)

# print(data[ data['category'] == 'Groceries']['items'].head())


category = data.groupby(['category']).agg({'price': ['min', 'max', 'mean']})
sub_category = data.groupby(['sub_category']).agg({'price': ['min', 'max', 'mean']})
# max.rename(columns={'price' : 'max'}, inplace = True)
print(category)
print(sub_category)
# print(category.axes[0])
# print(category.axes[0].values) # закинуть в шаблон

description = 'В наборе данных хранить информации о продуктах JIO'

task1 = 'Минимальная, максимальная, средняя цена в разрезе категорий'
task2 = 'Минимальная, максимальная, средняя цена в разрезе подкатегорий'
task3 = 'Минимальная, максимальная, средняя цена за килограмм'

@app.route('/')
def home():
    return sub_category.to_html()

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
