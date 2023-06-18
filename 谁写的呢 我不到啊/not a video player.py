import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QFileDialog


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('视频播放器')

        # 添加部件
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)

        self.videoWidget = QVideoWidget(self)
        vbox.addWidget(self.videoWidget)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)

        self.playButton = QPushButton('播放', self)
        self.playButton.setEnabled(False)
        self.playButton.clicked.connect(self.playVideo)
        hbox.addWidget(self.playButton)

        self.pauseButton = QPushButton('暂停', self)
        self.pauseButton.setEnabled(False)
        self.pauseButton.clicked.connect(self.pauseVideo)
        hbox.addWidget(self.pauseButton)

        self.stopButton = QPushButton('停止', self)
        self.stopButton.setEnabled(False)
        self.stopButton.clicked.connect(self.stopVideo)
        hbox.addWidget(self.stopButton)

        self.show()

    def openFile(self):
        # 打开视频文件
        filename, _ = QFileDialog.getOpenFileName(self, '选择要播放的视频', '',
                                                  'Videos (*.mp4 *.avi *.mkv *.wmv *.mov)')
        if not filename:
            return

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        self.playButton.setEnabled(True)
        self.pauseButton.setEnabled(True)
        self.stopButton.setEnabled(True)

    def playVideo(self):
        # 播放视频
        self.mediaPlayer.play()

    def pauseVideo(self):
        # 暂停视频
        self.mediaPlayer.pause()

    def stopVideo(self):
        # 停止视频
        self.mediaPlayer.stop()

    def createMediaPlayer(self):
        # 创建媒体播放器
        self.mediaPlayer = QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.handleStateChanged)

    def handleStateChanged(self, state):
        # 处理媒体状态改变事件
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setEnabled(False)
            self.pauseButton.setEnabled(True)
            self.stopButton.setEnabled(True)
        elif self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.playButton.setEnabled(True)
            self.pauseButton.setEnabled(False)
            self.stopButton.setEnabled(True)
        elif self.mediaPlayer.state() == QMediaPlayer.StoppedState:
            self.playButton.setEnabled(True)
            self.pauseButton.setEnabled(True)
            self.stopButton.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoPlayer()
    ex.createMediaPlayer()
    ex.openFile()
    sys.exit(app.exec_())
