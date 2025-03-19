from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
# Shadow
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("start.ui", self)
        self.setWindowTitle("Start")
        self.setFixedSize(800, 520)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.start_window = StartWindow()
    parent.start_window.show()
