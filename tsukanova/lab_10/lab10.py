import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

from Model import Model
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel
from PySide6.QtGui import QPixmap
import sys
from typing import List
from formScores import Ui_MainWindow
from plot import Ui_Dialog


class Lab10(QMainWindow):
    def __init__(self):
        super(Lab10, self).__init__()
        self.scores: List[Model] = []
        self.colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

        self.ui = Ui_MainWindow(self.scores)
        self.ui.setupUi(self)

        # коннекты
        self.ui.pushButton_add.clicked.connect(self.add_score)
        self.ui.pushButton_del.clicked.connect(self.del_score)
        self.ui.pushButton_confirm.clicked.connect(self.open_result_window)

    def add_score(self):
        self.scores.append(Model(self.ui.lineEdit_name.text(),
                                 int(self.ui.lineEdit_a.text()),
                                 int(self.ui.lineEdit_b.text()),
                                 int(self.ui.lineEdit_c.text())
                                 ))
        self.ui.listWidget.addItem(
            f'{self.ui.lineEdit_name.text()} a={self.ui.lineEdit_a.text()}, b={self.ui.lineEdit_b.text()}, c={self.ui.lineEdit_c.text()}')
        self.ui.kol += 1
        self.ui.set_input()

    def del_score(self):
        item = self.ui.listWidget.currentItem().text().split()[0]
        self.scores.remove([i for i in self.scores if i.name == item][0])
        self.update_list_widget()

    def update_list_widget(self):
        self.ui.listWidget.clear()
        for item in self.scores:
            self.ui.listWidget.addItem(f'{item.name} a={item.a}, b={item.b}, c={item.c}')

    def clear_scores(self):
        self.ui.listWidget.clear()
        self.scores.clear()

    def reset_param(self):
        self.ui.kol = 1
        self.clear_scores()
        self.ui.set_input()

    def open_result_window(self):
        if len(self.scores) > 10:
            self.reset_param()
            return

        # если оценки не введены берутся оценки по умолчанию
        if self.ui.listWidget.count() == 0:
            self.scores.append(Model("Ниже среднего", 15, 30, 45))
            self.scores.append(Model("Средняя", 35, 50, 70))
            self.scores.append(Model("Выше среднего", 60, 80, 90))

        y = [0, 1, 0]
        plt.figure(figsize=(12, 7))
        min = 1000000
        max = -1000000
        c = 0
        for item in self.scores:
            if item.a < min:
                min = item.a
            if item.c > max:
                max = item.c

            plt.plot(item.get_props(), y, color=self.colors[c], label=item.name)
            c += 1

        plt.axis([min - 10, max + 10, 0, 1])
        plt.title("Оценки загруженности сети")
        plt.xlabel("Загруженность сети")
        plt.ylabel("Степень принадлежности")
        plt.legend()

        plt.savefig('plot.png')
        plt.clf()

        self.new_window = QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window, QPixmap("plot.png"))
        self.new_window.show()
        self.new_window.rejected.connect(self.closed_dialog)

    def closed_dialog(self):
        self.reset_param()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Lab10()
    window.show()

    sys.exit(app.exec())
