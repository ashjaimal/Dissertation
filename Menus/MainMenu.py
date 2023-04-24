import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt
from SettingsWindow import SettingsWindow  # Make sure to create this file as per the provided instructions


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings_window = None
        self.memory_game = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Main Menu')
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        # Title
        title = QLabel('Welcome')
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Buttons
        button_layout = QHBoxLayout()

        memory_button = QPushButton('Memory')
        memory_button.clicked.connect(self.show_memory_game)
        button_layout.addWidget(memory_button)

        reaction_button = QPushButton('Reaction')
        button_layout.addWidget(reaction_button)

        layout.addLayout(button_layout)

        button_layout2 = QHBoxLayout()

        verbal_reasoning_button = QPushButton('Verbal Reasoning')
        button_layout2.addWidget(verbal_reasoning_button)

        logical_reasoning_button = QPushButton('Logical Reasoning')
        button_layout2.addWidget(logical_reasoning_button)

        layout.addLayout(button_layout2)

        # Settings button
        settings_button = QPushButton('\u2699')
        settings_button.setFixedSize(40, 40)
        settings_button.clicked.connect(self.show_settings)
        layout.addWidget(settings_button, alignment=Qt.AlignBottom | Qt.AlignRight)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            * {
                font-family: "Segoe UI";
                color: #FFFFFF;
                font-size: 18px;
                background-color: #363636;

            }
            QLabel {
                font-size: 24px;
                font-weight: bold;
                colour: #FFFFFF;
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

    def show_settings(self):
        if self.settings_window is None:
            self.settings_window = SettingsWindow(self.show)
        self.settings_window.show()
        self.hide()

    def show_memory_game(self):
        if hasattr(self, 'memory_game') and self.memory_game:
            self.memory_game.show()
        else:
            from Memory.Memory import main as memory_game_main
            self.memory_game = memory_game_main(self.show)
        self.hide()


def main():
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

