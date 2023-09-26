from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/diapason', methods=['GET'])
def diapason():
    values = request.args
    data = pd.read_csv('jio_mart_items_noEmpty.csv', sep=',')
    description = 'В наборе данных хранить информации о продуктах JIO'\
        'С помощью этих данных можно проанализировать, какие категории товаров содержать наиболее дорогие (дешевые) товары,' \
        'а так же категории с наибольшим(наименьшим) количеством продукции'   

    column_info = str(data.dtypes)
    
    line_count = len(data.axes[0])
    column_count = len(data.axes[1])
    #пустые ячейки
    empty_count = data.isna().sum()
    #заполненные
    fill_count = data.count()
    
    
    from_line = int(values['from_line']) - 1
    print('from_line' + values['from_line'])
    to_line = int(values['to_line'])
    print('to_line'+ values['to_line'])
    
    from_column = int(values['from_column']) - 1
    print('from_column'+ values['from_column'])
    to_column = int(values['to_column'])
    print('to_column'+ values['to_column'])
    
    outputData = data.iloc[from_line: to_line, from_column: to_column].to_html(
        classes='table-sm table align-middle table-bordered',
        justify='center')

    if from_line > to_line | from_column > to_column | to_line > line_count | to_column > column_count:
        return '''<center><h1>Введен некорректный диапазон</h1></center>''' + render_template("home.html")
    else:
        return render_template('view_data.html', 
                    column_info= column_info,
                    line_count = line_count,
                    column_count = column_count,
                    empty_count = empty_count,
                    fill_count = fill_count,
                    description = description
                    ) \
                        + "<div class='container mt-4'><div align='center' class='table table-bordered'>" \
                        + outputData + \
                        "</div></div>"


if __name__ == '__main__':
    app.run(debug=True, threaded=True)