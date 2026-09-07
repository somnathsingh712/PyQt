import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

w = QWidget()
a = QLineEdit()
b = QLineEdit()
r = QLabel()

def calc():
    x = float(a.text())
    y = float(b.text())
    r.setText(f"+={x+y}\n-={x-y}\n*={x*y}\n/={x/y}")

btn = QPushButton("Calculate")
btn.clicked.connect(calc)

v = QVBoxLayout()
v.addWidget(a)
v.addWidget(b)
v.addWidget(btn)
v.addWidget(r)

w.setLayout(v)
w.show()

sys.exit(app.exec())