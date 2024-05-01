import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *

sys.path.insert(1,'X:\\HydraWebBuilder\Engine')

import data 
import hgen

class PageOptions(QDialog):
    def __init__(self):
        super().__init__()
        self.plainTop = QPushButton("Plain Top")
        self.plainBottom = QPushButton("Plain Bottom")
        self.gradientTop = QPushButton("Gradient Top")
        self.gradientBottom = QPushButton("Gradient Bottom")

        

def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    wid = Setup()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()