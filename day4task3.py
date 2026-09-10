import sys
from PyQt6.QtWidgets import *

class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit()
        self.setCentralWidget(self.text)

        menu = self.menuBar().addMenu("File")
        menu.addAction("Save", self.saveFile)

    def saveFile(self):
        file, _ = QFileDialog.getSaveFileName(self, "Save", "", "Text Files (*.txt)")
        if file:
            open(file, "w").write(self.text.toPlainText())

app = QApplication(sys.argv)
win = Demo()
win.show()
sys.exit(app.exec())