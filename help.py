from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
# Shadow
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("help.ui", self)
        self.setWindowTitle("Help")
        self.setFixedSize(800, 520)

        # Shadow Effect: l_help
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(44, 111, 199, 180)) # Gray shadow with transparency
        self.l_help.setGraphicsEffect(shadow)

        # Button: Return
        self.b_return.clicked.connect(lambda: self.close())

def run(parent):
    parent.help_window = HelpWindow()
    parent.help_window.show()
