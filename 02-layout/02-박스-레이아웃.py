## Ex 4-2. 박스 레이아웃.
#박스 레이아웃을 이용하면 보다 유연하고 실용적인 레이아웃을 만들 수 있다고 한다.
#01에서 언급한 relative positioning과 관련이 있나 보다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
#QHBoxLayout, QVBoxLayout은 여러 위젯을 수평, 수직으로 정렬하는 레이아웃 클래스이다.
#두 클래스는 각각 박스를 하나 만드는데 안에는 또다른 박스나 위젯을 넣을 수 있다.
#참고로 01-basic-10 파일에서 맛보기로 다루어본 바 있다.


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        #버튼 두 개를 생성한다.

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        #수평 박스를 하나 만들고 두 개의 버튼과 함께 양쪽의 빈 공간을 추가해준다.
        #addStretch() 메소드를 통해 stretch factor를 조절해 주도록 하자
        #addStretch()는 신축성 있는 빈 공간을 제공하며 양쪽의 stretch factor가 같으므로 창 크기가 변화해도 크기가 같다.

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        #수직 박스를 하나 만들고 아까 만든 수평 박스를 넣어주었다.
        #위와 아래 strecth factor의 비율은 항상 3:1을 유지한다.

        self.setLayout(vbox)

        self.setWindowTitle('Box 02-layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())