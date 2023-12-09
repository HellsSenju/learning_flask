from flask import Flask, request, render_template
import pandas as pd
import math

app = Flask('__name__')

df = pd.read_csv('csv_files/for_tree_1.csv')
df.dropna(inplace=True)
df.drop_duplicates(subset=['price'], inplace=True)


def get_entropy(data):
    entropy = 0
    values = data.value_counts()

    for value_count in values:
        p = value_count / len(data)
        entropy -= p * math.log2(p)

    return entropy


def get_best_attribute(data, attributes):
    entropies = {}

    for attribute in attributes:
        attribute_entropy = get_entropy(data[attribute])
        entropies[attribute] = attribute_entropy

    best_attribute = min(entropies, key=entropies.get)
    return best_attribute


def build_decision_tree(data, target_column, attributes):
    # одно уникальное
    if len(data[target_column].unique()) == 1:
        return data[target_column].iloc[0]

    # больше нет атрибутов
    if len(attributes) == 0:
        return data[target_column].mode().iloc[0]

    # атрибут с наименьшей энтропией
    best_attribute = get_best_attribute(data, attributes)
    # оставшиеся атрибуты
    remaining_attributes = [attr for attr in attributes if attr != best_attribute]

    tree = {best_attribute: {}}

    for value in data[best_attribute].unique():
        subset = data[data[best_attribute] == value]
        if len(subset) == 0:
            tree[best_attribute][value] = data[target_column].mode().iloc[0]
        else:
            tree[best_attribute][value] = build_decision_tree(subset, target_column, remaining_attributes)

    return tree


def predict(tree, row, target):
    # если tree не dictionary
    if not isinstance(tree, dict):
        return tree
    else:
        attribute = list(tree.keys())[0]
        value = row.get(attribute)
        subtree = tree[attribute].get(value, target)
        return predict(subtree, row, target)


def predict_one(tree, attributes, targets):
    if not isinstance(tree, dict):
        return tree

    if len(tree.keys()) == 1:
        attr = attributes[0]
        tree = tree[attr]
        attributes.remove(attr)

    target = targets[0]
    targets.remove(target)
    tree = tree[target]
    return predict_one(tree, attributes, targets)


_attributes = ['category', 'sub_category']
_target_column = 'price'
decision_tree = build_decision_tree(df, _target_column, _attributes)


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
def prediction():
    category = ""
    sub_category = ""
    if request.args['sub_groceries'] is not None:
        category = "Groceries"
        sub_category = request.args['sub_groceries']

    elif request.args['sub_fashion'] is not None:
        category = "Fashion"
        sub_category = request.args['sub_fashion']

    elif request.args['sub_beauty'] is not None:
        category = "Beauty"
        sub_category = request.args['sub_beauty']

    elif request.args['sub_jewellery'] is not None:
        category = "Jewellery"
        sub_category = request.args['sub_jewellery']

    if category == "" and sub_category == "":
        print("1")
        return render_template("not_found.html")

    if decision_tree is None:
        print("2")
        return render_template("not_found.html")

    print(category)
    print(sub_category)
    return render_template('lab6_predict.html',
                           category=category,
                           sub_category=sub_category,
                           price=predict_one(decision_tree, _attributes.copy(), [category, sub_category]))


@app.route('/show_tree')
def show_tree():
    results = []
    for index, row in df.iterrows():
        _predict = predict(decision_tree, row, df['price'].mode().iloc[0])
        results.append(f"Actual: {row[_target_column]}, Predicted: {_predict}")

    return render_template('lab6_tree.html', results=results)


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
