import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('计算器')
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()
        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        grid_layout = QVBoxLayout()
        for i in range(4):
            row_layout = QVBoxLayout()
            for j in range(4):
                button = QPushButton(buttons[i * 4 + j])
                button.clicked.connect(self.button_clicked)
                row_layout.addWidget(button)
            grid_layout.addLayout(row_layout)
        layout.addLayout(grid_layout)
        self.setLayout(layout)
    def button_clicked(self):
        button = self.sender()
        text = button.text()
        if text == '=':
            expression = self.input_line.text()
            try:
                result = eval(expression)
                self.input_line.setText(str(result))
            except Exception as e:
                self.input_line.setText('Error')
        elif text == 'C':
            self.input_line.clear()
        else:
            self.input_line.setText(self.input_line.text() + text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
