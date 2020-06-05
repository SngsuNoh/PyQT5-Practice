## Ex 7-2. 이벤트 핸들러 만들기.
#PyQt에서 이벤트 처리를 할 때 사용되는 함수를 이벤트 핸들러(슬롯) 이라고 한다.
#아래는 버튼을 클릭했을 때 창의 크기가 바뀌도록 하는 함수

import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Small', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)
        #btn1과 btn2를 각각 resizeBig(), resizeSmall() 슬롯에 연결해 준다.

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def resizeBig(self): #resizeBlabla 메소드는 특정 버튼이 눌렸을 때에 호출되어 창의 크기를 변화시켜 준다. 
        self.resize(400, 500)

    def resizeSmall(self):
        self.resize(200, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())