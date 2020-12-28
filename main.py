from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QFileDialog
from PyQt5 import QtWidgets, QtGui, QtCore
from intro_window import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Главное окно")
        self.path = "bd.db"

        self.pushButton.clicked.connect(self.products)
        self.pushButton_2.clicked.connect(self.system)

    def products(self):
        try:
            from session_1 import main
            self.win1 = main.Win1(self.path)
            self.win1.show()
            self.close()
        except Exception as err:
            print(err)

    def system(self):
        try:
            from storage import main
            self.win = main.MainWindow(self.path)
            self.win.show()
            self.close()
        except Exception as err:
            print(err)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec())
