import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

def show():
    QMessageBox.information(None, "Message", "Hello!")

b = QPushButton("Click Me")
b.clicked.connect(show)
b.resize(200,60)
b.show()

sys.exit(app.exec())