import sys
from random import randint
from UI import Ui_Form
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.btn.clicked.connect(self.add_circle)

    def add_circle(self):
        d = randint(10, 100)
        x = randint(0, self.width() - d)
        y = randint(0, self.height() - d)
        color = (randint(0, 255), randint(0, 255),randint(0, 255))
        self.circles.append([(x, y, d, d), color])
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        for cir, col in self.circles:
            qp.setBrush(QColor(*col))
            qp.drawEllipse(*cir)


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec())
