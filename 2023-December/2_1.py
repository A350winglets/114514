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
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QColorDialog, QFileDialog, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPointF


class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Drawing App')
        self.setGeometry(300, 300, 800, 600)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.setupToolBar()

        self.penColor = Qt.black
        self.penWidth = 2

    def setupToolBar(self):
        # 创建工具栏
        toolbar = self.addToolBar('Tools')

        # 创建画笔颜色选择动作
        colorAction = QAction('Pen Color', self)
        colorAction.triggered.connect(self.selectPenColor)
        toolbar.addAction(colorAction)

        # 创建画笔粗细选择动作
        widthAction = QAction('Pen Width', self)
        widthAction.triggered.connect(self.selectPenWidth)
        toolbar.addAction(widthAction)

        # 创建清除画布动作
        clearAction = QAction('Clear', self)
        clearAction.triggered.connect(self.clearCanvas)
        toolbar.addAction(clearAction)

    def selectPenColor(self):
        # 打开颜色选择对话框选择画笔颜色
        color = QColorDialog.getColor()
        if color.isValid():
            self.penColor = color

    def selectPenWidth(self):
        # 打开输入对话框输入画笔粗细
        width, ok = QInputDialog.getInt(self, 'Pen Width', 'Enter pen width:')
        if ok:
            self.penWidth = width

    def clearCanvas(self):
        # 清除画布上的图形
        self.scene.clear()

    def mousePressEvent(self, event):
        # 鼠标按下时开始绘制
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()

    def mouseReleaseEvent(self, event):
        # 鼠标释放时结束绘制
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.drawShape()

    def drawShape(self):
        # 根据起始点和终点绘制形状
        shape = QPainterPath()
        shape.moveTo(self.startPoint)
        shape.lineTo(self.endPoint)

        pen = QPen(self.penColor, self.penWidth)
        self.scene.addPath(shape, pen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    drawing_app = DrawingApp()
    drawing_app.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QFileDialog
from PyQt5.QtGui import QPixmap


class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Image Editor')
        self.setGeometry(300, 300, 400, 400)

        self.initUI()

    def initUI(self):
        # 创建中心部件和布局
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)

        # 创建显示图片的标签
        self.imageLabel = QLabel(self)
        vbox.addWidget(self.imageLabel)

        # 创建按钮布局
        hbox = QHBoxLayout()
        vbox.addLayout(hbox)

        # 创建打开图片按钮
        openButton = QPushButton('Open Image', self)
        openButton.clicked.connect(self.openImage)
        hbox.addWidget(openButton)

        # 创建保存图片按钮
        saveButton = QPushButton('Save Image', self)
        saveButton.clicked.connect(self.saveImage)
        hbox.addWidget(saveButton)

    def openImage(self):
        # 打开文件对话框选择图片
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if fileName:
            # 加载图片并显示
            image = QPixmap(fileName)
            self.imageLabel.setPixmap(image)

    def saveImage(self):
        # 打开文件对话框选择保存路径和文件名
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if fileName:
            # 获取当前显示的图片，并保存到指定路径
            image = self.imageLabel.pixmap()
            image.save(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())

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
