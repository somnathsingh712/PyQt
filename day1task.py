import sys
from PyQt6.QtWidgets import *
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("My PyQt App")
window.resize(300,150)
label=QLabel("Hello PyQt!")

layout=QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.show()
sys.exit(app.exec())