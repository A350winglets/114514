import os
import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QSlider, QVBoxLayout, QWidget

from PyQt5.QtCore import QTimer
class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        ...
        # 初始化歌词标签和计时器
        self.lyrics_label = QLabel()
        self.lyrics_label.setAlignment(Qt.AlignCenter)
        self.lyrics_timer = QTimer(self)
        # 将歌词标签添加到布局中
        self.v_box_layout.addWidget(self.lyrics_label)
        # 连接计时器的信号与槽函数
        self.lyrics_timer.timeout.connect(self.show_lyrics)
    def play_music(self):
        ...
        # 判断是否存在lrc歌词文件
        lrc_file_name = os.path.splitext(file_name)[0] + '.lrc'
        if os.path.exists(lrc_file_name):
            self.lrc_dict = {}
            with open(lrc_file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    if ']' in line:
                        time_str = line.split(']')[0][1:]
                        time_list = time_str.split(':')
                        time = int(time_list[0]) * 60 + float(time_list[1])
                        lrc_text = line.split(']')[-1].strip()
                        self.lrc_dict[time] = lrc_text
            # 开始计时器
            self.lyrics_timer.start(100)
    def show_lyrics(self):
        # 获取当前播放时间
        current_time = self.media_player.position() // 1000
        # 判断当前时间是否在字典中
        if current_time in self.lrc_dict:
            # 获取当前时间所对应的歌词
            lrc_text = self.lrc_dict[current_time]
            # 设置歌词标签
            self.lyrics_label.setText(lrc_text)


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口属性
        self.setWindowTitle('Music Player')
        self.setWindowIcon(QIcon('music_icon.png'))
        self.resize(400, 300)
        # 初始化媒体播放器和标签
        self.media_player = QMediaPlayer(self)
        self.media_player.setVolume(50)
        self.play_label = QLabel()
        self.play_label.setAlignment(Qt.AlignCenter)
        # 初始化按钮和滑块
        self.play_button = QPushButton('Play')
        self.stop_button = QPushButton('Stop')
        self.mute_button = QPushButton('Mute')
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        # 初始化布局
        self.h_box_layout = QHBoxLayout()
        self.v_box_layout = QVBoxLayout()
        self.h_box_layout.addWidget(self.play_button)
        self.h_box_layout.addWidget(self.stop_button)
        self.h_box_layout.addWidget(self.mute_button)
        self.v_box_layout.addWidget(self.play_label)
        self.v_box_layout.addWidget(self.volume_slider)
        self.v_box_layout.addLayout(self.h_box_layout)
        self.setLayout(self.v_box_layout)
        # 连接按钮和滑块的信号与槽函数
        self.play_button.clicked.connect(self.play_music)
        self.stop_button.clicked.connect(self.stop_music)
        self.mute_button.clicked.connect(self.mute_music)
        self.volume_slider.valueChanged.connect(self.change_volume)
    def play_music(self):
        # 选择音频文件
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Audio', os.getenv('HOME'))
        if file_name != '':
            # 设置音频源
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            # 播放音频
            self.media_player.play()
            # 设置播放标签
            self.play_label.setText(os.path.basename(file_name))
    def stop_music(self):
        # 停止播放音频
        self.media_player.stop()
        # 清空播放标签
        self.play_label.setText('')
    def mute_music(self):
        # 静音或取消静音
        if self.media_player.isMuted():
            self.media_player.setMuted(False)
            self.mute_button.setText('Mute')
        else:
            self.media_player.setMuted(True)
            self.mute_button.setText('Unmute')
    def change_volume(self, value):
        # 改变音量大小
        self.media_player.setVolume(value)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
