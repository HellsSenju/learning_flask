# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog, pixmap: QPixmap):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        h_pixmap = pixmap.height()
        w_pixmap = pixmap.width()
        Dialog.resize(w_pixmap, h_pixmap)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, w_pixmap, h_pixmap))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setGeometry(QRect(0, 0, w_pixmap, h_pixmap))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label.setText("")
    # retranslateUi

