from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from session_1.window_1 import Ui_MainWindow
from session_1.save_window import Ui_MainWindow as SaveWin
import sqlite3


class Win6(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(Win6, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Товары')
        self.path = path
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.update_data()

    def update_data(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute(
            """select id_product from purchases""").fetchall()
        for i in range(len(self.data)):
            prod_id = self.data[i][0]
            self.count = cur.execute("""select sum(count) from purchases where purchases.id_product = {}""".format(prod_id))
            name = cur.execute("""select title_products from products where id_products= {}""".format(prod_id))
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(name)
            self.tableWidget.item(i, 1).setText(str(self.count))

    def update_table(self):
        self.tableWidget.setRowCount(0)
        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(self.data[i][1])
            self.tableWidget.item(i, 1).setText(str(self.data[i][2]))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Win6("C:/Users/USER/PycharmProjects/petshop/session_5/bd.db")
    mainWindow.show()
    sys.exit(app.exec())
