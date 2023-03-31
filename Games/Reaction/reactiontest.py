'''
@Author: Ashwin Jaimal
@Date: 27/11/21
@About: Class to register and login with user accounts for the project
'''
import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt, QTimer


class ReactionGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.start_time = 0
        self.best_time = float('inf')

    def init_ui(self):
        self.setWindowTitle('Reaction Game')
        self.resize(500, 500)

        layout = QVBoxLayout()
        self.setStyleSheet("""background-color: #363636;""")
        # Reaction button
        self.reaction_button = QPushButton('Click me when green')
        self.reaction_button.setFixedSize(300, 300)
        self.reaction_button.setStyleSheet("""
            background-color: red;
            color: white;
            font-family: "Segoe UI";
            font-size: 24px;
            font-weight: bold;
            border: none;
        """)
        self.reaction_button.clicked.connect(self.handle_button_click)
        layout.addWidget(self.reaction_button, alignment=Qt.AlignCenter)

        # Result label
        self.result_label = QLabel('')
        self.result_label.setStyleSheet("font-family: 'Segoe UI'; font-size: 18px; color: #FFFFFF;")
        layout.addWidget(self.result_label, alignment=Qt.AlignCenter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.turn_button_green)
        self.timer.setSingleShot(True)
        self.timer.start(random.randint(2000, 5000))

    def turn_button_green(self):
        self.reaction_button.setStyleSheet("""
            background-color: green;
            color: white;
            font-family: "Segoe UI";
            font-size: 24px;
            font-weight: bold;
            border: none;
        """)
        self.start_time = time.time()

    def handle_button_click(self):
        if self.start_time == 0:
            return

        reaction_time = (time.time() - self.start_time) * 1000
        self.best_time = min(self.best_time, reaction_time)

        self.result_label.setText(f"Reaction Time: {reaction_time:.2f} ms | Best Time: {self.best_time:.2f} ms")

        self.reaction_button.setStyleSheet("""
            background-color: red;
            color: white;
            font-family: "Segoe UI";
            font-size: 24px;
            font-weight: bold;
            border: none;
        """)
        self.start_time = 0
        self.timer.start(random.randint(2000, 5000))


def main():
    app = QApplication(sys.argv)
    reaction_game = ReactionGame()
    reaction_game.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
