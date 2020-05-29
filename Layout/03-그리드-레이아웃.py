## Ex 4-3. 그리드 레이아웃.
#그리드 레이아웃은 위젯의 공간을 행과 열 (row&column)으로 구분한다. 행:가로줄 / 열:세로줄
#가장 일반적인 레이아웃 클래스라고 한다. 일찍 알았으면 좋았을텐데


import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)
from PyQt5.QtCore import QDateTime
#그리드 레이아웃은 QGridLayout() 메소드를 사용해 생성한다.

class MyApp(QWidget):
    #세 개의 라벨, 두 개의 라인 에디터, 한 개의 텍스트 에디터를 그리드 레이아웃으로 배치해 보도록 하자.

    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        #그리드 레이아웃을 생성해 어플리케이션 창의 레이아웃으로 설정해 주었다.

        dateLabel = QLabel(self.date.toString('yyyy년 M월 d일 ddd요일'))
        #맨 아래에 날짜를 표시하고 싶어졌다.

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)
        grid.addWidget(QLabel('Date'), 3, 0)
        #addWidget(추가할 위젯, 행번호, 열번호)
        #세 라벨을 첫 번째 열에 수직으로 배치하는것이다.

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)
        grid.addWidget(dateLabel, 3, 1)
        #라인 에디터와 텍스트 에디터를 추가해준다. 라인 에디터는 한 줄, 텍스트 에디터는 여러 줄을 수정한다.

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())