import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize, Qt

class AnimationOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(350,200))
        
        #Main
        items = ["None", "Drop-Down", "Fade Over"]
        self.mainCombo = QComboBox()
        self.mainCombo.addItems(items)
        self.mainCombo.activated.connect(self.getdata)


        main = QWidget()
        mainl = QHBoxLayout()
        mainl.addWidget(QLabel("Main"))
        mainl.addWidget(self.mainCombo)
        main.setLayout(mainl)

        #Heading
        self.headCombo = QComboBox()
        self.headCombo.addItems(items)
        self.headCombo.activated.connect(self.getdata)


        head = QWidget()
        headl = QHBoxLayout()
        headl.addWidget(QLabel("Heading"))
        headl.addWidget(self.headCombo)
        head.setLayout(headl)

        #Content
        self.contentCombo = QComboBox()
        self.contentCombo.addItems(items)
        self.contentCombo.activated.connect(self.getdata)

        content = QWidget()
        contentl = QHBoxLayout()
        contentl.addWidget(QLabel("Content"))
        contentl.addWidget(self.contentCombo)
        content.setLayout(contentl)

        #boundingbox
        box = QWidget()
        boxl = QVBoxLayout()
        boxl.addWidget(main)
        boxl.addWidget(head)
        boxl.addWidget(content)
        box.setLayout(boxl)
        
        #layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Animation Settings"))
        layout.addWidget(box)
        self.setLayout(layout)
        self.show()

    def getdata(self, _):
        mc = self.mainCombo.currentText()
        hc = self.headCombo.currentText()
        cc = self.contentCombo.currentText()
        print(f"main: {mc}, heading: {hc}, content: {cc}")

class HeaderOptions(QWidget):
    def __init__(self):
        super().__init__()
        #self.setFixedSize(QSize(350,200))
        
        #Font
        items = ["None", "Drop-Down", "Fade Over"]
        self.fontCombo = QComboBox()
        self.fontCombo.addItems(items)
        self.fontCombo.activated.connect(self.getdata)


        font = QWidget()
        fontl = QHBoxLayout()
        fontl.addWidget(QLabel("Font"))
        fontl.addWidget(self.fontCombo)
        font.setLayout(fontl)

        #Size
        self.sizebox = QSpinBox()
        self.sizebox.setValue(16)
        self.sizebox.valueChanged.connect(self.getdata)

        size = QWidget()
        sizel = QHBoxLayout()
        sizel.addWidget(QLabel("Font Size"))
        sizel.addWidget(self.sizebox)
        size.setLayout(sizel)

        #Color
        self.colorBox = QColorDialog().setOption(QColorDialog.NoButtons)

        color = QWidget()
        colorl = QHBoxLayout()
        colorl.addWidget(QLabel("Font Color"))
        colorl.addWidget(self.colorBox)
        color.setLayout(colorl)

        #boundingbox
        box = QWidget()
        boxl = QVBoxLayout()
        boxl.addWidget(font)
        boxl.addWidget(size)
        boxl.addWidget(color)
        box.setLayout(boxl)
        
        #layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Header Settings"))
        layout.addWidget(box)
        self.setLayout(layout)
        self.show()

    def getdata(self, _):
        font = self.fontCombo.currentText()
        size = self.sizebox.value()
        color = self.colorBox.selectedColor()
        print(f"font: {font}, size: {size}, color: {color}")


def main():
    app = QApplication(sys.argv)

    wid = HeaderOptions()
    #id = AnimationOptions()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
