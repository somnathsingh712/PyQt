import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Counter App")
window.resize(250, 200)

count = 0

label = QLabel("0")
label.setStyleSheet("font-size: 20px;")

inc_button = QPushButton("Increment")
dec_button = QPushButton("Decrement")

def increment():
    global count
    count += 1
    label.setText(str(count))

def decrement():
    global count
    count -= 1
    label.setText(str(count))

inc_button.clicked.connect(increment)
dec_button.clicked.connect(decrement)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(inc_button)
layout.addWidget(dec_button)

window.setLayout(layout)
window.show()

sys.exit(app.exec())