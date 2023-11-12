import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget, QMessageBox, QMenu, QAction
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
        self.tree_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.show_context_menu)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tree_view)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
    def show_context_menu(self, pos):
        index = self.tree_view.indexAt(pos)
        if index.isValid():
            menu = QMenu(self)
            open_action = QAction("打开", self)
            delete_action = QAction("删除", self)
            menu.addAction(open_action)
            menu.addAction(delete_action)
            open_action.triggered.connect(lambda: self.open_file(index))
            delete_action.triggered.connect(lambda: self.delete_file(index))
            menu.exec_(self.tree_view.viewport().mapToGlobal(pos))
    def open_file(self, index):
        file_path = self.file_model.filePath(index)
        if os.path.isfile(file_path):
            try:
                os.startfile(file_path)
            except OSError:
                QMessageBox.warning(self, "错误", "无法打开文件")
        else:
            QMessageBox.warning(self, "错误", "选择的不是文件")
    def delete_file(self, index):
        file_path = self.file_model.filePath(index)
        if os.path.isfile(file_path):
            reply = QMessageBox.question(self, "确认", "确定要删除文件吗？", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    os.remove(file_path)
                    self.file_model.refresh()  # 刷新文件视图
                except OSError:
                    QMessageBox.warning(self, "错误", "无法删除文件")
        else:
            QMessageBox.warning(self, "错误", "选择的不是文件")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_browser = FileBrowser()
    file_browser.show()
    sys.exit(app.exec_())import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QColorDialog, QFileDialog, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPointF


class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Drawing App')
        self.setGeometry(300, 300, 800, 600)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.setupToolBar()

        self.penColor = Qt.black
        self.penWidth = 2

    def setupToolBar(self):
        # 创建工具栏
        toolbar = self.addToolBar('Tools')

        # 创建画笔颜色选择动作
        colorAction = QAction('Pen Color', self)
        colorAction.triggered.connect(self.selectPenColor)
        toolbar.addAction(colorAction)

        # 创建画笔粗细选择动作
        widthAction = QAction('Pen Width', self)
        widthAction.triggered.connect(self.selectPenWidth)
        toolbar.addAction(widthAction)

        # 创建清除画布动作
        clearAction = QAction('Clear', self)
        clearAction.triggered.connect(self.clearCanvas)
        toolbar.addAction(clearAction)

    def selectPenColor(self):
        # 打开颜色选择对话框选择画笔颜色
        color = QColorDialog.getColor()
        if color.isValid():
            self.penColor = color

    def selectPenWidth(self):
        # 打开输入对话框输入画笔粗细
        width, ok = QInputDialog.getInt(self, 'Pen Width', 'Enter pen width:')
        if ok:
            self.penWidth = width

    def clearCanvas(self):
        # 清除画布上的图形
        self.scene.clear()

    def mousePressEvent(self, event):
        # 鼠标按下时开始绘制
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()

    def mouseReleaseEvent(self, event):
        # 鼠标释放时结束绘制
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.drawShape()

    def drawShape(self):
        # 根据起始点和终点绘制形状
        shape = QPainterPath()
        shape.moveTo(self.startPoint)
        shape.lineTo(self.endPoint)

        pen = QPen(self.penColor, self.penWidth)
        self.scene.addPath(shape, pen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    drawing_app = DrawingApp()
    drawing_app.show()
    sys.exit(app.exec_())
