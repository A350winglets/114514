# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:00:40 2022

@author: Student
"""
n=int(input("最小范围="))         #取值最小范围
m=int(input("最大范围="))         #取值最大范围
if n<0 or m<=0 or m<n:            #不符合条件时操作
    print("重新输入")
while n<0 or m<=0 or m<n:
    n=int(input("最小范围="))
    m=int(input("最大范围="))
def fx (x):                      #定义质数函数
    for i in range(2,x):
        if x%i==0:
            return False
    return True
h=0
if n<2:
    for i in range(2,m+1):      #最小值小于2时输出方式
        if fx(i)==True:
            print(i)
            h=h+1
    print("个数：",h)
else:
    for i in range(n,m+1):      #最小值大于2时输出方式
        if fx(i)==True:
            print(i)
            h=h+1
    print("个数：",h)
            
        import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 300)

        self.initUI()

    def initUI(self):
        # 创建中心部件和布局
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)

        # 创建显示结果的文本框
        self.resultLineEdit = QLineEdit(self)
        self.resultLineEdit.setReadOnly(True)
        vbox.addWidget(self.resultLineEdit)

        # 创建按钮布局
        gridLayout = QGridLayout()
        vbox.addLayout(gridLayout)

        # 定义按钮的文本和位置
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        # 创建按钮并连接点击事件
        for btnText, row, col in buttons:
            button = QPushButton(btnText, self)
            button.clicked.connect(self.buttonClicked)
            gridLayout.addWidget(button, row, col)

    def buttonClicked(self):
        # 获取按钮对象
        button = self.sender()

        # 获取按钮的文本
        buttonText = button.text()

        # 如果按钮文本为'='，执行计算结果
        if buttonText == '=':
            try:
                result = eval(self.resultLineEdit.text())
                self.resultLineEdit.setText(str(result))
            except Exception as e:
                self.resultLineEdit.setText('Error')
        # 如果按钮文本为'AC'，清空文本框
        elif buttonText == 'AC':
            self.resultLineEdit.setText('')
        # 其他情况在文本框后追加按钮文本
        else:
            self.resultLineEdit.setText(self.resultLineEdit.text() + buttonText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
