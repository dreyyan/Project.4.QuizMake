from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QApplication
from PyQt6 import uic

class ExitAppWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("exit_app.ui", self)
        self.setWindowTitle("Exit")

        # Find the button box in the UI
        self.button_box = self.findChild(QDialogButtonBox, "bbox")

        # Connect buttons to functions
        self.button_box.accepted.connect(self.on_ok_clicked)
        self.button_box.rejected.connect(self.on_cancel_clicked)

    def on_ok_clicked(self):
        QApplication.quit() # Exit app
        self.accept() # Close dialog and return accepted state

    def on_cancel_clicked(self):
        self.reject() # Close dialog and return rejected state

def run(parent):
    parent.exit_app_window = ExitAppWindow()
    parent.exit_app_window.exec() # Use .exec() for QDialog instead of .show()
