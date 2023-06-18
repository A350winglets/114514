"""带有切换粗体、斜体、字体和深色模式的文字编辑器"""




import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMenuBar, QMenu, QFontDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 设置窗口大小和标题
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Text Editor')
        # 添加文本编辑框
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        # 添加菜单栏
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        # 添加文件菜单
        fileMenu = QMenu('文件', self)
        self.menuBar.addMenu(fileMenu)
        # 添加文件菜单项
        newFileAction = QAction('新建', self)
        newFileAction.setShortcut('Ctrl+N')
        newFileAction.triggered.connect(self.newFile)
        fileMenu.addAction(newFileAction)
        openFileAction = QAction('打开', self)
        openFileAction.setShortcut('Ctrl+O')
        openFileAction.triggered.connect(self.openFile)
        fileMenu.addAction(openFileAction)
        saveFileAction = QAction('保存', self)
        saveFileAction.setShortcut('Ctrl+S')
        saveFileAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveFileAction)
        exitAction = QAction('退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        # 添加编辑菜单
        editMenu = QMenu('编辑', self)
        self.menuBar.addMenu(editMenu)
        # 添加编辑菜单项
        boldAction = QAction('粗体', self)
        boldAction.setShortcut('Ctrl+B')
        boldAction.setCheckable(True)
        boldAction.triggered.connect(self.toggleBold)
        editMenu.addAction(boldAction)
        italicAction = QAction('斜体', self)
        italicAction.setShortcut('Ctrl+I')
        italicAction.setCheckable(True)
        italicAction.triggered.connect(self.toggleItalic)
        editMenu.addAction(italicAction)
        fontAction = QAction('字体', self)
        fontAction.setShortcut('Ctrl+T')
        fontAction.triggered.connect(self.changeFont)
        editMenu.addAction(fontAction)
        fontSizeAction = QAction('字号', self)
        fontSizeAction.setShortcut('Ctrl+H')
        fontSizeAction.triggered.connect(self.changeFontSize)
        editMenu.addAction(fontSizeAction)
        # 添加视图菜单
        viewMenu = QMenu('视图', self)
        self.menuBar.addMenu(viewMenu)
        # 添加深色模式菜单项
        darkModeAction = QAction('深色模式', self)
        darkModeAction.setShortcut('Ctrl+D')
        darkModeAction.triggered.connect(self.toggleDarkMode)
        viewMenu.addAction(darkModeAction)
        # 显示窗口
        self.show()
    def newFile(self):
        # 清空文本编辑框
        self.textEdit.clear()
    def openFile(self):
        # 打开文件对话框并读取文件内容到文本编辑框
        fileName, _ = QFileDialog.getOpenFileName(self, '打开文件', '', '文本文件 (*.txt);;所有文件 (*.*)')
        if fileName:
            with open(fileName, 'r', encoding='utf-8') as f:
                self.textEdit.setText(f.read())
    def saveFile(self):
        # 打开文件对话框并将文本编辑框内容保存到文件中
        fileName, _ = QFileDialog.getSaveFileName(self, '保存文件', '', '文本文件 (*.txt);;所有文件 (*.*)')
        if fileName:
            with open(fileName, 'w', encoding='utf-8') as f:
                f.write(self.textEdit.toPlainText())
    def toggleBold(self):
        # 切换粗体
        if self.textEdit.fontWeight() == QFont.Normal:
            self.textEdit.setFontWeight(QFont.Bold)
        else:
            self.textEdit.setFontWeight(QFont.Normal)
    def toggleItalic(self):
        # 切换斜体
        self.textEdit.setFontItalic(not self.textEdit.fontItalic())
    def changeFont(self):
        # 修改字体
        font, ok = QFontDialog.getFont(self.textEdit.font(), self)
        if ok:
            self.textEdit.setFont(font)
    def changeFontSize(self):
        # 修改字号
        size, ok = QInputDialog.getInt(self, '字号', '请输入字号:', self.textEdit.fontPointSize(), 1, 100, 1)
        if ok:
            font = QFont(self.textEdit.font())
            font.setPointSize(size)
            self.textEdit.setFont(font)
    def toggleDarkMode(self):
        # 切换深色模式
        if self.textEdit.styleSheet() == '':
            self.textEdit.setStyleSheet('background-color: #222; color: #fff')
        else:
            self.textEdit.setStyleSheet('')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextEditor()
    sys.exit(app.exec_())
