import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox

class LightSwitchPuzzle(QMainWindow):
    def __init__(self, bulb_count=5):
        super().__init__()
        self.bulb_count = bulb_count
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Light Switch Puzzle')

        main_layout = QVBoxLayout()

        self.bulbs = [random.choice([True, False]) for _ in range(self.bulb_count)]
        self.switch_buttons = []

        bulb_layout = QHBoxLayout()
        for i in range(self.bulb_count):
            bulb_button = QPushButton('💡' if self.bulbs[i] else '🔌')
            bulb_button.setDisabled(True)
            bulb_layout.addWidget(bulb_button)

            switch_button = QPushButton('Toggle')
            switch_button.clicked.connect(lambda _, idx=i: self.toggle(idx))
            self.switch_buttons.append(switch_button)

        main_layout.addLayout(bulb_layout)

        switch_layout = QHBoxLayout()
        for switch_button in self.switch_buttons:
            switch_layout.addWidget(switch_button)

        main_layout.addLayout(switch_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            * {
                font-family: "Segoe UI";
                font-size: 14px;
            }
            QLabel, QPushButton:disabled {
                color: #555;
            }
            QPushButton {
                background-color: #5c9efe;
                color: white;
                padding: 5px 20px;
                border: 1px solid #5c9efe;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #6eb5ff;
                border-color: #6eb5ff;
            }
            QPushButton:pressed {
                background-color: #4a89dc;
                border-color: #4a89dc;
            }
        """)

    def toggle(self, idx):
        for i in range(idx - 1, idx + 2):
            if 0 <= i < self.bulb_count:
                self.bulbs[i] = not self.bulbs[i]
                self.switch_buttons[i].setText('💡' if self.bulbs[i] else '🔌')

        if all(self.bulbs):
            QMessageBox.information(self, 'Congratulations', 'You have turned on all the light bulbs!')

def main():
    app = QApplication(sys.argv)
    light_switch_puzzle = LightSwitchPuzzle()
    light_switch_puzzle.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()