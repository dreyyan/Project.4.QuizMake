from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
# Shadow
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class SubjectsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("subjects.ui", self)
        self.setWindowTitle("Subjects")
        self.setFixedSize(800, 520)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.subjects_window = SubjectsWindow()
    parent.subjects_window.show()
