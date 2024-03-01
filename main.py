import sys

import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.do_paint = False
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.pushButton = QPushButton("Кнопка", self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randrange(256), random.randrange(256), random.randrange(256)))
        a = random.randint(50, 150)
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        qp.drawEllipse(y, x, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
