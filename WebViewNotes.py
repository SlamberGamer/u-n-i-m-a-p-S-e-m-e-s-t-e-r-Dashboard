from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import *
import sys

app = QtWidgets.QApplication(sys.argv)

def mainPyQt5():
    url = 'https://www.protectedtext.com/unimapflexi'
    browser = QWebEngineView()
    browser.load(QUrl(url))
    browser.show()
    sys.exit(app.exec_())

mainPyQt5()