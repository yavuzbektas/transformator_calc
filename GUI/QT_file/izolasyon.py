# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'izolasyon.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(309, 325)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 291, 311))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(10, 50, 91, 25))
        self.doubleSpinBox.setValue(0.190000000000000)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 211, 16))
        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(10, 110, 91, 25))
        self.doubleSpinBox_2.setValue(0.190000000000000)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 261, 16))
        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setGeometry(QRect(10, 170, 91, 25))
        self.doubleSpinBox_3.setValue(0.190000000000000)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 150, 291, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 200, 111, 16))
        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setGeometry(QRect(40, 220, 91, 25))
        self.doubleSpinBox_4.setValue(0.190000000000000)
        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setGeometry(QRect(40, 280, 91, 25))
        self.doubleSpinBox_5.setValue(0.190000000000000)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 260, 111, 16))
        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setGeometry(QRect(160, 50, 51, 25))
        self.doubleSpinBox_6.setDecimals(0)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(121, 53, 31, 16))
        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setGeometry(QRect(160, 110, 51, 25))
        self.doubleSpinBox_7.setDecimals(0)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(121, 113, 31, 16))
        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setGeometry(QRect(160, 170, 51, 25))
        self.doubleSpinBox_8.setDecimals(0)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(121, 173, 31, 16))
        self.pushButton_sec = QPushButton(self.groupBox)
        self.pushButton_sec.setObjectName(u"pushButton_sec")
        self.pushButton_sec.setGeometry(QRect(210, 260, 80, 41))
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 200, 31, 22))
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 260, 31, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u0130zolasyon", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Primer Kademe Aras\u0131 \u0130zolasyon", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sekonder (VA) Kademe Aras\u0131 \u0130zolasyon", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Primer - Sekonder Aras\u0131 \u0130zolasyon", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Ekran \u0130zolasyon", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ekstra \u0130zolasyon", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Tur : ", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Tur : ", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Tur : ", None))
        self.pushButton_sec.setText(QCoreApplication.translate("Dialog", u"Kaydet", None))
        self.checkBox.setText("")
        self.checkBox_2.setText("")
    # retranslateUi

