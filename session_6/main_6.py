from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPrintDialog, QPrinter
import sqlite3
from session_6.storage import Ui_MainWindow


class Storage(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Отчетность")
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
