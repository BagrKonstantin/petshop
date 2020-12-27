from window_5 import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3


class UI_Task5(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(UI_Task5, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Товары')

        self.path = path
        self.data = self.get_data()

        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()

        self.products = self.cur.execute('select title_products from products').fetchall()
        self.products = [j for i in self.products for j in i]

        self.t = 1

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_count.clicked.connect(self.count_price)

    def get_data(self):
        pass

    def count_price(self, combobox):
        print('ok')
        self.total = 0.0
        for i in range(self.tableWidget.rowCount()):
            try:
                # self.price = self.cur.execute(
                #     '''select purchase_price from products where title_products="{}"'''.format(self.combobox.currentText())).fetchone()[0]
                self.price = \
                    self.cur.execute("""select purchase_price from products where title_products='{}'""".format(
                        self.tableWidget.cellWidget(i, 0).currentText())).fetchone()[0]

                self.tableWidget.setItem(i, 1, QTableWidgetItem())
                self.tableWidget.item(i, 1).setText(str(self.price))
            except Exception as ex:
                print(ex)

            try:
                self.tableWidget.setItem(i, 3, QTableWidgetItem())
                self.tableWidget.item(i, 3).setText(
                    str(float(self.tableWidget.item(i, 1).text()) * float(
                        self.tableWidget.item(i, 2).text())))
            except Exception as ex:
                print(ex)
            self.total += float(self.tableWidget.item(i, 3).text())
        self.label_3.setText(str(self.total))

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

    def check(self):
        to_delete = []
        data = []
        for i in range(self.tableWidget.rowCount()):
            line = []
            for j in range(self.tableWidget.columnCount()):
                if j == 0:
                    cell = self.tableWidget.item(i, j).text()
                    if cell == "":
                        to_delete.append(i)
                        break
                else:
                    cell = self.tableWidget.item(i, j).text()
                    try:
                        cell = int(cell)
                        self.tableWidget.item(i, j).setBackground(QtGui.QColor(255, 255, 255))
                    except Exception:
                        self.tableWidget.item(i, j).setBackground(QtGui.QColor(125, 125, 125))
                line.append(cell)
            if line:
                data.append(line)
        for i in to_delete[::-1]:
            self.tableWidget.removeRow(i)
        return data

    def save(self):
        for i in range(self.tableWidget.rowCount()):
            try:
                prod_id = self.cur.execute("""select id_products from products where title_products = '{}' """.format(
                    self.tableWidget.cellWidget(i, 0).currentText())).fetchone()[0]
                self.cur.execute("""insert into purchases (id_product, amount, total) values (?, ?, ?)""",
                                 (prod_id, self.price, self.total))
                self.con.commit()
            except Exception as ex:
                print(ex)
        try:
            QMessageBox.information(self, "Успех!", "Данные успешно сохранены", QMessageBox.Ok)
        except Exception as er:
            print(er)

    def delete(self):
        self.tableWidget.removeRow(self.tableWidget.verticalHeader().sortIndicatorSection())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Task5("bd.db")
    mainWindow.show()
    sys.exit(app.exec())
