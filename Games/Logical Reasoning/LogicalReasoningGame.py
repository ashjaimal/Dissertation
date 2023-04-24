import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QRadioButton, QPushButton, QHBoxLayout

class DeductivePuzzleGame(QMainWindow):
    def __init__(self, main_menu_callback=None):
        super().__init__()

        self.main_menu_callback = main_menu_callback

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Deductive Puzzle Game')
        self.setFixedSize(600, 600)

        layout = QVBoxLayout()

        self.clues_label = QLabel("1. Alice is not first.\n2. Bob is not last.\n3. Carol is in the middle.")
        layout.addWidget(self.clues_label)

        self.options = {
            "A": ["Alice", "Bob", "Carol"],
            "B": ["Bob", "Alice", "Carol"],
            "C": ["Carol", "Alice", "Bob"],
            "D": ["Alice", "Carol", "Bob"]
        }

        self.radio_buttons = {}
        for option, names in self.options.items():
            radio_button = QRadioButton(f"{option}: {', '.join(names)}")
            self.radio_buttons[option] = radio_button
            layout.addWidget(radio_button)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_answer)
        layout.addWidget(self.submit_button)

        self.score_label = QLabel("Score: 0")
        layout.addWidget(self.score_label)

        self.main_menu_button = QPushButton("Return to Main Menu")
        self.main_menu_button.clicked.connect(self.return_to_main_menu)
        layout.addWidget(self.main_menu_button)

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

        self.score = 0

    def check_answer(self):
        correct_option = "B"
        for option, radio_button in self.radio_buttons.items():
            if radio_button.isChecked() and option == correct_option:
                self.score += 1
                self.score_label.setText(f"Score: {self.score}")
                break

    def return_to_main_menu(self):
        if self.main_menu_callback:
            self.main_menu_callback()
            self.hide()


def main():
    app = QApplication(sys.argv)
    game = DeductivePuzzleGame()
    game.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
