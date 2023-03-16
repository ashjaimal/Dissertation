'''
@Author: Ashwin Jaimal
@Date: 27/11/21
@About: Class to register for an account which stores it in a database
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QVBoxLayout, QWidget

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal

class RegisterWindow(QMainWindow):
    back_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Registration App')
        self.setFixedSize(600, 600)
        layout = QVBoxLayout()

        # Create input fields and labels
        self.first_name_label = QLabel('First Name:')
        self.first_name_input = QLineEdit()
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)

        self.last_name_label = QLabel('Last Name:')
        self.last_name_input = QLineEdit()
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.gender_label = QLabel('Gender:')
        self.gender_input = QComboBox()
        self.gender_input.addItems(['Select Gender', 'Male', 'Female', 'Other'])
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)

        self.dob_label = QLabel('Date of Birth:')
        self.dob_input = QDateEdit()
        layout.addWidget(self.dob_label)
        layout.addWidget(self.dob_input)

        self.register_button = QPushButton('Register')
        self.register_button.clicked.connect(self.handle_registration)
        layout.addWidget(self.register_button)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.back_signal.emit)
        layout.addWidget(self.back_button)

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
            QLineEdit, QComboBox, QDateEdit {
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

    def handle_registration(self):
        # Validate and store user data here
        pass

def main():
    app = QApplication(sys.argv)
    register_window = RegisterWindow()
    register_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
