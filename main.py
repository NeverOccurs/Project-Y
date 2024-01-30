import sys
from PyQt6.QtWidgets import QApplication
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Read the style sheet file
    with open('style.qss', 'r') as file:
        style_sheet = file.read()
    
    # Apply the style sheet
    app.setStyleSheet(style_sheet)
    
    # Create and show your main window
    main_win = MainWindow()
    main_win.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
