## Ex 3-9. 날짜와 시간 표시하기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QDate, Qt
#QDate, QTime, QDateTime 클래스를 사용해 현재날짜/현재시각/현재날짜와 시간을 얻을 수 있다.

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        #currentDate를 통해 현재 날짜를 얻는다.
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        #showMessage()를 통해 상태 표시줄에 현재 날짜를 표시한다.

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())