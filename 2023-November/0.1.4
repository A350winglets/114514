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
