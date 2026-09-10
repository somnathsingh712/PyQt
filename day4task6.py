import sys
import json
from PyQt6.QtWidgets import *

class Demo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text = QTextEdit()
        self.setCentralWidget(self.text)

        self.saveConfig()
        self.loadConfig()

    def saveConfig(self):
        data = {"title": "My App"}
        with open("config.json", "w") as file:
            json.dump(data, file)

    def loadConfig(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        self.setWindowTitle(data["title"])

app = QApplication(sys.argv)
win = Demo()
win.show()
sys.exit(app.exec())