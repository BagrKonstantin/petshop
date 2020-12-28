from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3
from session_4.save_deal import Ui_MainWindow


class Deal(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Продажа")
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.products = self.curs.execute('select title_products from products').fetchall()
        self.products = [j for i in self.products for j in i]
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_count_price.clicked.connect(self.count_price)
        self.client_name.textChanged.connect(self.check_discount)
        self.pushButton_save.clicked.connect(self.save)
        self.discount = 0

    def add(self):
        n = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(n + 1)

        combobox = QtWidgets.QComboBox()
        combobox.addItems(self.products)
        self.tableWidget.setCellWidget(n, 0, combobox)

        try:
            self.tableWidget.setItem(n, 2, QTableWidgetItem())
            self.tableWidget.item(n, 2).setText('1')

        except Exception as ex:
            print(ex)

        try:
            combobox.currentTextChanged.connect(self.count_price)
        except Exception as ex:
            print(ex)

        self.count_price(combobox.currentText())

    def save(self):
        for i in range(self.tableWidget.rowCount()):
            try:
                prod_id = self.curs.execute("""select id_products from products where title_products = '{}' """.format(
                    self.tableWidget.cellWidget(i, 0).currentText())).fetchone()[0]
                self.count = float(self.tableWidget.item(i, 2).text())
                self.curs.execute(
                    """insert into sales_details (id_products, price,  amount, total) values (?, ?, ?, ?)""",
                    (prod_id, self.price, self.count, self.count * self.price))
                self.curs.execute(
                    """update products set count = count + {} where id_products = {}""".format(self.count, prod_id))
                self.conn.commit()
                self.curs.execute("""insert into sales (id_customer) values(?)""", (self.client_name))
            except Exception as ex:
                print(ex)
        try:
            QMessageBox.information(self, "Успех!", "Данные успешно сохранены", QMessageBox.Ok)
        except Exception as er:
            print(er)

    def count_price(self, combobox):
        print('ok')
        self.total = 0.0
        for i in range(self.tableWidget.rowCount()):
            try:
                # self.price = self.cur.execute(
                #     '''select purchase_price from products where title_products="{}"'''.format(self.combobox.currentText())).fetchone()[0]
                self.price = \
                    self.curs.execute("""select retail_price from products where title_products='{}'""".format(
                        self.tableWidget.cellWidget(i, 0).currentText())).fetchone()[0]

                self.tableWidget.setItem(i, 1, QTableWidgetItem())
                self.tableWidget.item(i, 1).setText(str(self.price))
            except Exception as ex:
                print(ex)

            try:
                self.tableWidget.setItem(i, 3, QTableWidgetItem())
                self.count = float(self.tableWidget.item(i, 2).text())
                self.s = self.tableWidget.item(i, 3).setText(
                    str(float(self.tableWidget.item(i, 1).text()) * self.count))
                self.total += float(self.tableWidget.item(i, 3).text())
            except Exception as ex:
                print(ex)
        try:
            self.sum.setText(str(self.total - (self.total * self.discount)))
            print((self.total * self.discount))
        except Exception as er:
            print(er)

    def check_discount(self):
        try:
            status = self.curs.execute("""select title_category from customers where title_customer = "{}" """.format(
                self.client_name.text())).fetchone()[0]
            if status == "Хороший клиент":
                self.discount = 0
            elif status == "Супер клиент":
                self.discount = 0.05
            elif status == " Супер-пупер клиент":
                self.discount = 0.1
            self.sale.setText(str(self.discount * 100) + '%')
        except Exception as er:
            pass
