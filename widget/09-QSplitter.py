## Ex 5-9. QSplitter.
#QSplitter는 경계를 드래그해서 자식 위젯의 크기를 조절할 수 있는 스플리터 위젯을 제공한다
#라고 하는데 이전 위젯들은 들어본 적 있어도 이건 진짜 생소하다. 차차 배워보도록 하자.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(QFrame.Box)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)
        #스플리터를 통해 수평 방향으로 쪼개고 양쪽에 midleft, midright 위젯을 넣어주자.

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        #수직 방향으로 쪼개고 top, splitter1, bottom 위젯을 각각 넣어준다.

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        #완성화면을 보니 웹 프로그래밍에서의 section과 비슷한 역할을 하는 것 같다.

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())