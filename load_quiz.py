from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class LoadQuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("load_quiz.ui", self)
        self.setWindowTitle("Load Quiz")
        self.setFixedSize(800, 560)

def run(parent):
    parent.load_quiz_window = LoadQuizWindow()
    parent.load_quiz_window.show()
