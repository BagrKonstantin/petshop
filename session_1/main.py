from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from session_1.window_1 import Ui_MainWindow
from session_1.save_window import Ui_MainWindow as SaveWin
import sqlite3


class Save(QMainWindow, SaveWin):
    def __init__(self, path):
        super(Save, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path
        self.pushButton_save.clicked.connect(self.save_data)

    def save_data(self):
        try:
            title = str(self.lineEdit_title.text())
            pet = str(self.comboBox_animal.currentText())
            type_p = str(self.comboBox_type.currentText())
            p_price = float(self.lineEdit_purchasing_price.text())
            r_price = float(self.lineEdit_retail_price.text())
            description = str(self.textBrowser.toPlainText())
            print(title, pet, type_p, description, p_price, r_price)

            con = sqlite3.connect(self.path)
            cur = con.cursor()
            cur.execute(
                """insert into products (title_products, pet, type, description, purchase_price, retail_price) VALUES 
                    ("{}", "{}", "{}", "{}", {}, {})""".format(
                    title, pet, type_p, description, p_price, r_price))
            con.commit()
            con.close()
        except Exception as err:
            print(err)


class Win1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(Win1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('enter data')
        self.path = path

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""Select id_products, title_products, pet, type, description 
                                    from products""").fetchall()
        con.close()

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.update_table()
        self.pushButton_update.clicked.connect(self.update_data)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_update.clicked.connect(self.update_data)

    def update_data(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute(
            """Select id_products, title_products, pet, type, description from products""").fetchall()
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

    def add(self):
        self.win = Save(self.path)
        self.win.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Win1("../bd.db")
    mainWindow.show()
    sys.exit(app.exec())
