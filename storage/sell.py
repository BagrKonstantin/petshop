from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from storage.sell_win import Ui_MainWindow
import sqlite3


class SellWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Главное окно")
        self.path = path
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def closeEvent(self, event):
        from storage.main import MainWindow
        self.win = MainWindow("bd.db")
        self.win.show()
        self.close()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = SellWindow("bd.db")
    mainWindow.show()
    sys.exit(app.exec())