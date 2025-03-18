from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("help.ui", self)
        self.setWindowTitle("Help")
        self.setFixedSize(800, 560)

def run(parent):
    parent.help_window = HelpWindow()
    parent.help_window.show()
