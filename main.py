import sys
from random import randint
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.x_ogr = (0, 400)
        self.y_ogr = (0, 400)
        self.r_ogr = (1, 100)
        self.circles = []
        self.btn.clicked.connect(self.add_circle)

    def add_circle(self):
        x = randint(*self.x_ogr)
        y = randint(*self.y_ogr)
        r = randint(*self.r_ogr)
        self.circles.append((x, y, r, r))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        color = 'yellow'
        qp.setBrush(QColor(color))
        for c in self.circles:
            qp.drawEllipse(*c)


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec())