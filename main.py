# main.py

import sys
from PyQt6.QtWidgets import QApplication
from gui import FloatingWidget

def main():
    app = QApplication(sys.argv)
    floating_widget = FloatingWidget()
    floating_widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
