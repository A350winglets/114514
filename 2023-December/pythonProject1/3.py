import os
import re
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QLabel, QFileDialog
class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化界面
        self.init_ui()
        # 初始化播放器
        self.player = QMediaPlayer(self)
        self.player.setVolume(50)
        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration)
        # 初始化歌词
        self.lyric = {}
        self.current_lyric_index = 0
        self.lyric_label = QLabel()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_lyric)
    def init_ui(self):
        # 创建控件
        self.play_button = QPushButton('Play')
        self.pause_button = QPushButton('Pause')
        self.stop_button = QPushButton('Stop')
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_label = QLabel('Volume: 50%')
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_label = QLabel('00:00 / 00:00')
        self.file_label = QLabel('No file selected')
        # 创建布局
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)
        volume_layout = QHBoxLayout()
        volume_layout.addWidget(self.volume_slider)
        volume_layout.addWidget(self.volume_label)
        position_layout = QHBoxLayout()
        position_layout.addWidget(self.position_slider)
        position_layout.addWidget(self.position_label)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.file_label)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(volume_layout)
        main_layout.addLayout(position_layout)
        main_layout.addWidget(self.lyric_label)
        # 设置布局
        self.setLayout(main_layout)
        # 连接信号槽
        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)
        self.volume_slider.valueChanged.connect(self.update_volume)
        self.position_slider.sliderMoved.connect(self.set_position)
    def play(self):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser('~'))
        # 如果选择了文件，则播放
        if file_path:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.player.play()
            self.file_label.setText(os.path.basename(file_path))
            # 加载歌词
            self.load_lyric(os.path.splitext(file_path)[0] + '.lrc')
            self.timer.start(100)
    def pause(self):
        self.player.pause()
    def stop(self):
        self.player.stop()
        self.position_slider.setValue(0)
        self.position_label.setText('00:00 / 00:00')
        self.lyric_label.setText('')
        self.timer.stop()
    def update_volume(self):
        self.player.setVolume(self.volume_slider.value())
        self.volume_label.setText('Volume: {}%'.format(self.volume_slider.value()))
    def update_position(self, position):
        self.position_slider.setValue(position)
        self.position_label.setText('{}/{}'.format(self.format_time(position), self.format_time(self.player.duration())))
        # 更新歌词
        for i in range(self.current_lyric_index, len(self.lyric)):
            if position >= self.lyric[i][0]:
                self.lyric_label.setText(self.lyric[i][1])
                self.current_lyric_index = i
            else:
                break
    def update_duration(self, duration):
        self.position_slider.setRange(0, duration)
        self.position_label.setText('{}/{}'.format(self.format_time(self.player.position()), self.format_time(duration)))
    def set_position(self, position):
        self.player.setPosition(position)
        # 更新歌词
        for i in range(self.current_lyric_index, len(self.lyric)):
            if position >= self.lyric[i][0]:
                self.lyric_label.setText(self.lyric[i][1])
                self.current_lyric_index = i
            else:
                break
    def load_lyric(self, file_path):
        self.lyric = {}
        with open(file_path, encoding='utf-8') as f:
            for line in f:
                m = re.match(r'\[(\d+):(\d+\.\d+)\](.*)', line)
                if m:
                    time = int(m.group(1)) * 60 * 1000 + int(float(m.group(2)) * 1000)
                    text = m.group(3)
                    self.lyric[time] = text
    def update_lyric(self):
        # 更新歌词
        if self.player.state() == QMediaPlayer.PlayingState:
            position = self.player.position()
            for i in range(self.current_lyric_index, len(self.lyric)):
                if position >= self.lyric[i][0]:
                    self.lyric_label.setText(self.lyric[i][1])
                    self.current_lyric_index = i
                else:
                    break
    @staticmethod
    def format_time(milliseconds):
        seconds = milliseconds // 1000
        minutes = seconds // 60
        seconds -= minutes * 60
        return '{:02d}:{:02d}'.format(minutes, seconds)
if __name__ == '__main__':
    app = QApplication([])
    music_player = MusicPlayer()
    music_player.show()
    app.exec_()