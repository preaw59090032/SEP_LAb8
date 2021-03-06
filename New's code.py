#New

import sys
from PyQt5.QtCore import*
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

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(113, 3, 255))
        p.drawPolygon(
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
            )

        p.setPen(QColor(250,124,255))
        p.setBrush(QColor(250, 124, 255))
        p.drawPie(50, 150, 100, 100, 0, 180*16)

        p.drawPolygon(QPoint( 50, 200), QPoint(150, 200), QPoint(100, 400),)

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
