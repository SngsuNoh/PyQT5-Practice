## Ex 6-1. QInputDialog.
#다이얼로그는 대화창이라고도 부르며, GUI 프로그래밍에서 필수적인 요소이다. 사용자와 어플리케이션 간의 '대화'를 돕는다.
#QInputDialog(입력 다이얼로그) 는 사용자가 간단한 값을 입력할 때 사용되는 다이얼로그이다.
#입력값은 숫자, 문자, 선택한 항목 등이 될 수 있다.
#http://doc.qt.io/qt-5/qinputdialog.html

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QLabel)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 35)

        self.lbl = QLabel('click dialog', self)
        self.lbl.move(35, 70)
        self.lbl.resize(300,30)
        self.le.textChanged.connect(lambda: self.showName())
        #라벨을 하나 만들어서 이름을 표시하도록 했다.

        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self): #입력 대화창을 나타내는 메소드이다.
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        #(self, '대화창의 타이틀', '대화창에 표시할 텍스트')
        #입력한 텍스트와 boolean 값을 반환하는데, ok를 누르면 boolean값이 True, cancel을 누르면 False가 된다.

        if ok: #ok버튼을 누르면 조건문이 실행된다.
            self.le.setText(str(text))
            #입력한 값을 줄 편집 위젯에 표시되도록 한다.
    def showName(self):
        self.lbl.setText('your name is ' + str(self.le.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())