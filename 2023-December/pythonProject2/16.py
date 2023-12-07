import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget
class FileBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Browser')
        self.setGeometry(300, 300, 800, 600)
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath('')  # 设置根目录
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.file_model)
        self.tree_view.setRootIndex(self.file_model.index(''))  # 设置树视图的根索引
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tree_view)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_browser = FileBrowser()
    file_browser.show()
    sys.exit(app.exec_())