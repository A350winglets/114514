import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLineEdit, QFileDialog, QMessageBox, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPalette, QColor, QDesktopServices
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('浏览器')
        self.setWindowIcon(QIcon('icon.png'))
        # 添加地址栏和工具栏
        self.addressBar = QLineEdit(self)
        self.addressBar.returnPressed.connect(self.loadUrl)
        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)
        self.toolbar.addWidget(self.addressBar)
        # 添加动作
        backAction = QAction(QIcon('back.png'), '后退', self)
        backAction.triggered.connect(self.back)
        self.toolbar.addAction(backAction)
        forwardAction = QAction(QIcon('forward.png'), '前进', self)
        forwardAction.triggered.connect(self.forward)
        self.toolbar.addAction(forwardAction)
        refreshAction = QAction(QIcon('refresh.png'), '刷新', self)
        refreshAction.triggered.connect(self.refresh)
        self.toolbar.addAction(refreshAction)
        bookmarkAction = QAction(QIcon('bookmark.png'), '收藏', self)
        bookmarkAction.triggered.connect(self.bookmark)
        self.toolbar.addAction(bookmarkAction)
        darkModeAction = QAction(QIcon('darkmode.png'), '深色模式', self)
        darkModeAction.triggered.connect(self.toggleDarkMode)
        self.toolbar.addAction(darkModeAction)
        aboutAction = QAction('关于', self)
        aboutAction.triggered.connect(self.showAboutDialog)
        self.toolbar.addAction(aboutAction)
        # 添加浏览器部件
        self.browser = QWebEngineView(self)
        self.setCentralWidget(self.browser)
        self.browser.urlChanged.connect(self.updateAddressBar)
        # 加载主页
        self.loadUrl('https://www.baidu.com')
        # 显示窗口
        self.show()
    def loadUrl(self, url):
        # 加载网页
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.load(QUrl(url))
    def back(self):
        # 后退
        self.browser.back()
    def forward(self):
        # 前进
        self.browser.forward()
    def refresh(self):
        # 刷新
        self.browser.reload()
    def bookmark(self):
        # 收藏网页
        url = self.browser.url().toString()
        title = self.browser.title()
        with open('bookmarks.txt', 'a', encoding='utf-8') as f:
            f.write(title + '\n' + url + '\n')
        QMessageBox.information(self, '收藏网页', '网页已收藏！')
    def toggleDarkMode(self):
        # 切换深色模式
        palette = QPalette()
        if self.browser.palette().color(QPalette.Background).name() == '#ffffff':
            palette.setColor(QPalette.Background, QColor('#222'))
            palette.setColor(QPalette.Base, QColor('#333'))
            palette.setColor(QPalette.Text, QColor('#fff'))
        else:
            palette.setColor(QPalette.Background, QColor('#fff'))
            palette.setColor(QPalette.Base, QColor('#f0f0f0'))
            palette.setColor(QPalette.Text, QColor('#000'))
        self.browser.setPalette(palette)
    def updateAddressBar(self, url):
        # 更新地址栏
        self.addressBar.setText(url.toString())
    def showAboutDialog(self):
        # 显示关于对话框
        aboutDialog = AboutDialog(self)
        aboutDialog.exec()
class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    def initUI(self):
        # 设置窗口大小和标题
        self.setWindowTitle('关于')
        self.setFixedSize(300, 200)
        # 添加部件
        label1 = QLabel('浏览器 v1.0', self)
        label1.move(100, 20)
        label2 = QLabel('作者：PyQt5 爱好者', self)
        label2.move(80, 60)
        label3 = QLabel('联系方式：qq12345678', self)
        label3.move(70, 100)
        label4 = QLabel('版权所有，翻版必究！', self)
        label4.move(80, 140)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Browser()
    sys.exit(app.exec_())