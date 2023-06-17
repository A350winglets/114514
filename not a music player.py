import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        openFile = QAction(QIcon('open.png'), '打开', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('打开新文件')
        openFile.triggered.connect(self.showDialog)
        saveFile = QAction(QIcon('save.png'), '保存', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('保存文件')
        saveFile.triggered.connect(self.saveDialog)
        boldButton = QAction(QIcon('bold.png'), '粗体', self)
        boldButton.setShortcut('Ctrl+B')
        boldButton.setStatusTip('加粗')
        boldButton.triggered.connect(self.bold)
        italicButton = QAction(QIcon('italic.png'), '斜体', self)
        italicButton.setShortcut('Ctrl+I')
        italicButton.setStatusTip('倾斜')
        italicButton.triggered.connect(self.italic)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        formatMenu = menubar.addMenu('格式')
        formatMenu.addAction(boldButton)
        formatMenu.addAction(italicButton)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('文本编辑器')
        self.show()
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', '/home')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
    def saveDialog(self):
        fname = QFileDialog.getSaveFileName(self, '保存文件', '/home')
        if fname[0]:
            f = open(fname[0], 'w')
            f.write(self.textEdit.toPlainText())
            f.close()
    def bold(self):
        if self.textEdit.fontWeight() == 50:
            self.textEdit.setFontWeight(75)
        else:
            self.textEdit.setFontWeight(50)
    def italic(self):
        state = self.textEdit.fontItalic()
        self.textEdit.setFontItalic(not state)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextEditor()
    sys.exit(app.exec_())
