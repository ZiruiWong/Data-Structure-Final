# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sort（原身）.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(781, 548)
        Form.setMinimumSize(QtCore.QSize(781, 548))
        Form.setMaximumSize(QtCore.QSize(781, 548))
        Form.setAutoFillBackground(False)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 721, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(680, 60, 50, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton.setSizeIncrement(QtCore.QSize(75, 50))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(224,124,106);\n"
"    border-radius:5px;\n"
"    color:white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(234,172,91);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(220,83,129);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 120, 791, 431))
        self.label.setStyleSheet("QLabel{\n"
"    border-radius:5px;\n"
"}\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 0, 601, 41))
        self.label_3.setStyleSheet("color:rgb(89,80,107);\n"
"font: 14pt \"Avenir Next Condensed\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 811, 251))
        self.label_2.setStyleSheet("QLabel{\n"
"    background-color: white;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 171, 21))
        self.label_4.setStyleSheet("QLabel{\n"
"    background-color: rgb(145,108,198);\n"
"    font: 14pt \"Heiti SC\";\n"
"    border-radius:10px;\n"
"    color:white\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(120, 40, 71, 21))
        self.spinBox.setMaximum(10000)
        self.spinBox.setProperty("value", 200)
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 70, 561, 41))
        self.label_5.setStyleSheet("QLabel{\n"
"    background-color: rgb(102,135,213);\n"
"    font: 14pt \"Heiti SC\";\n"
"    border-radius:10px;\n"
"    color:white\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(120, 70, 81, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 70, 81, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(390, 70, 81, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(300, 70, 81, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(480, 70, 81, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 40, 171, 21))
        self.label_6.setStyleSheet("QLabel{\n"
"    background-color: rgb(145,108,198);\n"
"    font: 14pt \"Heiti SC\";\n"
"    border-radius:10px;\n"
"    color:white\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(400, 40, 201, 21))
        self.label_7.setStyleSheet("QLabel{\n"
"    background-color: rgb(145,108,198);\n"
"    font: 14pt \"Heiti SC\";\n"
"    border-radius:10px;\n"
"    color:white\n"
"}\n"
"")
        self.label_7.setObjectName("label_7")
        self.comboBox_6 = QtWidgets.QComboBox(Form)
        self.comboBox_6.setGeometry(QtCore.QRect(300, 40, 81, 21))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(Form)
        self.comboBox_7.setGeometry(QtCore.QRect(470, 40, 101, 21))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(200, 70, 21, 16))
        self.label_8.setStyleSheet("color:white")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(290, 70, 21, 16))
        self.label_9.setStyleSheet("color:white")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(380, 70, 21, 16))
        self.label_10.setStyleSheet("color:white")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(470, 70, 21, 16))
        self.label_11.setStyleSheet("color:white")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(380, 90, 21, 16))
        self.label_12.setStyleSheet("color:white")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(470, 90, 21, 16))
        self.label_13.setStyleSheet("color:white")
        self.label_13.setObjectName("label_13")
        self.comboBox_9 = QtWidgets.QComboBox(Form)
        self.comboBox_9.setGeometry(QtCore.QRect(120, 90, 81, 21))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(200, 90, 21, 16))
        self.label_14.setStyleSheet("color:white")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(290, 90, 21, 16))
        self.label_15.setStyleSheet("color:white")
        self.label_15.setObjectName("label_15")
        self.comboBox_10 = QtWidgets.QComboBox(Form)
        self.comboBox_10.setGeometry(QtCore.QRect(210, 90, 81, 21))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_11 = QtWidgets.QComboBox(Form)
        self.comboBox_11.setGeometry(QtCore.QRect(300, 90, 81, 21))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_12 = QtWidgets.QComboBox(Form)
        self.comboBox_12.setGeometry(QtCore.QRect(390, 90, 81, 21))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_13 = QtWidgets.QComboBox(Form)
        self.comboBox_13.setGeometry(QtCore.QRect(480, 90, 81, 21))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.label_2.raise_()
        self.label.raise_()
        self.tableWidget.raise_()
        self.pushButton_4.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.spinBox.raise_()
        self.label_5.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_4.raise_()
        self.comboBox_3.raise_()
        self.comboBox_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.comboBox_6.raise_()
        self.comboBox_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.comboBox_9.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.comboBox_10.raise_()
        self.comboBox_11.raise_()
        self.comboBox_12.raise_()
        self.comboBox_13.raise_()

        self.retranslateUi(Form)
        self.comboBox_2.setCurrentIndex(1)
        self.comboBox_4.setCurrentIndex(3)
        self.comboBox_3.setCurrentIndex(2)
        self.comboBox_5.setCurrentIndex(4)
        self.comboBox_6.setCurrentIndex(1)
        self.pushButton.clicked.connect(Form.sort_data)
        self.pushButton_4.clicked.connect(Form.returnWel)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GKD多关键字排序系统--获得排序结果"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "关键字1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "关键字2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "关键字3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "关键字4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "关键字5"))
        self.pushButton_4.setText(_translate("Form", "返回"))
        self.pushButton.setText(_translate("Form", "测试"))
        self.label_3.setText(_translate("Form", "2020 数据结构大作业    作者: ZZY YBR WZR    version: 1.0.3"))
        self.label_4.setText(_translate("Form", "  数据个数"))
        self.label_5.setText(_translate("Form", "  关键字顺序"))
        self.comboBox.setItemText(0, _translate("Form", "关键字1"))
        self.comboBox.setItemText(1, _translate("Form", "关键字2"))
        self.comboBox.setItemText(2, _translate("Form", "关键字3"))
        self.comboBox.setItemText(3, _translate("Form", "关键字4"))
        self.comboBox.setItemText(4, _translate("Form", "关键字5"))
        self.comboBox_2.setItemText(0, _translate("Form", "关键字1"))
        self.comboBox_2.setItemText(1, _translate("Form", "关键字2"))
        self.comboBox_2.setItemText(2, _translate("Form", "关键字3"))
        self.comboBox_2.setItemText(3, _translate("Form", "关键字4"))
        self.comboBox_2.setItemText(4, _translate("Form", "关键字5"))
        self.comboBox_4.setItemText(0, _translate("Form", "关键字1"))
        self.comboBox_4.setItemText(1, _translate("Form", "关键字2"))
        self.comboBox_4.setItemText(2, _translate("Form", "关键字3"))
        self.comboBox_4.setItemText(3, _translate("Form", "关键字4"))
        self.comboBox_4.setItemText(4, _translate("Form", "关键字5"))
        self.comboBox_3.setItemText(0, _translate("Form", "关键字1"))
        self.comboBox_3.setItemText(1, _translate("Form", "关键字2"))
        self.comboBox_3.setItemText(2, _translate("Form", "关键字3"))
        self.comboBox_3.setItemText(3, _translate("Form", "关键字4"))
        self.comboBox_3.setItemText(4, _translate("Form", "关键字5"))
        self.comboBox_5.setItemText(0, _translate("Form", "关键字1"))
        self.comboBox_5.setItemText(1, _translate("Form", "关键字2"))
        self.comboBox_5.setItemText(2, _translate("Form", "关键字3"))
        self.comboBox_5.setItemText(3, _translate("Form", "关键字4"))
        self.comboBox_5.setItemText(4, _translate("Form", "关键字5"))
        self.label_6.setText(_translate("Form", "  关键字顺序"))
        self.label_7.setText(_translate("Form", "  排列种类"))
        self.comboBox_6.setItemText(0, _translate("Form", "LSD"))
        self.comboBox_6.setItemText(1, _translate("Form", "MSD"))
        self.comboBox_7.setItemText(0, _translate("Form", "shell_sort"))
        self.comboBox_7.setItemText(1, _translate("Form", "radix_10_sort"))
        self.comboBox_7.setItemText(2, _translate("Form", "merge_sort"))
        self.comboBox_7.setItemText(3, _translate("Form", "quick_sort"))
        self.comboBox_7.setItemText(4, _translate("Form", "bubble_sort"))
        self.comboBox_7.setItemText(5, _translate("Form", "insert_sort"))
        self.comboBox_7.setItemText(6, _translate("Form", "heap_sort"))
        self.comboBox_7.setItemText(7, _translate("Form", "radix_101_sort"))
        self.label_8.setText(_translate("Form", "--"))
        self.label_9.setText(_translate("Form", "--"))
        self.label_10.setText(_translate("Form", "--"))
        self.label_11.setText(_translate("Form", "--"))
        self.label_12.setText(_translate("Form", "--"))
        self.label_13.setText(_translate("Form", "--"))
        self.comboBox_9.setItemText(0, _translate("Form", "从大到小"))
        self.comboBox_9.setItemText(1, _translate("Form", "从小到大"))
        self.label_14.setText(_translate("Form", "--"))
        self.label_15.setText(_translate("Form", "--"))
        self.comboBox_10.setItemText(0, _translate("Form", "从大到小"))
        self.comboBox_10.setItemText(1, _translate("Form", "从小到大"))
        self.comboBox_11.setItemText(0, _translate("Form", "从大到小"))
        self.comboBox_11.setItemText(1, _translate("Form", "从小到大"))
        self.comboBox_12.setItemText(0, _translate("Form", "从大到小"))
        self.comboBox_12.setItemText(1, _translate("Form", "从小到大"))
        self.comboBox_13.setItemText(0, _translate("Form", "从大到小"))
        self.comboBox_13.setItemText(1, _translate("Form", "从小到大"))

