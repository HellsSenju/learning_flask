from flask import Flask, request, render_template
from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import math
from binarytree import tree as Tree, Node


app = Flask('__name__')

df = pd.read_csv('csv_files/for_tree_1.csv')
df.dropna(inplace=True)
df.drop_duplicates(subset=['price'], inplace=True)

x = df.reset_index().iloc[:20, 7:]
y = df.reset_index().iloc[:20, 6:7]


def entropy(_list: list, col: str):
    entropy_ = 0
    for i in categories_list:
        kol = len(df[df[col] == i])
        p = kol / len(df)
        entropy_ += p * math.log(p, 2)

    return -entropy_


categories_list = df['category'].drop_duplicates().tolist()
categories_entropy = entropy(categories_list, 'category')  # энтропия для столбца "категории"

sub_categories_list = df['sub_category'].drop_duplicates().tolist()
sub_categories_entropy = entropy(categories_list, 'category')  # энтропия для столбца "подкатегории"

# for i in categories_list:
#     kol = len(df[df['category'] == i])
#     p = kol / len(df)
#     categories_entropy += p * math.log(p, 2)
#
# categories_entropy = -categories_entropy
# print(categories_entropy)

print(x.values)
model = tree.DecisionTreeClassifier(criterion="entropy")
model = model.fit(x, y)


@app.route('/')
def home():
    sub_groceries = df[df['category'] == 'Groceries']['sub_category'].drop_duplicates().tolist()
    sub_fashion = df[df['category'] == 'Fashion']['sub_category'].drop_duplicates().tolist()
    sub_beauty = df[df['category'] == 'Beauty']['sub_category'].drop_duplicates().tolist()
    sub_jewellery = df[df['category'] == 'Jewellery']['sub_category'].drop_duplicates().tolist()

    return render_template("lab6_home.html",
                           sub_cat=df['sub_category'].drop_duplicates().tolist(),
                           cat=df['category'].drop_duplicates().tolist(),
                           sub_groceries=sub_groceries,
                           sub_fashion=sub_fashion,
                           sub_beauty=sub_beauty,
                           sub_jewellery=sub_jewellery)


@app.route('/predict', methods=['GET'])
def predict():
    category_mean_price = 0
    sub_cat_mean_price = 0

    if request.args['sub_groceries'] is not None:
        sub_groceries = request.args['sub_groceries']
        category_mean_price = df[df['category'] == 'Groceries']["category_mean_price"].drop_duplicates().values[0]
        sub_cat_mean_price = df[df['sub_category'] == sub_groceries]["sub_cat_mean_price"].drop_duplicates().values[0]

    elif request.args['sub_fashion'] is not None:
        sub_fashion = request.args['sub_fashion']
        category_mean_price = df[df['category'] == 'Fashion']["category_mean_price"].drop_duplicates().values[0]
        sub_cat_mean_price = df[df['sub_category'] == sub_fashion]["sub_cat_mean_price"].drop_duplicates().values[0]

    elif request.args['sub_beauty'] is not None:
        sub_beauty = request.args['sub_beauty']
        category_mean_price = df[df['category'] == 'Beauty']["category_mean_price"].drop_duplicates().values[0]
        sub_cat_mean_price = df[df['sub_category'] == sub_beauty]["sub_cat_mean_price"].drop_duplicates().values[0]

    elif request.args['sub_jewellery'] is not None:
        sub_jewellery = request.args['sub_jewellery']
        category_mean_price = df[df['category'] == 'Jewellery']["category_mean_price"].drop_duplicates().values[0]
        sub_cat_mean_price = df[df['sub_category'] == sub_jewellery]["sub_cat_mean_price"].drop_duplicates().values[0]

    if category_mean_price == 0 & sub_cat_mean_price == 0:
        return

    predicted = model.predict([[category_mean_price, sub_cat_mean_price]])
    return render_template("lab6_predict.html",
                           price=predicted[0])


@app.route('/show_tree')
def show_tree():
    plt.figure(figsize=(40, 40))
    tree.plot_tree(model)

    # plt.savefig('./plots/tree_2.png')

    file = BytesIO()  # создание временного файла
    plt.savefig(file, format='png')
    encoded = base64.b64encode(file.getvalue()).decode('utf-8')  # кодирование
    return render_template("lab6_tree.html", encoded=encoded, score=model.score(x, y).round(2))


@app.route('/fit')
def fit():
    srez = df.drop_duplicates(subset=['price'])
    srez = srez.iloc[:20, :]
    srez = srez.drop(['href'], axis=1)
    srez['predict'] = 1
    result = 0

    for index, row in srez[:].iterrows():
        row.predict = model.predict([[row.category_mean_price, row.sub_cat_mean_price]])[0]
        if row.predict == row.price:
            result += 1

    return render_template("lab6_fit.html",
                           result=(result / 20) * 100)


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
