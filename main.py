import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
# Python files
import start, subjects
import statistics, settings, help, exit_app
# Remove warnings
import warnings
# Shadow
warnings.simplefilter("ignore", category=DeprecationWarning)
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self) # Load the UI file directly
        self.setWindowTitle("QuizMake (v1.0)") # Override window title
        self.setFixedSize(800, 520) # Override window size

        # Connect buttons
        self.b_start.clicked.connect(lambda: start.run(self))
        self.b_subjects.clicked.connect(lambda: subjects.run(self))
        self.b_statistics.clicked.connect(lambda: statistics.run(self))
        self.b_settings.clicked.connect(lambda: settings.run(self))
        self.b_help.clicked.connect(lambda: help.run(self))
        self.b_exit.clicked.connect(lambda: exit_app.run(self))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
