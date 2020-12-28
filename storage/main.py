from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from storage.main_win import Ui_MainWindow as MainW
import sqlite3


class MainWindow(QMainWindow, MainW):
    def __init__(self, path):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Главное окно")
        self.path = path

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.update_table()

    def update_table(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""select id_products, title_products, pet, type, count from products""").fetchall()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.setItem(i, 2, QTableWidgetItem())
            self.tableWidget.setItem(i, 3, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(self.data[i][1])
            self.tableWidget.item(i, 1).setText(str(self.data[i][2]))
            self.tableWidget.item(i, 2).setText(str(self.data[i][3]))
            self.tableWidget.item(i, 3).setText(str(self.data[i][4]))

        self.pushButton_purchase.clicked.connect(self.purchase)
        self.pushButton_sell.clicked.connect(self.sell)

    def sell(self):
        from storage.sell import SellWindow
        self.win = SellWindow(self.path)
        self.win.show()
        self.close()

    def purchase(self):
        from session_5.main_5 import UI_Task5
        self.win = UI_Task5(self.path)
        self.win.show()
        self.close()

    def closeEvent(self, event):
        from main import Window
        self.win = Window()
        self.win.show()
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
