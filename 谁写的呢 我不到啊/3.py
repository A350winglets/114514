import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import numpy as np
class FunctionPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('函数图像绘制软件')
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        
        self.function_label = QLabel("函数：")
        self.layout.addWidget(self.function_label)
        
        self.function_input = QLineEdit()
        self.layout.addWidget(self.function_input)
        
        self.plot_button = QPushButton("绘制")
        self.plot_button.clicked.connect(self.plot)
        self.layout.addWidget(self.plot_button)
        
        self.setLayout(self.layout)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        
        # 设置画笔颜色和宽度
        pen = QPen(Qt.blue, 2)
        painter.setPen(pen)
        
        # 获取窗口的宽度和高度
        width = self.width()
        height = self.height()
        
        # 计算x轴和y轴的原点坐标
        origin_x = width // 2
        origin_y = height // 2
        
        # 绘制x轴和y轴
        painter.drawLine(0, origin_y, width, origin_y)
        painter.drawLine(origin_x, 0, origin_x, height)
        
        # 获取函数输入框中的文本
        function_text = self.function_input.text()
        
        try:
            # 生成x轴上的坐标点
            x_points = np.linspace(-10, 10, 1000)
            
            # 将x轴坐标点代入函数，计算得到y轴坐标点
            y_points = eval(function_text)
            
            # 将坐标点转换为窗口坐标系中的坐标
            x_points = x_points + origin_x
            y_points = origin_y - y_points * (height / 20)
            
            # 绘制函数图像
            for i in range(len(x_points) - 1):
                painter.drawLine(QPoint(x_points[i], y_points[i]), QPoint(x_points[i+1], y_points[i+1]))
        
        except Exception as e:
            print("绘制函数图像出错:", e)
        
    def plot(self):
        self.update()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    function_plot = FunctionPlot()
    function_plot.show()
    sys.exit(app.exec_())
