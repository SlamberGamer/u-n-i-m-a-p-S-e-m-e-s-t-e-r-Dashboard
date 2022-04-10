# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import webbrowser


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 500, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        # counter value
        self.n = 0

        # creating label
        label = QLabel("Counter", self)

        # setting label geometry
        label.setGeometry(100, 100, 100, 40)

        # creating a command link button
        cl_button = QCommandLinkButton("Next", self)

        # setting geometry
        cl_button.setGeometry(200, 100, 200, 40)

        # adding action to the button
        cl_button.clicked.connect(lambda: increment(self.n))

        # method for incrementing the counter
        def increment(n):
            # increment
            self.n = n + 1

            # setting text to the label
            label.setText(str(self.n))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())