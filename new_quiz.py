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

        # Shadow Effect: l_new_quiz
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(44, 111, 199, 180)) # Gray shadow with transparency
        self.l_new_quiz.setGraphicsEffect(shadow)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.new_quiz_window = NewQuizWindow()
    parent.new_quiz_window.show()
