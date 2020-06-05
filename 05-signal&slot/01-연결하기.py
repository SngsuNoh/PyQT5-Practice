## Ex 7-1. 연결하기.
#PyQt는 이벤트 처리를 위해 시그널과 슬롯이라는 개념을 사용한다.
#아래는 변하는 다이얼의 값에 맞추어 LCD에 숫자를 표시하는 코드

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self) #QLCDNumber() 위젯은 LCD 화면과 같이 숫자를 표시한다.
        dial = QDial(self) #다이얼을 하나 만들어 주자. (QDial: widget-08-2번 예제 참고)

        vbox = QVBoxLayout() #수직 박스 레이아웃으로 lcd와 다이얼을 정렬하고 위젯의 레이아웃으로 설정한다.
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        #valueChanged() 시그널을 lcd.display 메소드에 연결한다. display 슬롯은 숫자를 받아서 lcd에 표시해 준다.
        #sender: dial, receiver: lcd
        #슬롯(slot)은 시그널에 어떻게 반응할 지 구현되어 있는 메소드를 의미한다.

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())