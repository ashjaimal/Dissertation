import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt

class AnagramGame(QMainWindow):
    def __init__(self, main_menu_callback=None):
        super().__init__()

        self.main_menu_callback = main_menu_callback

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Anagram Game')
        self.setFixedSize(800, 600)

        layout = QVBoxLayout()

        self.score_label = QLabel('Score: 0')
        layout.addWidget(self.score_label)

        self.level_label = QLabel()
        layout.addWidget(self.level_label, alignment=Qt.AlignCenter)

        self.anagram_label = QLabel()
        layout.addWidget(self.anagram_label, alignment=Qt.AlignCenter)

        self.user_input = QLineEdit()
        layout.addWidget(self.user_input)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.check_answer)
        layout.addWidget(self.submit_button)

        self.main_menu_button = QPushButton('Return to Main Menu')
        self.main_menu_button.clicked.connect(self.return_to_main_menu)
        layout.addWidget(self.main_menu_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            * {
                font-family: "Segoe UI";
                font-size: 18px;
                background-color: #363636;
                color: #FFFFFF;
            }
            QLabel {
                font-size: 24px;
                font-weight: bold;
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

        self.words = [
            ('easy', ['apple', 'table', 'chair']),
            ('medium', ['jungle', 'paradox', 'factory']),
            ('hard', ['capricious', 'conundrum', 'enigmatic']),
        ]

        self.current_level = 1
        self.score = 0
        self.start_level()

    def start_level(self):
        self.level_label.setText(f'Level {self.current_level}')
        difficulty, words = self.words[self.current_level - 1]
        self.current_word = random.choice(words)
        self.current_anagram = ''.join(random.sample(self.current_word, len(self.current_word)))
        self.anagram_label.setText(self.current_anagram)

    def check_answer(self):
        if self.user_input.text().lower() == self.current_word.lower():
            self.score += 1
            self.score_label.setText(f'Score: {self.score}')
            self.next_level()
        else:
            self.score_label.setText(f'Score: {self.score} - Incorrect')

    def next_level(self):
        self.current_level += 1
        if self.current_level <= 5:
            self.start_level()
        else:
            self.level_label.setText('You have completed all levels!')
            self.anagram_label.setText('')

    def return_to_main_menu(self):
        if self.main_menu_callback:
            self.main_menu_callback()
            self.hide()

def main(main_menu_callback=None):
    app = QApplication(sys.argv)
    anagram_game = AnagramGame(main_menu_callback)
    anagram_game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()