# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_5.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 366)
        MainWindow.setMinimumSize(QtCore.QSize(732, 366))
        MainWindow.setMaximumSize(QtCore.QSize(732, 366))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Clean SemiCondensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Clean Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 72, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Clean Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 691, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(20, 330, 75, 23))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(640, 330, 75, 23))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(110, 330, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_count = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_count.setGeometry(QtCore.QRect(200, 330, 75, 23))
        self.pushButton_count.setObjectName("pushButton_count")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Покупка"))
        self.label_2.setText(_translate("MainWindow", "Итог:"))
        self.label_3.setText(_translate("MainWindow", "0,00"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Количество"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Стоимость"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_close.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_count.setText(_translate("MainWindow", "Рассчитать"))