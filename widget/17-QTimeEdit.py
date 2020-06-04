## Ex 5-17. QTimeEdit.
#사용자에게 시간을 선택하고 편집하도록 할 때 사용한다.
#https://doc.qt.io/qt-5/qtimeedit.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QVBoxLayout
from PyQt5.QtCore import QTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QTimeEdit')

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(8, 00, 00), QTime(21, 30, 00))
        #16-QDateEdit과 같은 방법으로 사용한다. 범위의 default는 00:00:000~23:59:999
        timeedit.setDisplayFormat('hh:mm:ss')
        #setDisplayFormat 메소드를 이용해 시간이 hh:mm:ss 형식으로 표시되도록 한다.

        vbox = QVBoxLayout() #수직 박스 레이아웃을 이용해 정렬한다.
        vbox.addWidget(lbl)
        vbox.addWidget(timeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())