from main_window_1 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3


class UI_Task1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Task1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Товары')

        self.path = path
        self.data = self.get_data()

        self.t = 1

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_close.clicked.connect(self.close)

    def update_list(self):
        pass

    def get_data(self):
        pass

    def add(self):
        n = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(n + 1)

        combobox = QtWidgets.QComboBox()
        combobox.addItems(["Кошки", "Собаки", "Рыбы и рептилии", "Грызуны", "Птицы", "Другое"])
        self.tableWidget.setCellWidget(n, 1, combobox)

        combobox2 = QtWidgets.QComboBox()
        combobox2.addItems(["Еда", "Домики и утварь", "Одежда", "Игрушки", "Уход"])
        self.tableWidget.setCellWidget(n, 2, combobox2)

    def save(self):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task1("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
