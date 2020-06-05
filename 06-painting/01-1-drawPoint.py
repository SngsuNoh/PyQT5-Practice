## Ex 8-1-1. 점 그리기1 (drawPoint).
#QPainter는 일반적으로 paint event를 통해 동작한다.
#아래는 drawPoint를 이용해 위젯에 다양한 방식으로 점을 찍어 보는 코드.

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp): #setPen()을 이용해 펜의 색과 두께를 조절해 가며 세 개의 점을 찍었다.
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawPoint(self.width() / 2, self.height() / 2) #위젯의 가로세로 길이를 특정 비율로 분할해 위치를 정해 주었다. 
        qp.setPen(QPen(Qt.green, 12))
        qp.drawPoint(self.width() / 4, 3 * self.height() / 4)
        qp.setPen(QPen(Qt.magenta, 16))
        qp.drawPoint(3 * self.width() / 4, self.height() / 4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())