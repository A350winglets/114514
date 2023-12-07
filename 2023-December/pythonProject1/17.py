import sys
import hashlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox


class MD5Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MD5 Editor')
        self.setGeometry(300, 300, 800, 600)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.create_actions()
        self.create_menus()

    def create_actions(self):
        self.open_action = QAction('打开', self)
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction('保存', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.triggered.connect(self.save_file)

        self.exit_action = QAction('退出', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(self.close)

        self.calculate_md5_action = QAction('计算MD5', self)
        self.calculate_md5_action.setShortcut('Ctrl+M')
        self.calculate_md5_action.triggered.connect(self.calculate_md5)

    def create_menus(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('文件')
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.exit_action)

        md5_menu = menubar.addMenu('MD5')
        md5_menu.addAction(self.calculate_md5_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '打开文件')
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_edit.setPlainText(file.read())
            except Exception as e:
                QMessageBox.warning(self, '错误', str(e))

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, '保存文件')
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_edit.toPlainText())
            except Exception as e:
                QMessageBox.warning(self, '错误', str(e))

    def calculate_md5(self):
        text = self.text_edit.toPlainText()
        if text:
            md5 = hashlib.md5(text.encode()).hexdigest()
            QMessageBox.information(self, 'MD5', f'MD5 值：{md5}')
        else:
            QMessageBox.warning(self, '警告', '请先输入文本')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md5_editor = MD5Editor()
    md5_editor.show()
    sys.exit(app.exec_())