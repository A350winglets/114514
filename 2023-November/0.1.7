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
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 300)

        self.initUI()

    def initUI(self):
        # 创建中心部件和布局
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)

        # 创建显示结果的文本框
        self.resultLineEdit = QLineEdit(self)
        self.resultLineEdit.setReadOnly(True)
        vbox.addWidget(self.resultLineEdit)

        # 创建按钮布局
        gridLayout = QGridLayout()
        vbox.addLayout(gridLayout)

        # 定义按钮的文本和位置
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        # 创建按钮并连接点击事件
        for btnText, row, col in buttons:
            button = QPushButton(btnText, self)
            button.clicked.connect(self.buttonClicked)
            gridLayout.addWidget(button, row, col)

    def buttonClicked(self):
        # 获取按钮对象
        button = self.sender()

        # 获取按钮的文本
        buttonText = button.text()

        # 如果按钮文本为'='，执行计算结果
        if buttonText == '=':
            try:
                result = eval(self.resultLineEdit.text())
                self.resultLineEdit.setText(str(result))
            except Exception as e:
                self.resultLineEdit.setText('Error')
        # 如果按钮文本为'AC'，清空文本框
        elif buttonText == 'AC':
            self.resultLineEdit.setText('')
        # 其他情况在文本框后追加按钮文本
        else:
            self.resultLineEdit.setText(self.resultLineEdit.text() + buttonText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
