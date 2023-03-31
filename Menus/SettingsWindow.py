import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox, QPushButton,
                             QWidget, QHBoxLayout, QSlider, QCheckBox)
from PyQt5.QtCore import Qt, pyqtSignal

class SettingsWindow(QMainWindow):
    back_signal = pyqtSignal()

    def __init__(self, back_callback):
        super().__init__()

        self.init_ui()
        self.back_signal.connect(back_callback)

    def init_ui(self):
        self.setWindowTitle('Settings')
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()

        # Title
        title = QLabel('Settings')
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Graphics options
        graphics_label = QLabel('Graphics:')
        layout.addWidget(graphics_label)

        graphics_combobox = QComboBox()
        graphics_combobox.addItems(['Low', 'Medium', 'High', 'Ultra'])
        layout.addWidget(graphics_combobox)

        # Resolution options
        resolution_label = QLabel('Resolution:')
        layout.addWidget(resolution_label)

        resolution_combobox = QComboBox()
        resolution_combobox.addItems(['800x600', '1024x768', '1280x720', '1920x1080'])
        layout.addWidget(resolution_combobox)

        # Screen mode options
        screen_mode_label = QLabel('Screen mode:')
        layout.addWidget(screen_mode_label)

        screen_mode_combobox = QComboBox()
        screen_mode_combobox.addItems(['Fullscreen', 'Fullscreen Borderless', 'Windowed'])
        layout.addWidget(screen_mode_combobox)

        # Volume control
        bgm_label = QLabel('Background Music Volume:')
        layout.addWidget(bgm_label)

        bgm_slider = QSlider(Qt.Horizontal)
        layout.addWidget(bgm_slider)

        sfx_label = QLabel('SFX Volume:')
        layout.addWidget(sfx_label)

        sfx_slider = QSlider(Qt.Horizontal)
        layout.addWidget(sfx_slider)

        # Change language
        language_label = QLabel('Language:')
        layout.addWidget(language_label)

        language_combobox = QComboBox()
        language_combobox.addItems(['English', 'Spanish', 'French', 'German', 'Chinese'])
        layout.addWidget(language_combobox)

        # Back button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            * {
                font-family: "Segoe UI";
                color: #FFFFFF;
                font-size: 14px;
                background-color: #363636;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
            QComboBox {
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

    def go_back(self):
        self.hide()
        self.back_signal.emit()

def main():
    app = QApplication(sys.argv)
    settings_window = SettingsWindow()
    settings_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
