from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from session_1.window_1 import Ui_MainWindow
import sqlite3


class Win1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(Win1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""Select id_products, title_products, title_pet, title_type, description from products
                                    join pet p on p.id_pet = products.id_pet
                                    join type t on t.id_type = products.id_type""").fetchall()
        con.close()

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.update_table()

        self.pushButton_update.clicked.connect(self.update_data)

    def update_data(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""Select id_products, title_products, title_pet, title_type, description from products
                                    join pet p on p.id_pet = products.id_pet
                                    join type t on t.id_type = products.id_type""").fetchall()
        con.close()
        self.update_table()

    def update_table(self):
        self.tableWidget.setRowCount(0)

        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.setItem(i, 2, QTableWidgetItem())
            self.tableWidget.setItem(i, 3, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(self.data[i][1])
            self.tableWidget.item(i, 1).setText(self.data[i][2])
            self.tableWidget.item(i, 2).setText(self.data[i][3])
            self.tableWidget.item(i, 3).setText(self.data[i][4])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Win1("../bd.db")
    mainWindow.show()
    sys.exit(app.exec())
