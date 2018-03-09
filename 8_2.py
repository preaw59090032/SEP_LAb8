import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MouseTracker(QWidget):
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('Mouse Tracker')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()

    def mouseMoveEvent(self, event):
        distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)

        q = QPainter()  #Painting the line
        q.begin(self)
        q.drawLine(event.x(), event.y(), 250, 500)
        q.end()

    def drawPoints(self, q, x, y):
        q.setPen(Qt.red)
        q.drawPoint(x, y)


def main():
    app = QApplication(sys.argv)
    ex = MouseTracker()
    sys.exit(app.exec_())

if __name__ == "__main__":
    sys.exit(main())
