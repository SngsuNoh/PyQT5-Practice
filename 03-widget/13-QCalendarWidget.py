## Ex 5-13. QCalendarWidget.
#QCalendar위젯을 통해 사용자가 날짜를 선택할 수 있는 달력을 표시할 수 있다.
#https://doc.qt.io/qt-5/qcalendarwidget.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        #QCalendarWidget 객체를 하나 생성한다.
        cal.setGridVisible(False)
        #setGridVisible(True/False) 로 날짜 사이의 그리드 표시 여부를 설정한다.
        cal.clicked[QDate].connect(self.showDate)
        #날짜를 클릭했을 때 showDate 메소드를 호출한다.

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        #selectedDate는 선택된 날짜의 정보를 가지고 있으며, default는 현재 날짜이다.

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)
        #수직 박스 레이아웃을 이용해 달력과 날짜 표시 라벨을 정렬한다.

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date): #위에서 호출한 showDate 메소드이다.
        self.lbl.setText(date.toString())
        #날짜를 클릭할 때마다 라벨의 텍스트가 선택된 날짜로 표시되도록 해 준다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())