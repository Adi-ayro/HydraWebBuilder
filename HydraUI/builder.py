import sys
import html
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *

import content
import options
import preview

class Builder(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(1350,725))

        self.options = options.Options()
        self.preview = preview.Preview()
        self.content = content.Content()

        #Signals

        #Preview
        self.preview.reload.clicked.connect(self.reload_page)
        self.preview.save.clicked.connect(self.getdata)

        #layout
        layout = QHBoxLayout()
        layout.addWidget(self.options)
        layout.addWidget(self.preview)
        layout.addWidget(self.content)
        self.setLayout(layout)

        #self.centralWidget = QWidget()
        #self.centralWidget.setLayout(layout)
        #self.setCentralWidget(self.centralWidget)
        self.show()

    def getdata(self):
        # Fetcher for Content
        url = self.content.imgurl.text()
        hd = self.content.headerdata.toPlainText()
        cd = self.content.contentdata.toPlainText()
        h = self.content.header.isChecked()
        c = self.content.content.isChecked()
        iv = self.content.radio.checkedButton().text()
        print(f"Header: {h} Content: {c} Img/Vid: {iv}")
        print(f"Url: {url}")
        print(f"Header Data: {hd}")
        print(f"Content Data: {cd}")

        # Fetcher for Options
        cfont = self.options.content.fontCombo.currentText()
        csize = self.options.content.sizebox.value()
        ccolor = self.options.content.colorBox.selected_color.name()
        print("Content Options:")
        print(f"font: {cfont}, size:{csize}, color: {ccolor} ")

        hfont = self.options.heading.fontCombo.currentText()
        hsize = self.options.heading.sizebox.value()
        hcolor = self.options.heading.colorBox.selected_color.name()
        print("Heading Options:")
        print(f"font: {hfont}, size:{hsize}, color: {hcolor} ") 

        mc = self.options.animate.mainCombo.currentText()
        hc = self.options.animate.headCombo.currentText()
        cc = self.options.animate.contentCombo.currentText()
        print(f"Animation Options")
        print(f"main: {mc}, heading: {hc}, content: {cc}")

    # Workings for Preview    
    def set_html(self, html):
        self.preview.set_html(html)  

    def reload_page(self):
        self.preview.reload_page()


def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Material"))

    wid = Builder()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()