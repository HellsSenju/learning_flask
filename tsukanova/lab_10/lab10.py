import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

from Model import Model
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
import sys
from typing import List
from formScores import Ui_MainWindow
from plot import Ui_Dialog


class Lab10(QMainWindow):
    def __init__(self):
        super(Lab10, self).__init__()
        self.scores: List[Model] = []

        self.ui = Ui_MainWindow(self.scores)
        self.ui.setupUi(self)
        self.ui.pushButton_confirm.clicked.connect(self.open_result_window)

    def open_result_window(self):
        # если оценки не введены берутся оценки по умолчанию
        if self.ui.listWidget.count() == 0:
            self.scores.append(Model("Ниже среднего", 15, 30, 45))
            self.scores.append(Model("Средняя", 35, 50, 70))
            self.scores.append(Model("Выше среднего", 60, 80, 90))

        self.new_window = QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()


if __name__ == '__main__':
    y = [0, 1, 0]
    x1 = [15, 30, 45]
    x2 = [35, 50, 70]
    x3 = [60, 80, 90]
    plt.figure(figsize=(12, 7))
    plt.axis([0, 100, 0, 1])

    plt.plot(x1, y, c='r', label='Ниже среднего')
    plt.plot(x2, y, c='b', label='Средняя')
    plt.plot(x3, y, c='g', label='Выше среднего')
    plt.legend()
    plt.show()


    # app = QApplication(sys.argv)
    # window = Lab10()
    # window.show()
    #
    # sys.exit(app.exec())
