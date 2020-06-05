## Ex 8-3. 직사각형 그리기 (drawRect).
#메소드 이름에서 알 수 있듯이 drawRect를 사용하면 사각형을 그릴 수 있다. (x, y, width, height) 순으로 입력하면 된다.
#사각형을 세 개 정도 그려보도록 하자.

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawRect')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(180, 100, 160)) #setBrush를 통해 사각형 면의 색을 설정할 수 있다.
        qp.setPen(QPen(QColor(60, 60, 60), 3))
        qp.drawRect(20, 20, 100, 100)

        qp.setBrush(QColor(40, 150, 20))
        qp.setPen(QPen(Qt.blue, 2))
        qp.drawRect(180, 120, 50, 120)

        qp.setBrush(Qt.yellow)
        qp.setPen(QPen(Qt.red, 5))
        qp.drawRect(280, 30, 80, 40)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())