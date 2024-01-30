# gui.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QMessageBox, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

class FloatingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.Tool | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # 设置悬浮窗口的大小和位置（根据需要调整）
        self.setGeometry(100, 100, 200, 50)
        self.doubleClicked = False
        self.initUI()

    def initUI(self):
        self.label = QLabel('双击我', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("QWidget { background-color: %s; }" % QColor(200, 200, 200, 150).name())
        self.resize(200, 50)

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked = True
        self.popUpWindow()

    def popUpWindow(self):
        if self.doubleClicked:
            # 弹出输入框和按钮
            self.inputField = QLineEdit(self)
            self.settingButton = QPushButton('设置', self)
            self.closeButton = QPushButton('关闭', self)
            # 布局
            layout = QVBoxLayout()
            layout.addWidget(self.inputField)
            layout.addWidget(self.settingButton)
            layout.addWidget(self.closeButton)
            self.setLayout(layout)
            # 连接关闭按钮的点击事件
            self.closeButton.clicked.connect(self.confirmClose)
            # 显示控件
            self.show()

    def confirmClose(self):
        reply = QMessageBox.question(self, '确认', '您确定要退出吗？', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()


def main():
    app = QApplication(sys.argv)
    floating_widget = FloatingWidget()
    floating_widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
