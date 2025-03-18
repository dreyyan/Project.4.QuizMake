from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class DeleteQuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("delete_quiz.ui", self)
        self.setWindowTitle("Delete Quiz")
        self.setFixedSize(800, 560)

def run(parent):
    parent.delete_quiz_window = DeleteQuizWindow()
    parent.delete_quiz_window.show()
