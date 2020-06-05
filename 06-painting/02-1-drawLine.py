## Ex 8-2. 직선 그리기 (drawLine).
#drawLine() 을 이용하면 위젯에 다양한 스타일의 직선을 그릴 수 있다.
#아래는 서로 다른 두께와 색깔의 직선 세 개를 그려 본 코드.

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
        self.setWindowTitle('drawLine')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()

    def draw_line(self, qp):
        qp.setPen(QPen(Qt.blue, 8)) #펜의 색과 두께를 설정한다.
        qp.drawLine(30, 230, 200, 50) #시작점과 끝점을 설정하면 직선이 그려진다.
        qp.setPen(QPen(Qt.green, 12))
        qp.drawLine(140, 60, 320, 280)
        qp.setPen(QPen(Qt.red, 16))
        qp.drawLine(330, 250, 40, 190)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())