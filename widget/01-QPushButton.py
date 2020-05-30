## Ex 5-1. QPushButton.
#Push 버튼은 애플리케이션이 어떤 동작을 수행하도록 명령할 때에 사용된다. QPushButton 클래스로 만들 수 있다.
#https://doc.qt.io/qt-5/qpushbutton.html <-함께 쓰이는 메소드와 시그널

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        #QPushButton 클래스로 push버튼을 하나 생성한다. ('표시할 텍스트', 부모 클래스 이름)
        #B 앞에 &가 붙었으므로 이 버튼의 단축키는 alt+b이다.
        btn1.setCheckable(True)
        #setCheckable(True)는 선택되거나 선택되지 않은 상태를 유지할 수 있도록 한다. 아마 default는 False
        btn1.toggle()
        #toggle() 메소드를 호출하면 버튼의 상태가 바뀐다. 따라서 이 버튼은 프로그램 실행 시부터 선택되어 있다.

        btn2 = QPushButton(self)
        btn2.setText('Button&2')
        #setText()로 버튼에 표시할 텍스트를 따로 설정할 수 있으며 이 버튼의 단축키는 alt+2이다.

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)
        #setEnabled(False)는 버튼을 사용할 수 없도록 한다. 이 메소드의 default는 아마 True

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        #layout룬 폴더에서 다룬 박스 레이아웃을 이용해 버튼들 수직으로 정렬한다.

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())