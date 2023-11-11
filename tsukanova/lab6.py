from flask import Flask, request, render_template, Response
from sklearn import tree
import pandas as pd
import csv
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask('__name__')

df = pd.read_csv('csv_files/for_tree.csv')
df.dropna(inplace=True)

x = df.reset_index().iloc[:, 7:]
y = df.reset_index().iloc[:, 6:7]
# print(y)
model = tree.DecisionTreeClassifier(criterion="entropy")
model = model.fit(x.values, y)
# print('predict: ', model.predict([[538, 82]]))


@app.route('/')
def home():
    return render_template("lab6_home.html")


@app.route('/predict',  methods=['GET'])
def predict():

    return render_template("lab6_predict.html")


@app.route('/show_tree')
def show_tree():
    plt.figure()
    tree.plot_tree(model)

    # plt.savefig('./plots/tree.png')

    file = BytesIO()  # создание временного файла
    plt.savefig(file, format='png')
    encoded = base64.b64encode(file.getvalue()).decode('utf-8')  # кодирование
    return render_template("lab6_tree.html", encoded=encoded, score=model.score(x, y).round(2))


def new_data_set():
    data = pd.read_csv('csv_files/jio_mart_items.csv')
    data.dropna(inplace=True)
    data['category_mean_price'] = data['category'].map(df.groupby('category')['price'].mean().round())
    data['sub_category_mean_price'] = data['sub_category'].map(df.groupby('sub_category')['price'].mean().round())
    sub_categories_list = data['sub_category'].drop_duplicates().tolist()
    new_df = data.iloc[0:1]
    for i in range(len(sub_categories_list)):
        new = data[data['sub_category'] == sub_categories_list[i]].head(3)
        new_df = pd.concat([new_df, new], ignore_index=True)

    # new_df['category_mean_price'] = data['category'].map(data.groupby('category')['price'].mean().round())
    # new_df['sub_category_mean_price'] = data['sub_category'].map(data.groupby('sub_category')['price'].mean().round())

    new_df.to_csv('csv_files/for_tree.csv')


if __name__ == '__main__':
    # new_data_set()
    app.run(debug=True, threaded=True)