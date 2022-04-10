# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SemesterPendekAugust2021v2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import qdarkstyle
import webbrowser

f_date = date(2022, 3, 26)  # first date (year, month, date
l_date = date(2022, 8, 2)  # Last Date
A_date = date(2021, 7, 11)  # just to get 1 value. cannot use standart value because the date need to be in date
B_date = date(2021, 7, 10)  # just to get 1 value. cannot use standart value because the date need to be in date
one = A_date - B_date
today = date.today()
#print("Today's date:", today)
Total = l_date - f_date
#print(Total.days)
Current = l_date - today
#print(Current.days)
percentage = 100 - (( Current / Total ) * 100 )
weeks = (Current / one) / 7
days = today - f_date
weekscount = ((today-f_date) / one)/7
print (weekscount)
#print (weeks)
#print (percentage)

def MicroprocessorWASAP():
    webbrowser.open('https://t.me/+hm0zR0fgnXk1N2Zl') #self.pushButton.clicked.connect(MicroprocessorWASAP)
def MicroprocessorCLASS():
    webbrowser.open('https://classroom.google.com/c/NDgzNDE4ODUyMjUy?cjc=opvwvjf') #self.pushButton_2.clicked.connect(MicroprocessorCLASS)

def ElectromagneticWASAP():
    webbrowser.open('https://chat.whatsapp.com/L24RIqmpETBA7stHCHWi0f') #self.pushButton_4.clicked.connect(ElectromagneticWASAP)
def ElectromagneticCLASS():
    webbrowser.open('https://classroom.google.com/c/NDcxOTEzMDkyODAx?cjc=je7xft6') #self.pushButton_3.clicked.connect(ElectromagneticCLASS)

def EnglishWASAP():
    webbrowser.open('https://chat.whatsapp.com/KlKG42CNmQk6mDld9JDSFn') #self.pushButton_6.clicked.connect(EnglishWASAP)
def EnglishCLASS():
    webbrowser.open('https://classroom.google.com/c/NDgwNDIyOTMxMjE2?cjc=dqtwpy4') #self.pushButton_7.clicked.connect(EnglishCLASS)

def CircuitWASAP():
    webbrowser.open('https://chat.whatsapp.com/CcyUaQm7dfeE6xYSrNxo3w') #self.pushButton_8.clicked.connect(CircuitWASAP)
def CircuitCLASS():
    webbrowser.open('https://classroom.google.com/c/NDgzMzE4MDc2NTg4?cjc=mh5klxh') #self.pushButton_9.clicked.connect(CircuitCLASS)

def AnalogWASAP():
    webbrowser.open('https://chat.whatsapp.com/Fk1cKYZl7dQH4PLZt0FR0R') #self.pushButton_10.clicked.connect(AnalogWASAP)
def AnalogCLASS():
    webbrowser.open('https://classroom.google.com/c/NDgwNDIzODk5ODY2?cjc=pifkqyc') #self.pushButton_11.clicked.connect(AnalogCLASS)

