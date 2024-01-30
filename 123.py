import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 垂直布局
        layout = QVBoxLayout()

        # 创建控件
        self.inputField = QLineEdit(self)
        self.sendButton = QPushButton('发送', self)
        self.responseArea = QTextEdit(self)

        # 添加控件到布局
        layout.addWidget(self.inputField)
        layout.addWidget(self.sendButton)
        layout.addWidget(self.responseArea)

        # 设置主布局
        self.setLayout(layout)

        # 设置窗口的属性
        self.setWindowTitle('Project Y - Chat with LLM')
        self.setGeometry(300, 300, 350, 250)

def main():
    app = QApplication(sys.argv)
    
    # 在这里设置应用的样式
    app.setStyle('macintosh')
    
    chatApp = ChatApp()
    chatApp.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
