# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'karkas.ui'
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
        Dialog.resize(865, 529)
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 130, 841, 351))
        self.tableWidget.setFrameShape(QFrame.WinPanel)
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pushButton_sec = QPushButton(Dialog)
        self.pushButton_sec.setObjectName(u"pushButton_sec")
        self.pushButton_sec.setGeometry(QRect(780, 483, 80, 41))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sec.setFont(font)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 0, 751, 80))
        self.groupBox.setFont(font)
        self.lineEdit_ID = QLineEdit(self.groupBox)
        self.lineEdit_ID.setObjectName(u"lineEdit_ID")
        self.lineEdit_ID.setEnabled(False)
        self.lineEdit_ID.setGeometry(QRect(10, 50, 61, 24))
        self.lineEdit_karkas_name = QLineEdit(self.groupBox)
        self.lineEdit_karkas_name.setObjectName(u"lineEdit_karkas_name")
        self.lineEdit_karkas_name.setGeometry(QRect(80, 50, 161, 24))
        self.lineEdit_karkas_name.setClearButtonEnabled(True)
        self.doubleSpinBox_karkas_en = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_karkas_en.setObjectName(u"doubleSpinBox_karkas_en")
        self.doubleSpinBox_karkas_en.setEnabled(True)
        self.doubleSpinBox_karkas_en.setGeometry(QRect(250, 50, 71, 25))
        self.doubleSpinBox_karkas_en.setMaximum(9999.989999999999782)
        self.doubleSpinBox_karkas_boy = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_karkas_boy.setObjectName(u"doubleSpinBox_karkas_boy")
        self.doubleSpinBox_karkas_boy.setEnabled(True)
        self.doubleSpinBox_karkas_boy.setGeometry(QRect(330, 50, 71, 25))
        self.doubleSpinBox_karkas_boy.setMaximum(9999.989999999999782)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 55, 16))
        self.label.setFont(font)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 30, 151, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 30, 55, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 30, 55, 16))
        self.label_4.setFont(font)
        self.lineEdit_karkas_ozellik_1 = QLineEdit(self.groupBox)
        self.lineEdit_karkas_ozellik_1.setObjectName(u"lineEdit_karkas_ozellik_1")
        self.lineEdit_karkas_ozellik_1.setGeometry(QRect(410, 50, 161, 24))
        self.lineEdit_karkas_ozellik_1.setClearButtonEnabled(True)
        self.lineEdit_karkas_ozellik_2 = QLineEdit(self.groupBox)
        self.lineEdit_karkas_ozellik_2.setObjectName(u"lineEdit_karkas_ozellik_2")
        self.lineEdit_karkas_ozellik_2.setGeometry(QRect(580, 50, 161, 24))
        self.lineEdit_karkas_ozellik_2.setClearButtonEnabled(True)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 30, 55, 16))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(580, 30, 55, 16))
        self.label_7.setFont(font)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 90, 150, 30))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(250, 90, 160, 30))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 97, 81, 16))
        self.label_5.setFont(font)
        self.pushButton_ara = QPushButton(Dialog)
        self.pushButton_ara.setObjectName(u"pushButton_ara")
        self.pushButton_ara.setGeometry(QRect(420, 90, 80, 31))
        self.pushButton_ara.setFont(font)
        self.pushButton_kaydet = QPushButton(Dialog)
        self.pushButton_kaydet.setObjectName(u"pushButton_kaydet")
        self.pushButton_kaydet.setGeometry(QRect(780, 20, 80, 41))
        self.pushButton_kaydet.setFont(font)
        self.pushButton_sil = QPushButton(Dialog)
        self.pushButton_sil.setObjectName(u"pushButton_sil")
        self.pushButton_sil.setGeometry(QRect(780, 70, 80, 41))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        self.pushButton_sil.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Karkas Ad\u0131", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"En", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Boy", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Ozellik-1", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Ozellik-2", None));
        self.pushButton_sec.setText(QCoreApplication.translate("Dialog", u"Sec", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Secilen", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Karkas Ad\u0131", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"En", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Boy", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Ozellik-1", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Ozellik-2", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"(En)x(Boy)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Karkas Ad\u0131", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"En", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Boy", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Diger", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"Filitre :", None))
        self.pushButton_ara.setText(QCoreApplication.translate("Dialog", u"Ara", None))
        self.pushButton_kaydet.setText(QCoreApplication.translate("Dialog", u"Kaydet", None))
        self.pushButton_sil.setText(QCoreApplication.translate("Dialog", u"Sil", None))
    # retranslateUi

