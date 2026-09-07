import sys
# from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtWidgets import *
app=QApplication(sys.argv)
window=QWidget()
# label=QLabel("Hello Som")
window.setWindowTitle("My Empty Title")
window.show()
sys.exit(app.exec())