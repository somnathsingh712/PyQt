import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog
)
from PyQt6.QtGui import QAction


class Demo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text = QTextEdit()
        self.setCentralWidget(self.text)

        self.createMenu()
        self.statusBar().showMessage("Ready")

        self.saveConfig()
        self.loadConfig()

    def createMenu(self):
        menu = self.menuBar().addMenu("File")

        openAct = QAction("Open", self)
        openAct.triggered.connect(self.openFile)
        menu.addAction(openAct)

        saveAct = QAction("Save", self)
        saveAct.triggered.connect(self.saveFile)
        menu.addAction(saveAct)

        exitAct = QAction("Exit", self)
        exitAct.triggered.connect(self.close)
        menu.addAction(exitAct)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File")

        if fileName:
            with open(fileName, "r") as file:
                self.text.setText(file.read())

            self.statusBar().showMessage("File Opened")

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File")

        if fileName:
            with open(fileName, "w") as file:
                file.write(self.text.toPlainText())

            self.statusBar().showMessage("File Saved")

    def saveConfig(self):
        data = {"title": "Data Viewer"}

        with open("config.json", "w") as file:
            json.dump(data, file)

    def loadConfig(self):
        with open("config.json", "r") as file:
            data = json.load(file)

        self.setWindowTitle(data["title"])


app = QApplication(sys.argv)

win = Demo()
win.resize(600, 400)
win.show()

sys.exit(app.exec())