from flask import Flask, render_template
import pandas as pd
from pretty_html_table import build_table

app = Flask(__name__)
data = pd.read_csv('jio_mart_items.csv')
data.dropna(inplace=True)
data.drop_duplicates(inplace = True)
    

# print(data.agg({'price': ['max']}))
# print(data['price'].max())
#одно макс или мин или средн:
# print(data.loc[data['price'].idxmax()])
#data.describe()

description = 'В наборе данных хранить информации о продуктах JIO'

task1 = 'Минимальная, максимальная, средняя цена в разрезе категорий'
task2 = 'Минимальная, максимальная, средняя цена в разрезе подкатегорий'
task3 = 'Минимальная, максимальная, средняя цена за килограмм'


@app.route('/')
def home():
    
    
    html_task1 = """"" 
    <div class="container mt-4">
          <div class="card">
                <h1 class="text-center"> {task} </h1>
                <br>
                <h5 class="text-center">
                По проанализированным данным можно сделать вывод, что самая дешевая категория - продовольственные довары,
                самая дорогая категория - электроника
                </h5>
                <div class='container mt-4'>
                    <div class='table align-middle table-bordered'>
                        {category}
                    </div>
                </div>
          </div>
        </div>
    """""
    
    html_task2 = """""
    <div class="container mt-4">
          <div class="card">
                <h1 class="text-center"> {task} </h1>
                <br>
                <h5 class="text-center">
                По проанализированным данным можно сделать вывод, что 
                самая дешевая подкатегория - {min},
                самая дорогая подкатегория - {max}
                </h5>
                <div class="container mt-4">
                    <div class="table align-middle table-bordered">
                        {sub_category}
                    </div>
                </div>
          </div>
        </div>
    """""
    
    html_task3 = """""
    <div class="container mt-4">
          <div class="card">
                <h1 class="text-center"> {task} </h1>
                <div class="container mt-4">
                    <div class="table align-middle table-bordered">
                        {one_kg}
                    </div>
                </div>
          </div>
        </div>
    """""

    category = data.groupby(['category']).agg({'price': ['min', 'max', 'mean']}).reset_index()
    category.columns = ['Категории', 'Минимальная цена', 'Максимальная цена', 'Средняя цена']


    sub_category = data.groupby(['sub_category']).agg({'price': ['min', 'max', 'mean']}).reset_index()
    sub_category.columns = ['Подкатегории', 'Минимальная цена', 'Максимальная цена', 'Средняя цена']
    sub_category_max = sub_category.loc[sub_category['Средняя цена'].idxmax()]
    sub_category_min = sub_category.loc[sub_category['Средняя цена'].idxmin()]  
    
    
    one_kg = data[data['items'].str.contains("1 kg") == True].agg({'price': ['min', 'max', 'mean']}).reset_index()
    one_kg.columns = ['Критерий:', 'Результат:']
    
    return render_template("lab2.html") \
        + html_task3.format(task=task3, one_kg=one_kg.to_html(
        classes='table-sm table align-middle table-bordered',justify='center')) \
        + html_task1.format(task=task1, category=category.to_html(
        classes='table-sm table align-middle table-bordered',justify='center')) \
        + html_task2.format(task=task2,min=sub_category_min['Подкатегории'], 
                            max=sub_category_max['Подкатегории'], 
                            sub_category=sub_category.to_html(
        classes='table-sm table align-middle table-bordered',justify='center'))



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
