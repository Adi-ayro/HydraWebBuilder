import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize
from PySide6.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Image/Video Options
        op = QPushButton("O")
        imgurl = QLineEdit()
        radioImg = QRadioButton("Image")
        radioVideo = QRadioButton("Video")

        radio = QButtonGroup()
        radio.addButton(radioImg)
        radio.addButton(radioVideo)
  
        a = QWidget()
        al = QHBoxLayout()
        al.addWidget(QLabel("Image/Video URL"))
        al.addWidget(op)
        a.setLayout(al)

        #Header Options
        header = QCheckBox("Header")
        headerdata = QLineEdit()

        #Content Options
        content = QCheckBox("Content")
        contentdata = QLineEdit()

        # Create layout
        layout = QVBoxLayout(self)
        layout.addWidget(a)
        layout.addWidget(imgurl)
        layout.addWidget(radioImg)
        layout.addWidget(radioVideo)
        layout.addWidget(header)
        layout.addWidget(headerdata)
        layout.addWidget(content)
        layout.addWidget(contentdata)

        # Set layout
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
