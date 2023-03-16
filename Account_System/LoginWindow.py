'''
@Author: Ashwin Jaimal
@Date: 27/11/21
@About: Class to register and login with user accounts for the project
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
'''
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Login')
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        # Title
        title = QLabel('Login')
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Email input
        email_label = QLabel('Email')
        layout.addWidget(email_label)

        email_input = QLineEdit()
        layout.addWidget(email_input)

        # Password input
        password_label = QLabel('Password')
        layout.addWidget(password_label)

        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_input)

        # Login button
        login_button = QPushButton('Log in')
        layout.addWidget(login_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            * {
                font-family: "Segoe UI";
                font-size: 14px;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 5px 10px;
                border: 1px solid #cccccc;
                border-radius: 5px;
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


def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

class LoginWindow(QMainWindow):
    back_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Login')
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        title = QLabel('Login')
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        email_label = QLabel('Email')
        layout.addWidget(email_label)

        email_input = QLineEdit()
        layout.addWidget(email_input)

        password_label = QLabel('Password')
        layout.addWidget(password_label)

        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_input)

        login_button = QPushButton('Log in')
        layout.addWidget(login_button)

        back_button = QPushButton('Back')
        layout.addWidget(back_button)
        back_button.clicked.connect(self.back)

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
            }
            QLineEdit {
                padding: 5px 10px;
                border: 1px solid #cccccc;
                border-radius: 5px;
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

    def back(self):
        self.hide()
        self.back_signal.emit()

def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
