import sys
from PyQt6.QtWidgets import *
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("My PyQt App")
window.resize(300,200)
window.show()
sys.exit(app.exec())