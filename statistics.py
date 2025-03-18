from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class StatisticsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("statistics.ui", self)
        self.setWindowTitle("Statistics")
        self.setFixedSize(800, 560)

def run(parent):
    parent.statistics_window = StatisticsWindow()
    parent.statistics_window.show()
