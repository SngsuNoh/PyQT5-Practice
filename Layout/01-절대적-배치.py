## Ex 4-1. 절대적 배치.
#영어로는 absolute positioning
#절대배치는 창의 크기를 조절해도 위젯의 크기와 위치가 변하지 않으며 플랫폼마다 다르게 표현될수 있다.
#그래서 레이아웃 고치기가 번거롭지만 그래도 배워보도록 하자.
#이게 있으면 relative positioning도 있을 것 같은데 차후에 찾아보도록 해야겠다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        #라벨을 만들고 20,20에 위치시킨다.
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        #버튼을 만들고 80,13에 위치시킨다.
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning') #이름이 멋있다
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())