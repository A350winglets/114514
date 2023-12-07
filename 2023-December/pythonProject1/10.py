"""语音合成器"""

import sys
import pyttsx3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('语音合成器')

        # 添加部件
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)

        label = QLabel('输入要合成的文本：', self)
        vbox.addWidget(label)

        self.textEdit = QTextEdit(self)
        vbox.addWidget(self.textEdit)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)

        speakButton = QPushButton('朗读', self)
        speakButton.clicked.connect(self.speakText)
        hbox.addWidget(speakButton)

        exitButton = QPushButton('退出', self)
        exitButton.clicked.connect(self.close)
        hbox.addWidget(exitButton)

        self.show()

    def speakText(self):
        # 合成语音并朗读
        message = self.textEdit.toPlainText()
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())