import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *

sys.path.insert(1,'X:\\HydraWebBuilder\Engine')

import data 
import hgen

class Setup(QWidget):
    def __init__(self):
        super().__init__()
        #self.setFixedSize(QSize(900,600))
        
        self.canonical = QLineEdit()
        self.poster = QLineEdit()
        self.logo = QLineEdit()
        self.title = QLineEdit()
        self.publisher = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(QLabel("Canonical Link:"),0,0,1,2)
        layout.addWidget(self.canonical,0,2,1,3)
        layout.addWidget(self.title,2,0,1,2)
        layout.addWidget(self.poster,2,3,1,2)
        layout.addWidget(self.publisher,4,0,1,2)
        layout.addWidget(self.logo,4,3,1,2)
        layout.addWidget(QLabel("Title:"),1,0,1,1)
        layout.addWidget(QLabel("Poster:"),1,3,1,1)
        layout.addWidget(QLabel("Publisher:"),3,0,1,1)
        layout.addWidget(QLabel("Logo:"),3,3,1,1)

        self.setLayout(layout)
        self.show()

    def getData(self):
        a = self.canonical.text()
        b = self.title.text()
        c = self.publisher.text()
        d = self.poster.text()
        e = self.logo.text()

        self.data = data.Start(a,b,c,d,e)
        

def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    wid = Setup()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()