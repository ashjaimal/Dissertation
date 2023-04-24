import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

class MemoryGame(QMainWindow):
    def __init__(self, main_menu_callback):
        super().__init__()
        self.level = 1
        self.sequence = []
        self.main_menu_callback = main_menu_callback
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Memory Game')
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        font = QFont("Arial", 16)

        self.sequence_label = QLabel('')
        self.sequence_label.setFont(font)
        layout.addWidget(self.sequence_label)

        self.user_input = QLineEdit()
        self.user_input.setFont(font)
        layout.addWidget(self.user_input)

        self.submit_button = QPushButton('Submit')
        self.submit_button.setFont(font)
        self.submit_button.clicked.connect(self.check_answer)
        layout.addWidget(self.submit_button)

        self.result_label = QLabel('')
        self.result_label.setFont(font)
        layout.addWidget(self.result_label)

        self.restart_button = QPushButton('Restart')
        self.restart_button.setFont(font)
        self.restart_button.clicked.connect(self.restart_game)
        layout.addWidget(self.restart_button)

        self.return_button = QPushButton('Return to Main Menu')
        self.return_button.setFont(font)
        self.return_button.clicked.connect(self.return_to_main_menu)
        layout.addWidget(self.return_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setStyleSheet("""
                    * {
                        font-family: "Segoe UI";
                        font-size: 14px;
                        background-color: #363636;
                    }
                    QLabel {
                        font-size: 18px;
                        font-weight: bold;
                        color: white;

                    }
                    QLineEdit {
                        padding: 5px 10px;
                        border: 1px solid #cccccc;
                        border-radius: 5px;
                        color: white;

                    }
                    QPushButton {
                        background-color: #E8175D;
                        color: white;
                        padding: 10px 20px;
                        border: 1px solid #E8175D;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: #CC527A;
                        border-color: #CC527A;
                    }
                    QPushButton:pressed {
                        background-color: #A8A7A7;
                        border-color: #A8A7A7;
                    }
                """)
        self.start_game()

    def start_game(self):
        self.sequence = [random.randint(0, 9) for _ in range(self.level)]
        self.sequence_label.setText(' '.join(map(str, self.sequence)))
        self.user_input.clear()
        self.result_label.setText('')

        QTimer.singleShot(5000, self.hide_sequence)

    def hide_sequence(self):
        self.sequence_label.setText('Numbers hidden. Enter the sequence.')

    def check_answer(self):
        user_answer = list(map(int, self.user_input.text().split()))
        if user_answer == self.sequence:
            self.result_label.setText('Correct! Well done! Move onto the next level.')
            self.level += 1
            QTimer.singleShot(2000, self.start_game)
        else:
            self.result_label.setText(f'Incorrect. Game over. Your score: {self.level - 1}')

    def restart_game(self):
        self.level = 1
        self.start_game()

    def return_to_main_menu(self):
        self.main_menu_callback()
        self.hide()

def main(main_menu_callback):
    app = QApplication(sys.argv)
    memory_game = MemoryGame(main_menu_callback)
    memory_game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(None)
