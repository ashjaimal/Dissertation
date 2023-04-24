'''
@Author: Ashwin Jaimal
@Date: 27/11/21
@About: Class to register and login with user accounts for the project
'''


from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
import sys
import pyodbc

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
import pyodbc
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from Menus.MainMenu import MainMenu


class LoginWindow(QMainWindow):
    back_signal = pyqtSignal()

    MainMenu = None

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

        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        password_label = QLabel('Password')
        layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        login_button = QPushButton('Log in')
        login_button.clicked.connect(self.handle_login)
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

    def show_mainMenu(self):
        if self.MainMenu is None:
            self.MainMenu = MainMenu()
            self.MainMenu.back_signal.connect(self.show)
        self.MainMenu.show()
        self.hide()

    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=ASHWIN-DESKTOP\SQLEXPRESS;"
                              "Database=Brainiac;"
                              "Trusted_Connection=yes;")
        cursor = cnxn.cursor()
        cursor.execute("SELECT [email], [passwrd] FROM [Brainiac].[dbo].[userAccount] WHERE [email] = ? AND [passwrd] = ?", (email, password))
        result = cursor.fetchone()
        cursor.close()
        cnxn.close()

        if result:
            print("Logged in")
            self.show_mainMenu()
        else:
            print("Invalid credentials")

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