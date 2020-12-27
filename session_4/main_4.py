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

        self.pushButton_close.clicked.connect(self.close)
