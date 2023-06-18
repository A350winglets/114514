import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
class RandomNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Random Number Generator')
        # 添加标签和文本框用于输入随机数范围
        self.label1 = QLabel('最小值:', self)
        self.label1.move(20, 20)
        self.minLineEdit = QLineEdit(self)
        self.minLineEdit.move(80, 20)
        self.label2 = QLabel('最大值:', self)
        self.label2.move(20, 50)
        self.maxLineEdit = QLineEdit(self)
        self.maxLineEdit.move(80, 50)
        # 添加按钮用于生成随机数
        self.button = QPushButton('生成随机数', self)
        self.button.move(200, 85)
        self.button.clicked.connect(self.generateRandomNumber)
        # 添加标签用于显示生成的随机数
        self.resultLabel = QLabel(self)
        self.resultLabel.move(20, 85)
        # 显示窗口
        self.show()
    def generateRandomNumber(self):
        # 获取输入的最小值和最大值
        min_val = int(self.minLineEdit.text())
        max_val = int(self.maxLineEdit.text())
        # 生成随机数并显示
        result = random.randint(min_val, max_val)
        self.resultLabel.setText(str(result))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomNumberGenerator()
    sys.exit(app.exec_())
