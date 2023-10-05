from flask import Flask, request, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)
data = pd.read_csv('jio_mart_items.csv')
data.dropna(inplace=True)

# print(data[ data['category'] == 'Groceries']['items'].head())


max = data.agg({'price' : 'max'})
# max = data.groupby(['category']).agg({'price' : 'max'})
# max.rename(columns={'price' : 'max'}, inplace = True)
print(max)
print(max.axes[0])
print(max.axes[0].values) # закинуть в шаблон



# df = pd.DataFrame([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]],
#                   columns=['A', 'B', 'C'])

# print(df.agg(['min']))

description = 'В наборе данных хранить информации о продуктах JIO'

task1 = 'Минимальная, максимальная, средняя цена в разрезе категорий'
task2 = 'Минимальная, максимальная, средняя цена в разрезе категорий'
task3 = 'Минимальная, максимальная, средняя цена за килограмм'

@app.route('/')
def home():
    return max.to_html()

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
