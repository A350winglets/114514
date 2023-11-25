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
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:00:21 2022

@author: Student
"""

s=[]
a=int(input("列表项数="))
for i in range(1,a+1):
    s.append(int(input("项目=")))
a=s.__len__()
for i in range (1,a-1):
    if s[i]>s[i+1]:
        s[i],s[i+1]=s[i+1],s[i]
print(s)


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
    sys.exit(app.exec_())
