from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("settings.ui", self)
        self.setWindowTitle("Settings")
        self.setFixedSize(800, 560)

def run(parent):
    parent.settings_window = SettingsWindow()
    parent.settings_window.show()
