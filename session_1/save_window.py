# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 521)
        MainWindow.setMinimumSize(QtCore.QSize(433, 521))
        MainWindow.setMaximumSize(QtCore.QSize(433, 521))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_title.setGeometry(QtCore.QRect(190, 20, 151, 22))
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.comboBox_animal = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_animal.setGeometry(QtCore.QRect(190, 50, 151, 22))
        self.comboBox_animal.setObjectName("comboBox_animal")
        self.comboBox_animal.addItem("")
        self.comboBox_animal.addItem("")
        self.comboBox_animal.addItem("")
        self.comboBox_animal.addItem("")
        self.comboBox_animal.addItem("")
        self.comboBox_animal.addItem("")
        self.comboBox_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type.setGeometry(QtCore.QRect(190, 90, 151, 22))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.lineEdit_purchasing_price = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_purchasing_price.setGeometry(QtCore.QRect(190, 130, 151, 22))
        self.lineEdit_purchasing_price.setObjectName("lineEdit_purchasing_price")
        self.lineEdit_retail_price = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_retail_price.setGeometry(QtCore.QRect(190, 170, 151, 22))
        self.lineEdit_retail_price.setObjectName("lineEdit_retail_price")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 240, 411, 192))
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 158, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(330, 440, 93, 28))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(10, 440, 93, 28))
        self.pushButton_close.setObjectName("pushButton_close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.label_2.setText(_translate("MainWindow", "Животное"))
        self.label_3.setText(_translate("MainWindow", "Назначение"))
        self.label_4.setText(_translate("MainWindow", "Закупочная цена"))
        self.label_5.setText(_translate("MainWindow", "Розничная цена"))
        self.comboBox_animal.setItemText(0, _translate("MainWindow", "Кошки"))
        self.comboBox_animal.setItemText(1, _translate("MainWindow", "Собаки"))
        self.comboBox_animal.setItemText(2, _translate("MainWindow", "Рыбы и рептилии"))
        self.comboBox_animal.setItemText(3, _translate("MainWindow", "Грызуны"))
        self.comboBox_animal.setItemText(4, _translate("MainWindow", "Птицы"))
        self.comboBox_animal.setItemText(5, _translate("MainWindow", "Другое"))
        self.comboBox_type.setItemText(0, _translate("MainWindow", "Еда"))
        self.comboBox_type.setItemText(1, _translate("MainWindow", "Домики и утварь"))
        self.comboBox_type.setItemText(2, _translate("MainWindow", "Одежда"))
        self.comboBox_type.setItemText(3, _translate("MainWindow", "Игрушки"))
        self.comboBox_type.setItemText(4, _translate("MainWindow", "Уход"))
        self.label_6.setText(_translate("MainWindow", "Описание"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_close.setText(_translate("MainWindow", "Закрыть"))