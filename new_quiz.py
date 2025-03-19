from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
# Shadow
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class NewQuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("new_quiz.ui", self)
        self.setWindowTitle("New Quiz")
        self.setFixedSize(800, 520)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.new_quiz_window = NewQuizWindow()
    parent.new_quiz_window.show()
