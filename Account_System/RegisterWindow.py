'''
@Author: Ashwin Jaimal
@Date: 27/11/21
@About: Class to register for an account which stores it in a database
'''
import logging
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QVBoxLayout, QWidget

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
import pyodbc
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from Menus.MainMenu import MainMenu

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
                font-color: #FFFFFF;
                background-color: #363636;

            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: white;
            }
            QLineEdit, QComboBox, QDateEdit {
                padding: 5px 10px;
                border: 1px solid #cccccc;
                border-radius: 5px;
                color: white;
            }
            QPushButton {
                background-color: #5c9efe;
                color: white;
                padding: 10px 20px;
                border: 1px solid #5c9efe;
                border-radius: 5px;
                color: white;
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

    #logging.basicConfig(filename='user_management.log', level=logging.DEBUG,
                      #  format='%(asctime)s - %(levelname)s - %(message)s')

    #def register_user(username, password):
      #  logging.info('Attempting to register user: %s', username)

       # if registration_successful:
        #    logging.info('User %s successfully registered.', username)
       # else:
            #logging.error('User registration failed for %s.', username)

    def handle_registration(self):
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ASHWIN-DESKTOP\SQLEXPRESS;"
                              "Database=Brainiac;"
                              "Trusted_Connection=yes;")

        cursor = cnxn.cursor()
        cursor.execute(
            """INSERT INTO [Brainiac].[dbo].[userAccount] ([email],[passwrd],[first_name],[last_name],[gender],[date_of_birth]) VALUES (?,?,?,?,?,?)""",
            (self.email_input.text(), self.password_input.text(), self.first_name_input.text(), self.last_name_input.text(),
             self.gender_input.currentText(), self.dob_input.date().toPyDate()))
        cnxn.commit()
        cursor.close()
        cnxn.close()


def main():
    app = QApplication(sys.argv)
    register_window = RegisterWindow()
    register_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
