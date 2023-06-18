"""使用系统通知发送指定文字的通知"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton
from win10toast import ToastNotifier


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('通知应用')

        # 添加部件
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)

        label = QLabel('输入通知内容：', self)
        vbox.addWidget(label)

        self.textEdit = QTextEdit(self)
        vbox.addWidget(self.textEdit)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)

        sendButton = QPushButton('发送通知', self)
        sendButton.clicked.connect(self.sendNotification)
        hbox.addWidget(sendButton)

        exitButton = QPushButton('退出', self)
        exitButton.clicked.connect(self.close)
        hbox.addWidget(exitButton)

        self.show()

    def sendNotification(self):
        # 发送通知
        message = self.textEdit.toPlainText()
        toaster = ToastNotifier()
        toaster.show_toast("通知应用", message, duration=5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
