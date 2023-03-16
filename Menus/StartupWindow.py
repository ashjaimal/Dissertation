'''
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Now you can import Login
from Account_System import LoginWindow

from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton)
from PyQt5.QtCore import Qt

class MenuScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.login_window = None
        self.register_window = None
        self.settings_window = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Main Menu')
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        # Title
        title = QLabel('Menu')
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Login button
        login_button = QPushButton('Login')
        layout.addWidget(login_button)
        login_button.clicked.connect(self.show_login)

        # Register button
        register_button = QPushButton('Register')
        layout.addWidget(register_button)
        register_button.clicked.connect(self.show_register)

        # Settings button
        settings_button = QPushButton('\u2699')
        settings_button.setFixedSize(40, 40)
        settings_button.clicked.connect(self.show_settings)
        layout.setAlignment(settings_button, Qt.AlignBottom | Qt.AlignRight)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            * {
                font-family: "Segoe UI";
                font-size: 14px;
            }
            QLabel {
                font-size: 24px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #5c9efe;
                color: white;
                padding: 10px 20px;
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

    def show_login(self):
        if self.login_window is None:
            self.login_window = Login.LoginWindow()
        self.login_window.show()
        self.hide()

    def show_register(self):
        if self.register_window is None:
            self.register_window = RegisterWindow()
        self.register_window.show()
        self.hide()

    def show_settings(self):
        if self.settings_window is None:
            self.settings_window = SettingsWindow()
            self.settings_window.back_signal.connect(self.show)
        self.settings_window.show()
        self.hide()

def main():
    app = QApplication(sys.argv)
    menu_screen = MenuScreen()
    menu_screen.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    '''


import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton)
from PyQt5.QtCore import Qt
from Account_System.LoginWindow import LoginWindow
from Account_System.RegisterWindow import RegisterWindow

class StartupWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.login_window = None
        self.register_window = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Startup Window')
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        login_button = QPushButton('Login')
        layout.addWidget(login_button)
        login_button.clicked.connect(self.show_login)

        register_button = QPushButton('Register')
        layout.addWidget(register_button)
        register_button.clicked.connect(self.show_register)

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
                       font-size: 24px;
                       font-weight: bold;
                   }
                   QPushButton {
                       background-color: #5c9efe;
                       color: white;
                       padding: 10px 20px;
                       border: 1px solid #5c9efe;
                       border-radius: 5px;
                   }
                   QPushButton:hover {
                       background-color: #6eb5ff;
                       border-color: #6eb5ff;
                   }
                   QPushButton:pressed {
                       background-color: #A8A7A7;
                       border-color: #A8A7A7;
                   }
               """)

    def show_login(self):
        if self.login_window is None:
            self.login_window = LoginWindow()
            self.login_window.back_signal.connect(self.show)
        self.login_window.show()
        self.hide()

    def show_register(self):
        if self.register_window is None:
            self.register_window = RegisterWindow()
            self.register_window.back_signal.connect(self.show_and_close_register)
        self.register_window.show()
        self.hide()

    def show_and_close_register(self):
        self.register_window.hide()
        self.show()

def main():
    app = QApplication(sys.argv)
    startup_window = StartupWindow()
    startup_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
