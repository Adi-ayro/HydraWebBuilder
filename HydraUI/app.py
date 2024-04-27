import sys
import html
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QAction

from builder import *

class app(QMainWindow):
    def __init__(self):
        super().__init__()

        #Tab Builder
        self.tab_widget = QTabWidget()
        Cover = Builder()
        Page1 = Builder()
        self.tab_widget.addTab(Cover, "Cover")
        self.tab_widget.addTab(Page1, "Page1")

        #Toolbar
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        self.n = 2
        new = QAction("New Page", self)
        new.triggered.connect(self.add)
        toolbar.addAction(new)

        curr = QAction("Index", self)
        curr.triggered.connect(self.index)
        toolbar.addAction(curr)

        remove = QAction("Delete Page", self)
        remove.triggered.connect(self.remove)
        toolbar.addAction(remove)

        #Layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

    def add(self):
        print("clicked")
        self.tab_widget.addTab(Builder(), f"Page{self.n}")
        self.n += 1

    def remove(self):
        i = self.tab_widget.currentIndex()
        if i > 0:
            self.tab_widget.removeTab(i)
        else:
            print("Cover Page Cannot be Deleted")

    def index(self):
        print(self.tab_widget.currentIndex())

    


def main():
    a = QApplication(sys.argv)
    a.setStyle(QStyleFactory.create("Material"))

    wid = app()

    sys.exit(a.exec())

if __name__ == "__main__":
    main()