from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3
from session_3.window_3 import Ui_MainWindow
from session_3.add_client import Ui_MainWindow as AddClient
import openpyxl


class Client(QMainWindow, AddClient):
    def __init__(self, path):
        super(Client, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Добавить")
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        self.pushButton_close.clicked.connect(self.cls)
        self.pushButton_save.clicked.connect(self.save)

        self.lineEdit_phoneNumber.setInputMask("8(999)9999999")
        status = self.curs.execute("""select title_category from category""").fetchall()
        self.comboBox_status.clear()
        for i in status:
            for j in i:
                self.comboBox_status.addItem(j)

    # def save(self):
    # try:
    #  title = self.lineEdit_surname.text() + self.lineEdit_name.text() + self.lineEdit_otchestvo.text()
    # self.curs.execute("""insert into customers (title_customer, tel_number, )""")
    def save(self):
        try:
            title = self.lineEdit_surname.text() + " " + self.lineEdit_name.text() + " " + self.lineEdit_otchestvo.text()
            status = self.comboBox_status.currentText()
            self.curs.execute("""insert into customers (title_customer, tel_number, title_category) values (?, ?, ?)""",
                              (title, self.lineEdit_phoneNumber.text(), status))
            self.conn.commit()
            self.conn.close()
            self.cls()
        except Exception as er:
            print(er)

    def cls(self):
        self.win = Win3("bd.db")
        self.win.show()
        self.close()


class Win3(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(Win3, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Клиенты")
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_insert.clicked.connect(self.insert)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.update_data()

    def update_data(self):
        self.data = self.curs.execute(
            """Select id_customer, title_customer, tel_number, title_category from customers""").fetchall()
        self.update_table()

    def update_table(self):
        self.tableWidget.setRowCount(0)

        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.setItem(i, 2, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(self.data[i][1])
            self.tableWidget.item(i, 1).setText(self.data[i][2])
            self.tableWidget.item(i, 2).setText(str(self.data[i][3]))

    def add(self):
        try:
            self.win = Client(self.path)
            self.win.show()
            self.close()
        except Exception as er:
            print(er)

    def insert(self):
        try:
            fname = QFileDialog.getOpenFileName(self, '', 'C://')[0]
            wb = openpyxl.load_workbook(fname)

            # печатаем список листов
            sheets = wb.sheetnames

            # получаем активный лист
            sheet = wb.active
            sheet_name = str(sheet).strip('<Worksheet "').strip('">')
            for i in range(1, len(list(sheet.rows))):
                l_name = sheet[str(list(sheet.rows)[i][0]).strip("<Cell '{}'.".format(sheet_name)).strip('>')].value
                f_name = sheet[str(list(sheet.rows)[i][1]).strip("<Cell '{}'.".format(sheet_name)).strip('>')].value
                s_name = sheet[
                    str(list(sheet.rows)[i][2]).strip("<Cell '{}'".format(sheet_name)).strip('.').strip('>')].value
                phone_number = sheet[
                    str(list(sheet.rows)[i][3]).strip("<Cell '{}'".format(sheet_name)).strip('.').strip('>')].value
                status = sheet[
                    str(list(sheet.rows)[i][4]).strip("<Cell '{}'".format(sheet_name)).strip('.').strip('>')].value
                title = l_name + " " + f_name + " " + s_name
                self.curs.execute(
                    """insert into customers (title_customer, tel_number, title_category) values (?, ?, ?)""",
                    (title, phone_number, status))
                self.conn.commit()
                self.update_data()
        except Exception as er:
            print(er)
        self.conn.close()

    def closeEvent(self, event):
        from main import Window
        self.win = Window()
        self.win.show()
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Win3("../bd.db")
    mainWindow.show()
    sys.exit(app.exec())
