## Ex 3-10. 스타일 꾸미기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QDateTime
#setStyleSheet()을 이용하면 어플리케이션 구성 요소들의 스타일을 꾸밀 수 있다.
#대충 보니 웹프로그래밍의 css 느낌이 난다.

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):

        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')
        testLabel = QLabel(self.date.toString('yyyy년 M월 d일 ddd요일'))
        #QLabel 클래스를 통해 3개의 라벨을 만들고 텍스트를 설정해준다.
        #09에서 배운 날짜 표기를 연습하기 위해 날짜를 표시하는 testLabel도 만들어봤다.
        #QLabel은 곧 만들어질 widget 폴더에서 자세히 다루어보도록 하자


        lbl_red.setStyleSheet("color: red;" #글자색 
                             "border-style: solid;" #경계선 (solid: 실선)
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px") #경계선 모서리
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4") #배경색
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;" #대쉬 스타일 경계선 
                              "border-width: 3px;"
                              "border-color: #1E90FF")
        testLabel.setStyleSheet("color: white;"
                                "background-color: #cee5d5") #cee5d5는 민트색이다.

        vbox = QVBoxLayout()
        #수직박스레이아웃(QVBoxLayout())을 이용해 라벨들을 수직으로 배치해보자
        #한편 수평으로 라벨들을 배치하려면 QHBoxLayout()을 사용하면 된다.
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)
        vbox.addWidget(testLabel)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.resize(self.sizeHint())
        #창 크기만 설정하고 위치 설정은 안했는데 화면 중앙으로 가는 걸 보니 default인 것 같다. 지식이 늘었다!
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())