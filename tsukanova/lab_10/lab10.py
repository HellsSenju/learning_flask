import skfuzzy as fuzz
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
    x_qual = np.arange(0, 100, 1)

    lo = fuzz.trimf(x_qual, [15, 30, 45])
    md = fuzz.trimf(x_qual, [35, 50, 70])
    hi = fuzz.trimf(x_qual, [60, 80, 90])

    fig, ax = plt.subplots(nrows=1, figsize=(8, 9))
    ax.plot(x_qual, lo, 'b', linewidth=1.5, label='Ниже среднего')
    ax.plot(x_qual, md, 'g', linewidth=1.5, label='Средняя')
    ax.plot(x_qual, hi, 'r', linewidth=1.5, label='Выше среднего')
    ax.set_title('Загруженность сервера и сети')
    ax.legend()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.tight_layout()

    # app = QApplication(sys.argv)
    # window = Lab10()
    # window.show()
    #
    # sys.exit(app.exec())
