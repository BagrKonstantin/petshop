from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from intro_window import Ui_MainWindow
from session_1.main import Win1 as tab_1
from session_3.main_3 import Win3 as tab_2
from storage.main import MainWindow as tab_3
from session_5.main_5 import UI_Task5 as tab_4
from session_4.main_4 import Deal as tab_5


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Главное окно")
        self.path = "bd.db"
        self.tab_1 = tab_1(self.path)
        self.tab_2 = tab_2(self.path)
        self.tab_3 = tab_3(self.path)
        self.tab_4 = tab_4(self.path)
        self.tab_5 = tab_5(self.path)

        self.tabWidget.removeTab(4)
        self.tabWidget.removeTab(3)
        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(0)


        self.tabWidget.addTab(self.tab_1, "Товары")
        self.tabWidget.addTab(self.tab_2, "Клиенты")
        self.tabWidget.addTab(self.tab_3, "Учет")
        self.tabWidget.addTab(self.tab_4, "Покупки")
        self.tabWidget.addTab(self.tab_5, "Продажи")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec())
