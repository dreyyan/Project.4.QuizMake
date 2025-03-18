from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class NewQuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("new_quiz.ui", self)
        self.setWindowTitle("New Quiz")
        self.setFixedSize(800, 560)

def run(parent):
    parent.new_quiz_window = NewQuizWindow()
    parent.new_quiz_window.show()
