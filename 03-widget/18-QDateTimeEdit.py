## Ex 5-18. QDateTimeEdit.
#이름에서 알 수 있듯이 사용자가 날짜와 시간을 선택하고 편집하도록 할 때 사용한다.
#16~18번 파일을 살펴보면 왜 01-basic 폴더에서 날짜를 표시하는 방법을 배웠는지 짐작해 볼 수 있다.
#https://doc.qt.io/qt-5/qdatetimeedit.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateTimeEdit, QVBoxLayout
from PyQt5.QtCore import QDateTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QTimeEdit')

        datetimeedit = QDateTimeEdit(self)
        datetimeedit.setDateTime(QDateTime.currentDateTime())
        #QDateTimeEdit 위젯을 만들고 초기 시간을 현재 시간으로 설정해준다.
        datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        #선택 가능한 시간의 범위를 설정한다.
        datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')
        #setDisplayFormat을 이용해 날짜와 시간이 해당 포맷되로 출력되도록 만들어 준다.

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(datetimeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())