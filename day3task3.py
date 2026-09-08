import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

w = QWidget()

username_input = QLineEdit()
username_input.setPlaceholderText("Username")

password_input = QLineEdit()
password_input.setEchoMode(QLineEdit.EchoMode.Password)

login_button = QPushButton("Login")

def login():
    username = username_input.text().strip()
    password = password_input.text()

    if username == "" or password == "":
        QMessageBox.warning(w, "Warning", "Input is missing")
    else:
        QMessageBox.information(w, "Success", "Login validation passed")

login_button.clicked.connect(login)

layout = QVBoxLayout()
layout.addWidget(username_input)
layout.addWidget(password_input)
layout.addWidget(login_button)

w.setLayout(layout)
w.setWindowTitle("Login Validation")
w.resize(300, 150)
w.show()

sys.exit(app.exec())