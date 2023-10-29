from flask import Flask, render_template, request
import pandas as pd
from bloomFilter import BloomFilter
from pandas import DataFrame

app = Flask(__name__)

data = pd.read_csv('csv_files/jio_mart_items.csv')
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

keys = (data['category'].drop_duplicates().tolist() + data['sub_category'].drop_duplicates().tolist() +
        data['items'].value_counts().head(30).index.tolist())

bf = BloomFilter(len(keys) * 2, len(keys))
for i in range(len(keys)):
    bf.add_to_filter(keys[i])


@app.route('/')
def home():
    return render_template("lab4_home.html")


@app.route('/bloomFilter', methods=['GET'])
def bloom_filter():
    keyword = request.args['word']
    if not bf.check_is_not_in_filter(keyword):
        html = """
        <div class="container mt-4">
            <div class="container mt-4">
                <div>
                    {table}
                </div>
            </div>
        </div>
        """

        res = DataFrame
        col = data.columns.tolist()
        for j in range(len(col)):
            if not data[data[col[j]] == keyword].empty:
                res = data[data[col[j]] == keyword]
                break

        if not res.empty:
            return render_template("lab4.html", keyword=keyword) \
                + html.format(table=res.to_html(
                            classes='table table-sm table-striped align-middle table-bordered',
                            justify='center'))

    else:
        return render_template("not_found.html", keyword=keyword)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
