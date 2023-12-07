from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
self.initUI()

def initUI(self):
# 创建播放器和按钮
    self.player = QMediaPlayer(self)
    self.play_button = QPushButton('播放', self)
    self.play_button.clicked.connect(self.play_music)
    self.pause_button = QPushButton('暂停', self)
    self.pause_button.clicked.connect(self.pause_music)
    self.stop_button = QPushButton('停止', self)
    self.stop_button.clicked.connect(self.stop_music)
    self.open_button = QPushButton('打开', self)
    self.open_button.clicked.connect(self.open_music)

# 设置按钮布局
    self.play_button.move(50, 50)
    self.pause_button.move(150, 50)
    self.stop_button.move(250, 50)
    self.open_button.move(350, 50)

# 设置窗口
    self.setGeometry(300, 300, 500, 150)
    self.setWindowTitle('音乐播放器')
    self.show()

def play_music(self):
    self.player.play()

def pause_music(self):
    self.player.pause()

def stop_music(self):
    self.player.stop()

def open_music(self):
# 打开文件对话框
    file_name, _ = QFileDialog.getOpenFileName(self, '打开文件', '', '音频文件 (*.mp3 *.wav)')
    if file_name != '':
# 设置媒体
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
# 播放音乐
        self.player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MusicPlayer()
    sys.exit(app.exec_())