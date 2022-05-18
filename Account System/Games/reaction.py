import time
import random
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    def __int__(self):
        super().__init__()

        self.setWindowTitle("Reaction Speed Game")
        self.setGeometry(100,100,600,400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("Button " , self)
        button.setGeometry(200,200,100,40)

        button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : red;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : green;"
                             "}")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())














def reactionGame():
    print("WELCOME TO THE REACTION GAME")
    print("YOU SEE THE WORD GO HIT THE SPACEBAR")
    print("THE GAME WILL START IN 3 SECONDS")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")

    time.sleep(random.randint(1,5))
    print("GO")
    tic = time.perf_counter()
    a = input()
    tock = time.perf_counter()

    totalTime = tock - tic
    print("--------------------------------------")
    print("YOUR TIME WAS: ", totalTime, "SECONDS" )

def gui():
    app = QApplication(sys.argv)

    #frame set up
    window = QWidget()
    b = QLabel(window)
    b.setText("REACTION SPEED GAME")
    window.setGeometry(500,500,500,50)
    b.move(50,20)
    window.setWindowTitle("Reaction Speed Game")


    #font setup
    font = QFont()
    font.setFamily("Arial")
    font.setPointSize(20)
    b.setFont(font)

    buttonClick = QPushButton("Click")
    buttonClick.setGeometry(200, 150, 100, 40)
    buttonClick.setStyleSheet("background-color : green")
    buttonClick.clicked.connect(clickMe)


    window.show()
    sys.exit(app.exec())

def clickMe():
    print("pressed")


