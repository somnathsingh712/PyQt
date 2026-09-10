import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt6.QtGui import QAction


class DataViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Title and Size
        self.setWindowTitle("PyQt5 Data Viewer")
        self.setGeometry(200, 200, 800, 500)

        # Central Text Area
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Menu Bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")

        # Exit Action
        exitAction = QAction("Exit", self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Status Bar
        self.statusBar().showMessage("Ready")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataViewer()
    window.show()
    sys.exit(app.exec())