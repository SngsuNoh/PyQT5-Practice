## Ex 5-16. QDateEdit.
#QDateEdit은 사용자가 날짜를 선택하고 편집하도록 할 때 사용한다.
#https://doc.qt.io/qt-5/qdateedit.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit, QVBoxLayout
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QDateEdit')

        dateedit = QDateEdit(self)
        #QDateEdit 위젯을 하나 생성하자.
        dateedit.setDate(QDate.currentDate())
        #QDate.currentDate()를 이용해 프로그램 실행 시 현재 날짜가 표시되도록 한다.
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))
        #dateedit.setDateRange(QDate(가장 이전의 날짜), QDate(가장 나중의 날짜))로 설정할 수도 있다.
        #참고로 dafault는 1752.9.14~9999.12.31 이라고 한다. 1752년 9월 14일은 그레고리력이 처음 도입된 날이다.

        vbox = QVBoxLayout() #역시 수직 박스 레이아웃을 이용한다.
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())