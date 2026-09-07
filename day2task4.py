import sys
from PyQt6.QtWidgets import *
app = QApplication(sys.argv)
w = QWidget()
e = QLineEdit()
l = QLabel()

def check():
    if int(e.text()) >= 35:
        l.setText("Pass")
    else:
        l.setText("Fail")

b = QPushButton("Check")
b.clicked.connect(check)

v = QVBoxLayout()
v.addWidget(e)
v.addWidget(b)
v.addWidget(l)

w.setLayout(v)
w.show()

sys.exit(app.exec())