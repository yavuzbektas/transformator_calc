# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'genel_param.ui'
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
        Dialog.resize(526, 98)
        self.pushButton_sec = QPushButton(Dialog)
        self.pushButton_sec.setObjectName(u"pushButton_sec")
        self.pushButton_sec.setGeometry(QRect(440, 30, 80, 51))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sec.setFont(font)
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 0, 421, 91))
        self.groupBox_3.setFont(font)
        self.doubleSpinBox_sac = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_sac.setObjectName(u"doubleSpinBox_sac")
        self.doubleSpinBox_sac.setGeometry(QRect(100, 30, 101, 25))
        self.doubleSpinBox_sac.setFont(font)
        self.doubleSpinBox_sac.setLayoutDirection(Qt.LeftToRight)
        self.doubleSpinBox_sac.setAutoFillBackground(False)
        self.doubleSpinBox_sac.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_sac.setMaximum(7.000000000000000)
        self.doubleSpinBox_sac.setSingleStep(0.050000000000000)
        self.doubleSpinBox_sac.setValue(0.500000000000000)
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 30, 71, 20))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 30, 51, 20))
        self.label_5.setLayoutDirection(Qt.RightToLeft)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_gauss = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_gauss.setObjectName(u"doubleSpinBox_gauss")
        self.doubleSpinBox_gauss.setGeometry(QRect(260, 30, 71, 25))
        self.doubleSpinBox_gauss.setFont(font)
        self.doubleSpinBox_gauss.setLayoutDirection(Qt.LeftToRight)
        self.doubleSpinBox_gauss.setAutoFillBackground(False)
        self.doubleSpinBox_gauss.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_gauss.setDecimals(0)
        self.doubleSpinBox_gauss.setMaximum(99999.000000000000000)
        self.doubleSpinBox_gauss.setSingleStep(250.000000000000000)
        self.doubleSpinBox_gauss.setValue(10500.000000000000000)
        self.doubleSpinBox_frekans = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_frekans.setObjectName(u"doubleSpinBox_frekans")
        self.doubleSpinBox_frekans.setGeometry(QRect(100, 60, 101, 25))
        self.doubleSpinBox_frekans.setFont(font)
        self.doubleSpinBox_frekans.setLayoutDirection(Qt.LeftToRight)
        self.doubleSpinBox_frekans.setAutoFillBackground(False)
        self.doubleSpinBox_frekans.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_frekans.setValue(50.000000000000000)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 60, 61, 20))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 59, 51, 20))
        self.label_7.setLayoutDirection(Qt.RightToLeft)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_c = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_c.setObjectName(u"doubleSpinBox_c")
        self.doubleSpinBox_c.setGeometry(QRect(260, 59, 71, 25))
        self.doubleSpinBox_c.setFont(font)
        self.doubleSpinBox_c.setLayoutDirection(Qt.LeftToRight)
        self.doubleSpinBox_c.setAutoFillBackground(False)
        self.doubleSpinBox_c.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_c.setMaximum(15.000000000000000)
        self.doubleSpinBox_c.setValue(7.000000000000000)
        self.doubleSpinBox_c2 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_c2.setObjectName(u"doubleSpinBox_c2")
        self.doubleSpinBox_c2.setEnabled(False)
        self.doubleSpinBox_c2.setGeometry(QRect(340, 60, 71, 25))
        self.doubleSpinBox_c2.setFont(font)
        self.doubleSpinBox_c2.setLayoutDirection(Qt.LeftToRight)
        self.doubleSpinBox_c2.setAutoFillBackground(False)
        self.doubleSpinBox_c2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_c2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_c2.setValue(7.000000000000000)
        self.doubleSpinBox_gauss2 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_gauss2.setObjectName(u"doubleSpinBox_gauss2")
        self.doubleSpinBox_gauss2.setEnabled(False)
        self.doubleSpinBox_gauss2.setGeometry(QRect(340, 30, 71, 25))
        self.doubleSpinBox_gauss2.setFont(font)
        self.doubleSpinBox_gauss2.setLayoutDirection(Qt.LeftToRight)
        self.doubleSpinBox_gauss2.setAutoFillBackground(False)
        self.doubleSpinBox_gauss2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_gauss2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_gauss2.setDecimals(0)
        self.doubleSpinBox_gauss2.setMaximum(9999999.000000000000000)
        self.doubleSpinBox_gauss2.setValue(10500.000000000000000)
        self.label_113 = QLabel(self.groupBox_3)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(350, 10, 61, 20))
        self.label_113.setLayoutDirection(Qt.RightToLeft)
        self.label_113.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_sec.setText(QCoreApplication.translate("Dialog", u"SEC", None))
        self.groupBox_3.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Sac(mm)", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Gauss:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Frekans", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"C", None))
        self.label_113.setText(QCoreApplication.translate("Dialog", u"\u00d6nerilen:", None))
    # retranslateUi

