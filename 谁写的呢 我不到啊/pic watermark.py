import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QPainter, QFont, QColor
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('图片水印应用')
        
        # 添加部件
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)
        
        label = QLabel('添加水印：', self)
        vbox.addWidget(label)
        
        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        
        self.imageLabel = QLabel(self)
        self.imageLabel.setFixedSize(200, 200)
        self.imageLabel.setStyleSheet('border: 1px solid black;')
        hbox.addWidget(self.imageLabel)
        
        vbox2 = QVBoxLayout()
        hbox.addLayout(vbox2)
        
        fontLabel = QLabel('字体：', self)
        vbox2.addWidget(fontLabel)
        
        self.fontEdit = QLineEdit(self)
        vbox2.addWidget(self.fontEdit)
        
        sizeLabel = QLabel('字号：', self)
        vbox2.addWidget(sizeLabel)
        
        self.sizeEdit = QLineEdit(self)
        vbox2.addWidget(self.sizeEdit)
        
        colorLabel = QLabel('颜色（RGB）：', self)
        vbox2.addWidget(colorLabel)
        
        self.colorEdit = QLineEdit(self)
        vbox2.addWidget(self.colorEdit)
        
        textLabel = QLabel('文字：', self)
        vbox2.addWidget(textLabel)
        
        self.textEdit = QLineEdit(self)
        vbox2.addWidget(self.textEdit)
        
        addButton = QPushButton('添加水印', self)
        addButton.clicked.connect(self.addWatermark)
        vbox2.addWidget(addButton)
        
        saveButton = QPushButton('保存图片', self)
        saveButton.clicked.connect(self.saveImage)
        vbox2.addWidget(saveButton)
        
        self.show()
        
    def addWatermark(self):
        # 获取要添加水印的图片和水印参数
        filename, _ = QFileDialog.getOpenFileName(self, '选择要添加水印的图片', '', 'Images (*.png *.xpm *.jpg *.bmp)')
        if not filename:
            return
            
        image = QImage(filename)
        if image.isNull():
            return
            
        font = QFont(self.fontEdit.text() or 'Arial')
        size = int(self.sizeEdit.text() or '12')
        color = QColor(self.colorEdit.text() or '#000000')
        text = self.textEdit.text() or 'Watermark'
        
        # 绘制水印
        painter = QPainter(image)
        painter.setFont(font)
        painter.setPen(color)
        painter.setOpacity(0.5)
        painter.drawText(image.width() // 2, image.height() // 2, text)
        painter.end()
        
        # 显示结果
        pixmap = QPixmap.fromImage(image)
        self.imageLabel.setPixmap(pixmap)
        self.image = image
        self.filename = os.path.splitext(filename)[0] + '_watermark.png'
        
    def saveImage(self):
        # 保存添加水印的图片
        if not hasattr(self, 'filename'):
            return
            
        self.image.save(self.filename)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
