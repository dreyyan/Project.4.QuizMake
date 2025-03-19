from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
# Shadow
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class SaveQuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("save_quiz.ui", self)
        self.setWindowTitle("Save Quiz")
        self.setFixedSize(800, 520)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.save_quiz_window = SaveQuizWindow()
    parent.save_quiz_window.show()
