import sys
from PyQt6.QtWidgets import *

class TempConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temperature Converter")
        self.resize(300, 200)

        self.label1 = QLabel("Celsius:")
        self.celsius = QLineEdit()

        self.button = QPushButton("Convert")
        self.result = QLabel("Fahrenheit: ")

        self.button.clicked.connect(self.convert)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.celsius)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def convert(self):
        c = float(self.celsius.text())
        f = (c * 9 / 5) + 32
        self.result.setText(f"Fahrenheit: {f:.2f}")

app = QApplication(sys.argv)
window = TempConverter()
window.show()
sys.exit(app.exec())