import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
# Python files
import new_quiz, delete_quiz, load_quiz, save_quiz
import statistics, settings, help, exit_app
# Remove warnings
import warnings
# Shadow
warnings.simplefilter("ignore", category=DeprecationWarning)
from PyQt6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self) # Load the UI file directly
        self.setWindowTitle("QuizMake (v1.0)") # Override window title
        self.setFixedSize(800, 520) # Override window size

        # Shadow Effect: l_main_menu
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(44, 111, 199, 180)) # Gray shadow with transparency
        self.l_main_menu.setGraphicsEffect(shadow)

        # Connect buttons
        self.b_new_quiz.clicked.connect(lambda: new_quiz.run(self))
        self.b_delete_quiz.clicked.connect(lambda: delete_quiz.run(self))
        self.b_load_quiz.clicked.connect(lambda: load_quiz.run(self))
        self.b_save_quiz.clicked.connect(lambda: save_quiz.run(self))
        self.b_statistics.clicked.connect(lambda: statistics.run(self))
        self.b_settings.clicked.connect(lambda: settings.run(self))
        self.b_help.clicked.connect(lambda: help.run(self))
        self.b_exit.clicked.connect(lambda: exit_app.run(self))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