def ONLINENOTES():
    webbrowser.open('https://docs.google.com/spreadsheets/d/1HCHfHwx2NJgcOHa9wzyq-LKfV76KxazM2z1mtJGfalI/edit?usp=sharing') #self.pushButton_5.clicked.connect(ONLINENOTES)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(599, 822)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(40, 600, 521, 172))
        self.tableWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setMidLineWidth(-3)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(23)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(False)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(70)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(340, 370, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat("%p%")
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(300, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 40, 441, 111))
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb74, 77, 82;\n"
"    border-style: outset;\n"
"    border-width: 2.5px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 20px;\n"
"    min-width: 5em;\n"
"    padding: 10px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(300, 250, 111, 41))
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_3.setLineWidth(0)
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 410, 261, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setLineWidth(1)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(28, 170, 251, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(245, 81, 66);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(235, 52, 128);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(245, 81, 66);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(235, 52, 128);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(245, 81, 66);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(235, 52, 128);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(245, 81, 66);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 7, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(235, 52, 128);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 2)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    background-color: rgb(245, 81, 66);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 9, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    background-color: rgb(235, 52, 128);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 9, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Semester 4 \"2022"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Saturday"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sunday"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "9.00 am - 12.00 am"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2.00 pm - 5.00 pm"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "5.30 pm- 7.30 pm"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "NMJ21203\n"
"Microprocessor"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "NMJ21803\n"
"Electromagnetic Theory"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "SMB31202\n"
"English For Technical Communication"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "NMJ21603\n"
"Integrated Circuit Design"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "NMJ20303\n"
"Analog Electronic II"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Weeks left"))
        self.label_3.setText(_translate("MainWindow", "██╗░░░██╗███╗░░██╗██╗███╗░░░███╗░█████╗░██████╗░\n"
"██║░░░██║████╗░██║██║████╗░████║██╔══██╗██╔══██╗\n"
"██║░░░██║██╔██╗██║██║██╔████╔██║███████║██████╔╝\n"
"██║░░░██║██║╚████║██║██║╚██╔╝██║██╔══██║██╔═══╝░\n"
"╚██████╔╝██║░╚███║██║██║░╚═╝░██║██║░░██║██║░░░░░\n"
"░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░"))
        self.pushButton_5.setText(_translate("MainWindow", "Classroom Notes"))
        self.label_8.setText(_translate("MainWindow", "No of Weeks"))
        self.label_10.setText(_translate("MainWindow", "“Barangsiapa yang menempuh satu jalan untuk menuntutilmu maka Allah SWT akan memudahkan baginya jalan untuk ke Syurga. \"\n"
"\n"
" [Riwayat Muslim (4867)]"))
        self.label.setText(_translate("MainWindow", "Microprocessor"))
        self.pushButton.setText(_translate("MainWindow", "Whatsapp"))
        self.pushButton_2.setText(_translate("MainWindow", "Classroom"))
        self.label_2.setText(_translate("MainWindow", "Electromagnetic Theory"))
        self.pushButton_4.setText(_translate("MainWindow", "Whatsapp"))
        self.pushButton_3.setText(_translate("MainWindow", "Classroom"))
        self.label_4.setText(_translate("MainWindow", "English For Technical Com"))
        self.pushButton_6.setText(_translate("MainWindow", "Whatsapp"))
        self.pushButton_7.setText(_translate("MainWindow", "Classroom"))
        self.label_5.setText(_translate("MainWindow", "Integrated Circuit Design"))
        self.pushButton_8.setText(_translate("MainWindow", "Whatsapp"))
        self.pushButton_9.setText(_translate("MainWindow", "Classroom"))
        self.label_6.setText(_translate("MainWindow", "Analog Electronic II"))
        self.pushButton_10.setText(_translate("MainWindow", "Whatsapp"))
        self.pushButton_11.setText(_translate("MainWindow", "Classroom"))

        self.lcdNumber.display(weeks)

        self.lcdNumber_3.display(weekscount)
        self.progressBar.setValue(percentage)
        self.pushButton.clicked.connect(MicroprocessorWASAP)
        self.pushButton_2.clicked.connect(MicroprocessorCLASS)
        self.pushButton_4.clicked.connect(ElectromagneticWASAP)
        self.pushButton_3.clicked.connect(ElectromagneticCLASS)
        self.pushButton_6.clicked.connect(EnglishWASAP)
        self.pushButton_7.clicked.connect(EnglishCLASS)
        self.pushButton_8.clicked.connect(CircuitWASAP)
        self.pushButton_9.clicked.connect(CircuitCLASS)
        self.pushButton_10.clicked.connect(AnalogWASAP)
        self.pushButton_11.clicked.connect(AnalogCLASS)
        self.pushButton_5.clicked.connect(ONLINENOTES)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

