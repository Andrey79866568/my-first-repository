from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

    def InitUi(self):
        self.pushButton.clicked.connect(self.func)
        self.do_paint = False
        self.y = 275
        self.x = 250

    def paintEvent(self, event):
        if self.do_paint:
            q_painter = QPainter()
            q_painter.begin(self)
            self.draw_ell(q_painter)
            q_painter.end()

    def func(self):
        self.do_paint = True
        self.repaint()

    def draw_ell(self, qp):
        qp.setBrush(QColor(255, 66, 106))
        a = randint(1, self.width() + self.height())
        qp.drawEllipse(randint(0, self.width() // 5), randint(0, self.height() // 5), a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
