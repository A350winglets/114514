import sys
from PyQt5.QtCore import Qt, QUrl, QTime
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QFileDialog, QSlider, QStyle, QSizePolicy


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

        hbox1 = QHBoxLayout()
        vbox.addLayout(hbox1)

        self.playButton = QPushButton(self.style().standardIcon(QStyle.SP_MediaPlay), '', self)
        self.playButton.setEnabled(False)
        self.playButton.clicked.connect(self.playVideo)
        hbox1.addWidget(self.playButton)

        self.pauseButton = QPushButton(self.style().standardIcon(QStyle.SP_MediaPause), '', self)
        self.pauseButton.setEnabled(False)
        self.pauseButton.clicked.connect(self.pauseVideo)
        hbox1.addWidget(self.pauseButton)

        self.stopButton = QPushButton(self.style().standardIcon(QStyle.SP_MediaStop), '', self)
        self.stopButton.setEnabled(False)
        self.stopButton.clicked.connect(self.stopVideo)
        hbox1.addWidget(self.stopButton)

        self.positionSlider = QSlider(Qt.Horizontal, self)
        self.positionSlider.setToolTip('播放进度')
        self.positionSlider.setEnabled(False)
        self.positionSlider.setMinimum(0)
        self.positionSlider.setMaximum(1000)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        hbox1.addWidget(self.positionSlider)

        hbox2 = QHBoxLayout()
        vbox.addLayout(hbox2)

        self.openButton = QPushButton('打开文件', self)
        self.openButton.clicked.connect(self.openFile)
        hbox2.addWidget(self.openButton)

        self.timeLabel = QLabel('00:00 / 00:00', self)
        hbox2.addWidget(self.timeLabel)

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
        self.positionSlider.setEnabled(True)

    def playVideo(self):
        # 播放视频
        self.mediaPlayer.play()

    def pauseVideo(self):
        # 暂停视频
        self.mediaPlayer.pause()

    def stopVideo(self):
        # 停止视频
        self.mediaPlayer.stop()

    def setPosition(self, position):
        # 设置播放进度
        self.mediaPlayer.setPosition(position * self.mediaPlayer.duration() / 1000)

    def createMediaPlayer(self):
        # 创建媒体播放器
        self.mediaPlayer = QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.handleStateChanged)
        self.mediaPlayer.positionChanged.connect(self.handlePositionChanged)
        self.mediaPlayer.durationChanged.connect(self.handleDurationChanged)

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

    def handlePositionChanged(self, position):
        # 处理播放进度改变事件
        self.positionSlider.setValue(position * 1000 / self.mediaPlayer.duration())
        self.timeLabel.setText('{}/{}'.format(QTime(0, position // 60000, position // 1000 % 60).toString('mm:ss'),
                                              QTime(0, self.mediaPlayer.duration() // 60000,
                                                    self.mediaPlayer.duration() // 1000 % 60).toString('mm:ss')))

    def handleDurationChanged(self, duration):
        # 处理视频总时长改变事件
        self.positionSlider.setMaximum(duration / 1000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoPlayer()
    ex.createMediaPlayer()
    ex.openFile()
    sys.exit(app.exec_())