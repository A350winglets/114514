# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 120, 111, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 111, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 130, 360, 32))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"font: 11pt \"微软雅黑\";\n"
"border-radius: 5px;\n"
"border: 1px groove rgb(223, 223, 223);\n"
"background-color: rgb(251, 251, 253);\n"
"border-bottom-width: 1px;\n"
"border-bottom-color: rgb(136, 136, 136);\n"
"border-style: solid;\n"
"selection-background-color: rgb(19, 77, 231);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"font: 11pt \"微软雅黑\";\n"
"border-radius: 5px;\n"
"border: 1px groove rgb(223, 223, 223);\n"
"background-color: rgb(251, 251, 253);\n"
"border-bottom-width: 2px;\n"
"border-bottom-color: rgb(19, 77, 231);\n"
"border-style: solid;\n"
"selection-background-color: rgb(19, 77, 231);\n"
"}\n"
"")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 170, 360, 32))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"font: 11pt \"微软雅黑\";\n"
"border-radius: 5px;\n"
"border: 1px groove rgb(223, 223, 223);\n"
"background-color: rgb(251, 251, 253);\n"
"border-bottom-width: 1px;\n"
"border-bottom-color: rgb(136, 136, 136);\n"
"border-style: solid;\n"
"selection-background-color: rgb(19, 77, 231);\n"
"lineedit-password-mask-delay: 1000\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"font: 11pt \"微软雅黑\";\n"
"border-radius: 5px;\n"
"border: 1px groove rgb(223, 223, 223);\n"
"background-color: rgb(251, 251, 253);\n"
"border-bottom-width: 2px;\n"
"border-bottom-color: rgb(19, 77, 231);\n"
"border-style: solid;\n"
"selection-background-color: rgb(19, 77, 231);\n"
"lineedit-password-mask-delay: 1000\n"
"}\n"
"")
        self.lineEdit_2.setMaxLength(8)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 132, 32))
        self.pushButton.setStyleSheet("QPushButton {\n"
"font: 11pt \"微软雅黑\";\n"
"color: rgb(26, 26, 26);\n"
"border-radius: 5px; \n"
"border: 1px groove rgb(223, 223, 223);\n"
"background-color: rgb(251, 251, 253);\n"
"border-style: solid\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"font: 11pt \"微软雅黑\";\n"
"color: rgb(26, 26, 26);\n"
"border-radius: 5px; \n"
"border: 1px groove rgb(223, 223, 223);\n"
"background-color: rgb(246, 246, 246);\n"
"border-style: solid\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font: 11pt \"微软雅黑\";\n"
"color: rgb(136, 136, 136);\n"
"border-radius: 5px; \n"
"border: 1px groove rgb(223, 223, 223);\n"
"background-color: rgb(240, 240, 240);\n"
"border-style: solid\n"
"}\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 250, 301, 121))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(80, 380, 201, 91))
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setIconSize(QtCore.QSize(32, 32))
        self.radioButton.setChecked(False)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(True)
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(500, 190, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(230, 510, 271, 8))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
"border-radius:4px;\n"
"background: rgb(19, 77, 231)\n"
"}\n"
"\n"
"QProgressBar#progressBar {\n"
"height: 8px;\n"
"border-radius: 4px;\n"
"background: rgb(251, 251, 253);\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 90)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(290, 410, 371, 21))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.actionqi = QtWidgets.QAction(MainWindow)
        self.actionqi.setObjectName("actionqi")
        self.menu.addAction(self.action1)
        self.menu.addSeparator()
        self.menu.addAction(self.actionqi)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.lineEdit_2.clear) # type: ignore
        self.pushButton.clicked.connect(self.lineEdit.clear) # type: ignore
        self.lineEdit_2.textChanged['QString'].connect(self.lcdNumber.display) # type: ignore
        self.action1.triggered.connect(MainWindow.close) # type: ignore
        self.actionqi.triggered.connect(self.lineEdit.clear) # type: ignore
        self.actionqi.triggered.connect(self.lineEdit_2.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "clear all"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.menu.setTitle(_translate("MainWindow", "主菜单"))
        self.action1.setText(_translate("MainWindow", "关闭"))
        self.actionqi.setText(_translate("MainWindow", "清空"))
