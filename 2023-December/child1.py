# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

def __init__(self): # 构造方法
    super(Ui_Form, self).__init__()
    self.setupUi(self) # 初始化窗体设置

class Ui_child1(QMainWindow):
    def setupUi(self, child1):
        child1.setObjectName("child1")
        child1.resize(410, 107)
        self.centralwidget = QtWidgets.QWidget(child1)
        self.centralwidget.setObjectName("centralwidget")
        child1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(child1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 23))
        self.menubar.setObjectName("menubar")
        child1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(child1)
        self.statusbar.setObjectName("statusbar")
        child1.setStatusBar(self.statusbar)

        self.retranslateUi(child1)
        QtCore.QMetaObject.connectSlotsByName(child1)

    def retranslateUi(self, child1):
        _translate = QtCore.QCoreApplication.translate
        child1.setWindowTitle(_translate("child1", "子1"))
