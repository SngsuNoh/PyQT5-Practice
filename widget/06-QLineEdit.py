## Ex 5-6. QLineEdit.
#한 줄의 문자열을 입력하고 수정할 수 있는 위젯이다. echoMode를 설정하여 성질을 바꿀 수 있다.
#http://doc.qt.io/qt-5/qlineedit.html

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

#로그인 화면처럼 만들어 볼 생각이다.
#show/hide password 버튼을 추가해 보았다. password hide 모드에서는 lbl에 입력값을 보여주지 않는다.
class MyApp(QWidget):

    var = True

    def __init__(self):
        super().__init__()
        self.initUI()

    def showPW(self):
        if self.var==True:
            self.pw.setEchoMode(QLineEdit.Normal)
            self.var = False
        else:
            self.pw.setEchoMode(QLineEdit.Password)
            self.var = True

    def initUI(self):
        self.index = QLabel('Please Sign In', self)
        self.index.setAlignment(Qt.AlignCenter)

        self.lbl = QLabel(self)

        self.id = QLineEdit(self)
        self.id.setEchoMode(QLineEdit.Normal)

        self.pw = QLineEdit(self)
        #QLineEdit 위젯을 생성하였다.
        self.pw.setEchoMode(QLineEdit.Password)
        self.pw.textChanged[str].connect(self.onChanged)
        #qle의 텍스트가 바뀌면 onChanged() 메소드를 호출한다.

        btn = QPushButton('show/hide password', self)
        btn.clicked.connect(lambda: self.showPW())
        btn.clicked.connect(lambda: self.onChanged(self.pw.text()))
        #lambda를 안 붙이니까 실행이 안 됐는데 구글링해서 붙여보니까 잘 돌아간다. 뭐지?
        #이 블록의 세 번째 라인을 넣은 이유는 입력값을 수정하지 않고 노출 여부만 변경해도 lbl의 텍스트 상태가 바뀌도록 하기 위해서이다.

        layout = QVBoxLayout()
        layout.addWidget(self.index)
        layout.addWidget(self.id)
        layout.addWidget(btn)
        layout.addWidget(self.pw)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


    def onChanged(self, text): #호출되는 onChanged() 메소드를 구현한다.
        if self.var == True: self.lbl.setText('Password is secret')
        else:
            self.lbl.setText(text)
            self.lbl.adjustSize()
        #입력된 값으로 라벨의 텍스트를 수정하고, 사이즈를 조절한다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())