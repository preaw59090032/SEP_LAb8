import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.begin(self)
        self.drawRectangles(p)

        p.drawPixmap(QRect(250, 100, 320, 320), self.rabbit)
        p.end()

    def drawRectangles(self, p):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        p.setPen(col)

        p.setBrush(QColor(200, 0, 0))
        p.drawRect(10, 15, 90, 60)

        p.setBrush(QColor(255, 80, 0, 160))
        p.drawRect(130, 15, 90, 60)

        p.setBrush(QColor(25, 0, 90, 200))
        p.drawRect(250, 15, 90, 60)



def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())

