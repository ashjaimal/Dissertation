'''
@Author: Ashwin Jaimal
@Date: 27/11/21
@About: Class to register and login with user accounts for the project
'''

import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer, QCoreApplication

class ReactionGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Reaction Time Game')

        layout = QVBoxLayout()

        self.start_time = None
        self.button = QPushButton('Click when GREEN')
        self.button.setStyleSheet('background-color: red')
        layout.addWidget(self.button)

        self.label = QLabel('')
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.button.clicked.connect(self.check_reaction_time)

        # Set up a timer to change the button color
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_button_color)
        self.timer.start(random.randint(1000, 5000))  # Randomly wait between 1 to 5 seconds

    def change_button_color(self):
        self.button.setStyleSheet('background-color: green')
        self.start_time = time.time()
        self.timer.stop()

    def check_reaction_time(self):
        if self.start_time:
            reaction_time = time.time() - self.start_time
            self.label.setText(f'Reaction time: {reaction_time:.2f} seconds')
            self.start_time = None

            # Restart the game after a short delay
            QTimer.singleShot(3000, self.restart_game)
        else:
            self.label.setText('Clicked too early!')

    def restart_game(self):
        self.label.setText('')
        self.button.setStyleSheet('background-color: red')
        self.timer.start(random.randint(1000, 5000))

def main():
    app = QApplication(sys.argv)
    game = ReactionGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()