import sys
from PyQt6.QtWidgets import *

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.count=0
        self.setWindowTitle("Simple Calculator")
        self.resize(300,200)

        self.label=QLabel(str(self.count))

        self.inc_btn=QPushButton("Increment")
        self.dec_btn=QPushButton("Decrement")

        self.inc_btn.clicked.connect(self.increment)
        self.dec_btn.clicked.connect(self.decrement)
        hbox=QHBoxLayout()
        hbox.addWidget(self.inc_btn)
        hbox.addWidget(self.dec_btn)

        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def increment(self):
        self.count+=1
        self.label.setText(str(self.count))
    def decrement(self):
        self.count-=1
        self.label.setText(str(self.count))

app=QApplication(sys.argv)
window=CounterApp()
window.show()
sys.exit(app.exec())