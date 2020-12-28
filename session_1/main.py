from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from session_1.window_1 import Ui_MainWindow
from session_1.save_window import Ui_MainWindow as SaveWin
from session_1.change_price import Ui_MainWindow as ChangeWin
from session_1.log_price_change import Ui_MainWindow as LogWin
import sqlite3
import openpyxl


class Save(QMainWindow, SaveWin):
    def __init__(self, path):
        super(Save, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Ввести данные')
        self.path = path
        self.pushButton_save.clicked.connect(self.save_data)

    def save_data(self):
        try:
            title = str(self.lineEdit_title.text())
            pet = str(self.comboBox_animal.currentText())
            type_p = str(self.comboBox_type.currentText())
            p_price = float(self.lineEdit_purchasing_price.text())
            r_price = p_price * 1.5
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
            self.win = Win1("../bd.db")
            self.win.show()
            self.close()
        except Exception as err:
            QMessageBox.critical(self, "Ошибка", "Введены неверные данные", QMessageBox.Ok)
            print(err)

    def closeEvent(self, event):
        self.win = Win1("../bd.db")
        self.win.show()
        self.close()


class ChangePrice(QMainWindow, ChangeWin):
    def __init__(self, path, id):
        super(ChangePrice, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Изменение цены')
        self.path = path
        self.id = id

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute(
            """Select title_products, purchase_price from products where id_products = {}""".format(id)).fetchall()
        con.close()

        self.lineEdit.setText(self.data[0][0])
        self.lineEdit_old_price.setText(str(self.data[0][1]))

        self.spinBox_2.setValue(self.data[0][1])

        self.pushButton_save.clicked.connect(self.save)

    def save(self):
        try:
            con = sqlite3.connect(self.path)
            cur = con.cursor()
            cur.execute("""update products 
                            set purchase_price = {}, retail_price = {} 
                            where id_products = {}""".format(self.spinBox_2.value(), self.spinBox_2.value() * 1.5,
                                                             self.id))
            print(self.data[0][0], self.data[0][1], self.spinBox_2.value())
            cur.execute(
                """insert into price_changes (title_product, old_price, new_price) VALUES ('{}', {}, {})""".format(
                    self.data[0][0], self.data[0][1], self.spinBox_2.value()))
            con.commit()
            con.close()
            self.win = Win1("../bd.db")
            self.win.show()
            self.close()
        except Exception as err:
            print(err)

    def closeEvent(self, event):
        self.win = Win1("../bd.db")
        self.win.show()
        self.close()


class LogPrice(QMainWindow, LogWin):
    def __init__(self, path):
        super(LogPrice, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Журнал изменения цен')
        self.path = path
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        self.data = cur.execute("""select * from price_changes""").fetchall()

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.setItem(i, 2, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(self.data[i][1])
            self.tableWidget.item(i, 1).setText(str(self.data[i][2]))
            self.tableWidget.item(i, 2).setText(str(self.data[i][3]))

        for i in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(i, 1)
            font = QtGui.QFont()
            font.setStrikeOut(True)
            item.setFont(font)
            brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)
            item = self.tableWidget.item(i, 2)
            brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setForeground(brush)

    def closeEvent(self, event):
        self.win = Win1("../bd.db")
        self.win.show()
        self.close()


class Win1(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super(Win1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Товары')
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
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_insert.clicked.connect(self.insert)
        self.pushButton_change_price.clicked.connect(self.change_price)
        self.pushButton_log.clicked.connect(self.log)

    def log(self):
        try:
            self.win = LogPrice(self.path)
            self.win.show()
            self.close()
        except Exception as err:
            print(err)

    def change_price(self):
        print(self.tableWidget.verticalHeader().sortIndicatorSection())
        if self.tableWidget.verticalHeader().sortIndicatorSection() == self.tableWidget.rowCount():
            QMessageBox.critical(self, "Ошибка", "Выберите строку", QMessageBox.Ok)
        else:
            self.win = ChangePrice(self.path, self.data[self.tableWidget.verticalHeader().sortIndicatorSection()][0])
            self.win.show()
            self.close()

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
        self.close()

    def insert(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        try:
            fname = QFileDialog.getOpenFileName(self, '', 'C://')[0]
            wb = openpyxl.load_workbook(fname)

            # печатаем список листов
            sheets = wb.sheetnames

            # получаем активный лист
            sheet = wb.active
            sheet_name = str(sheet).strip('<Worksheet "').strip('">')
            for i in range(1, len(list(sheet.rows))):
                name = sheet[str(list(sheet.rows)[i][0]).strip("<Cell '{}'.".format(sheet_name)).strip('>')].value
                pet_name = sheet[str(list(sheet.rows)[i][1]).strip("<Cell '{}'.".format(sheet_name)).strip('>')].value
                category = sheet[
                    str(list(sheet.rows)[i][2]).strip("<Cell '{}'".format(sheet_name)).strip('.').strip('>')].value
                info = sheet[
                    str(list(sheet.rows)[i][3]).strip("<Cell '{}'".format(sheet_name)).strip('.').strip('>')].value
                buy_price = int(
                    sheet[
                        str(list(sheet.rows)[i][4]).strip("<Cell '{}'".format(sheet_name)).strip('.').strip('>')].value)
                second_price = 1.5 * buy_price
                cur.execute(
                    """insert into products (title_products, pet, type, description, purchase_price, retail_price) values (?, ?, ?, ?, ?, ?)""",
                    (name, pet_name, category, info, buy_price, second_price))
                con.commit()
                self.update_data()

        except Exception as er:
            print(er)
        con.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Win1("../bd.db")
    mainWindow.show()
    sys.exit(app.exec())
