## Ex 5-3. QCheckBox.
#QCheckBox는 on/off의 상태를 가지는 버튼이며 텍스트 라벨과 체크박스를 제공한다.
#http://doc.qt.io/qt-5/qcheckbox.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        #'Show title'이라는 텍스트를 갖는 체크박스를 생성한다.
        cb.move(20, 20)
        cb.toggle()
        #체크박스의 기본값을 on상태로 바꾸기 위해 사용한다.
        cb.stateChanged.connect(self.changeTitle)
        #체크박스는 상태가 바뀔 때 stateChanged 시그널을 반환한다. 이걸 changeTitle 메소드에 연결하도록 하자.

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state): #stateChanged 시그널이 연결될 changeTitle 메소드를 정의한다.
        if state == Qt.Checked: #체크박스의 상태 state가 매개변수로 주어진다.
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())