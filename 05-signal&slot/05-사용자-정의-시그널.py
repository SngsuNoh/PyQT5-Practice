## Ex 7-5. 사용자 정의 시그널.
#이미 구현되어 있는 시그널을 사용하는 대신, 사용자가 직접 시그널을 정의해 사용할 수 있다.
#아래는 pyqtSignal을 이용해 시그널을 새로 만들어서 특정 이벤트 발생 시 이 시그널을 반환해 보는 코드.

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):

    closeApp = pyqtSignal()
    #closeApp이라는 이름의 pyqtSignal을 만들었다.


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        #Communicate 클래스의 closeApp 시그널은 MyApp 클래스의 close 슬롯에 연결된다.
        #closeApp 시그널이 발생할 시 MyApp 위젯이 종료된다.

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e): #마우스 클릭 시 closeApp 시그널이 방출되도록 한다.
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())