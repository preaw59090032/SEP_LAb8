#SEP Lap 8
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(250, 70, 150))
        p.setBrush(QColor(250, 70, 150))
        p.drawPie(70, 159, 80, 80, 0, 180 * 16)

        p.setPen(QColor(250, 70, 150))
        p.setBrush(QColor(250, 70, 150))
        p.drawPie(150, 159, 80, 80, 0, 180 * 16)

        p.drawPolygon(
            QPoint(70, 200), QPoint(230, 200), QPoint (150, 350),
            )
        p.drawPixmap(QRect(250, 100, 320, 320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
