# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormAddScores.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
from Model import Model
from typing import List


class Ui_MainWindow(object):
    def __init__(self, scores: List[Model]):
        self.kol = 1
        self.scores: List[Model] = scores

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(460, 462)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 111, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(120, 50, 331, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 21, 16))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 100, 21, 20))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 100, 21, 16))
        self.label_4.setFont(font1)
        self.lineEdit_a = QLineEdit(self.centralwidget)
        self.lineEdit_a.setObjectName(u"lineEdit_a")
        self.lineEdit_a.setGeometry(QRect(30, 100, 101, 20))
        self.lineEdit_b = QLineEdit(self.centralwidget)
        self.lineEdit_b.setObjectName(u"lineEdit_b")
        self.lineEdit_b.setGeometry(QRect(190, 100, 101, 20))
        self.lineEdit_c = QLineEdit(self.centralwidget)
        self.lineEdit_c.setObjectName(u"lineEdit_c")
        self.lineEdit_c.setGeometry(QRect(350, 100, 101, 20))
        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(10, 140, 441, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.pushButton_add.setFont(font2)
        self.pushButton_add.setStyleSheet(u"\n"
"background-color: rgb(182, 241, 143);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 400, 31))
        self.label_5.setFont(font)
        self.pushButton_del = QPushButton(self.centralwidget)
        self.pushButton_del.setObjectName(u"pushButton_del")
        self.pushButton_del.setGeometry(QRect(10, 380, 441, 31))
        self.pushButton_del.setFont(font2)
        self.pushButton_del.setStyleSheet(u"background-color: rgb(255, 101, 103);")
        self.pushButton_confirm = QPushButton(self.centralwidget)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setGeometry(QRect(10, 420, 441, 31))
        self.pushButton_confirm.setFont(font2)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 180, 441, 192))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0446\u0435\u043d\u043e\u043a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Название", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"a:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"b:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"c:", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Добавление оценок (максимум 10):", None))
        self.pushButton_del.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u043e\u0446\u0435\u043d\u043a\u0438", None))
        self.set_input()
    # retranslateUi

    def set_input(self):
        # задание значений по умолчанию
        self.lineEdit_name.setText("Оценка_" + str(self.kol))
        self.lineEdit_a.setText("5")
        self.lineEdit_b.setText("10")
        self.lineEdit_c.setText("15")
