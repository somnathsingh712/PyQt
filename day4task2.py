import sys
from PyQt6.QtWidgets import *

class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit()
        self.setCentralWidget(self.text)
        menu = self.menuBar().addMenu("File")
        menu.addAction("Open", self.openFile)

    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open", "", "Text Files (*.txt)")
        if file:
            self.text.setText(open(file).read())

app = QApplication(sys.argv)
win = Demo()
win.show()
sys.exit(app.exec())