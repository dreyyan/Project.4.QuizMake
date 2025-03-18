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

        # Shadow Effect: l_save_quiz
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(44, 111, 199, 180)) # Gray shadow with transparency
        self.l_save_quiz.setGraphicsEffect(shadow)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.save_quiz_window = SaveQuizWindow()
    parent.save_quiz_window.show()
