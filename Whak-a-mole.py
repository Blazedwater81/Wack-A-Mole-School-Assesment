import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
import random

class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Whack-a-mole")
        self.setFixedSize(500, 500)

        self.board = [[None for _ in range(4)] for _ in range(4)]

        grid_layout = QGridLayout()
        self.buttons = []
        for row in range(4):
            row_buttons = []
            for col in range(4):
                button = QPushButton()
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
                button.clicked.connect(lambda clicked, r=row, c=col: self.button_clicked(r, c))
                button.setFixedSize(75, 60)
                button.setStyleSheet("QPushButton { background-color: #808080; }")
            self.buttons.append(row_buttons)



        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(grid_layout)

    def button_clicked(self, row, col):
        print(f"({row}, {col})")

app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())