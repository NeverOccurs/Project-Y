import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFrame
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Create custom title bar
        self.title_bar = QLabel('X', self)  # Add a custom close button
        self.title_bar.setFixedWidth(20)
        self.title_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_bar.mousePressEvent = self.close_application

        # Create input field
        self.input_field = QLineEdit('Input text here...', self)

        # Create buttons
        self.send_button = QPushButton('Send', self)
        self.settings_button = QPushButton('Settings', self)

        # Arrange widgets horizontally
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.title_bar)
        self.hbox.addWidget(self.input_field)
        self.hbox.addWidget(self.send_button)
        self.hbox.addWidget(self.settings_button)

        # Set the main layout
        self.setLayout(self.hbox)

    def close_application(self, event):
        self.close()
