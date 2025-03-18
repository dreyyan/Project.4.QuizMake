from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class SaveQuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("save_quiz.ui", self)
        self.setWindowTitle("Save Quiz")
        self.setFixedSize(800, 560)

def run(parent):
    parent.save_quiz_window = SaveQuizWindow()
    parent.save_quiz_window.show()
