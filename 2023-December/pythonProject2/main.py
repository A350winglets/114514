# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")



        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if self.pushButton.clicked:
            self.pushButton.clicked.connect(lambda:QSound.play('audio/对不起.wav'))
        if self.pushButton_2.clicked:
            self.pushButton_2.clicked.connect(lambda:QSound.play('audio/不行.wav'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "对不起"))
        self.pushButton_2.setText(_translate("MainWindow", "不行"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow =QtWidgets.QMainWindow()
    abc = Ui_MainWindow()
    abc.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())