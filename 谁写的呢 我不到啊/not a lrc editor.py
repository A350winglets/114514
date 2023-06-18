import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget
class LrcEditor(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口属性
        self.setWindowTitle('Lrc Editor')
        self.setWindowIcon(QIcon('lrc_icon.png'))
        self.resize(600, 400)
        # 初始化歌曲信息部分
        self.title_label = QLabel('Title:')
        self.title_edit = QLineEdit()
        self.artist_label = QLabel('Artist:')
        self.artist_edit = QLineEdit()
        self.album_label = QLabel('Album:')
        self.album_edit = QLineEdit()
        # 初始化歌词编辑部分
        self.lrc_edit = QTextEdit()
        # 初始化按钮部分
        self.open_button = QPushButton('Open')
        self.save_button = QPushButton('Save')
        # 初始化布局
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.title_edit)
        self.title_layout.addWidget(self.artist_label)
        self.title_layout.addWidget(self.artist_edit)
        self.title_layout.addWidget(self.album_label)
        self.title_layout.addWidget(self.album_edit)
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.open_button)
        self.button_layout.addWidget(self.save_button)
        self.v_box_layout = QVBoxLayout()
        self.v_box_layout.addLayout(self.title_layout)
        self.v_box_layout.addWidget(self.lrc_edit)
        self.v_box_layout.addLayout(self.button_layout)
        self.setLayout(self.v_box_layout)
        # 连接按钮的信号与槽函数
        self.open_button.clicked.connect(self.open_lrc_file)
        self.save_button.clicked.connect(self.save_lrc_file)
        # 初始化歌词文件名
        self.lrc_file_name = ''
    def open_lrc_file(self):
        # 打开 lrc 文件
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Lrc', os.getenv('HOME'), 'Lrc Files (*.lrc)')
        if file_name != '':
            self.lrc_file_name = file_name
            with open(file_name, 'r', encoding='utf-8') as f:
                # 读取歌曲信息和歌词文本
                lines = f.readlines()
                if len(lines) > 0:
                    title = ''
                    artist = ''
                    album = ''
                    lrc_text = ''
                    for line in lines:
                        if line.startswith('[ti:'):
                            title = line[4:-2]
                        elif line.startswith('[ar:'):
                            artist = line[4:-2]
                        elif line.startswith('[al:'):
                            album = line[4:-2]
                        else:
                            lrc_text += line
                    # 显示歌曲信息和歌词文本
                    self.title_edit.setText(title)
                    self.artist_edit.setText(artist)
                    self.album_edit.setText(album)
                    self.lrc_edit.setText(lrc_text)
    def save_lrc_file(self):
        if self.lrc_file_name == '':
            # 如果没有打开过 lrc 文件，则另存为
            file_name, _ = QFileDialog.getSaveFileName(self, 'Save Lrc', os.getenv('HOME'), 'Lrc Files (*.lrc)')
            if file_name != '':
                self.lrc_file_name = file_name
        if self.lrc_file_name != '':
            # 保存歌曲信息和歌词文本
            title = self.title_edit.text()
            artist = self.artist_edit.text()
            album = self.album_edit.text()
            lrc_text = self.lrc_edit.toPlainText()
            with open(self.lrc_file_name, 'w', encoding='utf-8') as f:
                f.write('[ti:%s]\n' % title)
                f.write('[ar:%s]\n' % artist)
                f.write('[al:%s]\n' % album)
                f.write(lrc_text)
            QMessageBox.information(self, 'Save Lrc', 'Lrc file saved successfully.')
if __name__ == '__main__':
    app = QApplication([])
    editor = LrcEditor()
    editor.show()
    app.exec_()
