from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
# Shadow
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class LoadQuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("load_quiz.ui", self)
        self.setWindowTitle("Load Quiz")
        self.setFixedSize(800, 520)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.load_quiz_window = LoadQuizWindow()
    parent.load_quiz_window.show()
