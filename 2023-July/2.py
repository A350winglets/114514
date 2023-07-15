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
