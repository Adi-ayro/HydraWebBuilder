import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QAction

from builder import *

class PageOptions(QDialog):
    def __init__(self):
        super().__init__()
        self.clicked = None

        self.plainTop = QPushButton("Plain Top")
        self.plainBottom = QPushButton("Plain Bottom")
        self.gradientTop = QPushButton("Gradient Top")
        self.gradientBottom = QPushButton("Gradient Bottom")

        self.plainTop.clicked.connect(self.handle)
        self.plainBottom.clicked.connect(self.handle)  
        self.gradientTop.clicked.connect(self.handle)
        self.gradientBottom.clicked.connect(self.handle)

        layout = QGridLayout()
        layout.addWidget(self.plainTop,0,0)
        layout.addWidget(self.plainBottom,0,1)
        layout.addWidget(self.gradientTop,1,0)
        layout.addWidget(self.gradientBottom,1,1)

        self.setLayout(layout)
        self.show()
    
    def handle(self):
        self.clicked = self.sender().text()
        print(self.clicked)
        self.close()

    def getData(self):
        return self.clicked


class app(QMainWindow):
    def __init__(self):
        super().__init__()

        #Tab Builder
        self.tab_widget = QTabWidget()
        self.tab_widget.setMovable(True)
        #Cover = Builder()
        #Page1 = Builder()
        #self.tab_widget.addTab(Cover, "Cover")
        #self.tab_widget.addTab(Page1, "Page1")

        #Toolbar
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        self.n = 1
        new = QAction("New Page", self)
        new.triggered.connect(self.add)
        toolbar.addAction(new)

        curr = QAction("Index", self)
        curr.triggered.connect(self.index)
        toolbar.addAction(curr)

        remove = QAction("Delete Page", self)
        remove.triggered.connect(self.remove)
        toolbar.addAction(remove)

        export = QAction("Export", self)
        export.triggered.connect(self.export)
        toolbar.addAction(export)

        #Layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

    def add(self):
        print("clicked")
        fn = PageOptions()
        wait = fn.exec()

        self.tab_widget.addTab(Builder(fn.getData()), f"Page{self.n}")
        self.n += 1

    def remove(self):
        i = self.tab_widget.currentIndex()
        if i > 0:
            self.tab_widget.removeTab(i)
        else:
            print("Cover Page Cannot be Deleted")

    def index(self):
        print(self.tab_widget.currentIndex())

    def export(self):
        idx = self.tab_widget.count()
        print(idx)
        for i in range (0,idx):
            widget = self.tab_widget.widget(i)
            widget.getdata()
    


def main():
    a = QApplication(sys.argv)
    a.setStyle(QStyleFactory.create("Fusion"))

    wid = app()

    sys.exit(a.exec())

if __name__ == "__main__":
    main()