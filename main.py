import sys

from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import random
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Отображение картинки')

        self.do_paint = False

        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()


    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw(qp)
            # Завершаем рисование
            qp.end()

    def draw(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 252, 25))
        x, y = random.randint(0, 300), random.randint(0, 200)
        r = random.randint(10, 100)
        qp.drawEllipse(x, y, x + r, x + r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())