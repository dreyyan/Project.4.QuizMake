from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
# Shadow
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class StatisticsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("statistics.ui", self)
        self.setWindowTitle("Statistics")
        self.setFixedSize(800, 520)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.statistics_window = StatisticsWindow()
    parent.statistics_window.show()
