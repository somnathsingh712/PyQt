import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction

class Demo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text = QTextEdit()
        self.setCentralWidget(self.text)

        menu = self.menuBar().addMenu("File")

        openAct = QAction("Open", self)
        openAct.triggered.connect(self.openFile)
        menu.addAction(openAct)

        saveAct = QAction("Save", self)
        saveAct.triggered.connect(self.saveFile)
        menu.addAction(saveAct)

        self.statusBar().showMessage("Ready")

    def openFile(self):
        self.statusBar().showMessage("File Opened")

    def saveFile(self):
        self.statusBar().showMessage("File Saved")

app = QApplication(sys.argv)
win = Demo()
win.show()
sys.exit(app.exec())