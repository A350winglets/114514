import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QAction, QFileDialog
class HTMLPreviewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HTML Previewer')
        self.setGeometry(300, 300, 800, 600)
        self.text_browser = QTextBrowser(self)
        self.setCentralWidget(self.text_browser)
        self.create_actions()
        self.create_menus()
    def create_actions(self):
        self.open_action = QAction('打开', self)
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.triggered.connect(self.open_file)
        self.exit_action = QAction('退出', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(self.close)
    def create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('文件')
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.exit_action)
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '打开HTML文件')
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    html_content = file.read()
                    self.text_browser.setHtml(html_content)
            except Exception as e:
                self.text_browser.clear()
                self.text_browser.append(f'打开文件失败：{str(e)}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    html_previewer = HTMLPreviewer()
    html_previewer.show()
    sys.exit(app.exec_())