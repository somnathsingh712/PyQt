import sys
from PyQt6.QtWidgets import *
app=QApplication(sys.argv)
window=QMainWindow()
window.setWindowTitle("This is window")
window.resize(400,600)
window.show()
sys.exit(app.exec())