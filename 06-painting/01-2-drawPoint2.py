## Ex 8-1-2. 점 그리기2 (drawPoint).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
import numpy as np


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawPoint')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        pen = QPen()
        colors = ['#D83C5F', '#3CD88F', '#AA5CE3',
                  '#DF4A26', '#AE85F6', '#F7A82E',
                  '#406CF3', '#E9F229', '#CEE5D5']
        for i in range(1000):
            pen.setWidth(np.random.randint(1, 15)) #선의 너비를 임의로 결정한다.
            pen.setColor(QColor(np.random.choice(colors))) #펜의 색을 임의로 결정한다.
            qp.setPen(pen)
            rand_x = 100 * np.random.randn()
            rand_y = 100 * np.random.randn()
            qp.drawPoint(self.width() / 2 + rand_x, self.height() / 2 + rand_y)
            #대충 점의 위치와 색을 임의로 결정하여 1000개의 점을 찍는 코드이다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())