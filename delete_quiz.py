from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
# Shadow
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class DeleteQuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("delete_quiz.ui", self)
        self.setWindowTitle("Delete Quiz")
        self.setFixedSize(800, 520)

        # Shadow Effect: l_delete_quiz
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(44, 111, 199, 180)) # Gray shadow with transparency
        self.l_delete_quiz.setGraphicsEffect(shadow)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.delete_quiz_window = DeleteQuizWindow()
    parent.delete_quiz_window.show()
