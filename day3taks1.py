import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

u = QLineEdit()
p = QLineEdit()
b = QPushButton("Login")

def check():
    if u.text()=="" or p.text()=="":
        QMessageBox.warning(None,"Warning","Input Missing")
    else:
        QMessageBox.information(None,"Success","Login Validation Passed")

b.clicked.connect(check)

v = QVBoxLayout()
v.addWidget(u)
v.addWidget(p)
v.addWidget(b)

w = QWidget()
w.setLayout(v)
w.show()

sys.exit(app.exec())