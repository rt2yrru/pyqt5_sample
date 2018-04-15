# coding: utf-8
import sys
import os
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QWidget

app = QtWidgets.QApplication(sys.argv)
view = QtWebEngineWidgets.QWebEngineView()
w=QWidget()
w.setWindowTitle('html loader test')
view.load(QtCore.QUrl().fromLocalFile(''))
view.show()
sys.exit(app.exec_())
