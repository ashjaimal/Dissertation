import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer

class MemoryGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.sequence = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Memory Game')

        layout = QVBoxLayout()

        self.sequence_label = QLabel('')
        layout.addWidget(self.sequence_label)

        self.user_input = QLineEdit()
        layout.addWidget(self.user_input)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.check_answer)
        layout.addWidget(self.submit_button)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.start_game()

    def start_game(self):
        self.sequence = [random.randint(0, 9) for _ in range(self.level)]
        self.sequence_label.setText(' '.join(map(str, self.sequence)))
        self.user_input.clear()
        self.result_label.setText('')

        QTimer.singleShot(10000, self.hide_sequence)

    def hide_sequence(self):
        self.sequence_label.setText('Numbers hidden. Enter the sequence.')

    def check_answer(self):
        user_answer = list(map(int, self.user_input.text().split()))
        correct_count = sum(u == s for u, s in zip(user_answer, self.sequence))

        if user_answer == self.sequence:
            self.result_label.setText('Correct! Next level.')
            self.level += 1
            QTimer.singleShot(2000, self.start_game)
        else:
            self.result_label.setText(f'Incorrect. {correct_count} out of {self.level} correct.')

def main():
    app = QApplication(sys.argv)
    memory_game = MemoryGame()
    memory_game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()