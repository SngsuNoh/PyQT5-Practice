## Ex 5-7. QProgressBar.
#Progress Bar(진행 표시줄) 은 시간이 걸리는 작업에 사용하는 위젯이다.
#QProgressBar은 수평, 수직의 진행 표시줄을 제공하며 범위(최솟값과 최대값) 을 설정할 수 있다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        #진행 표시줄을 하나 생성한다.
        self.pbar.setGeometry(40, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.btn2 = QPushButton('Reset', self)
        self.btn2.move(120, 80)
        self.btn2.clicked.connect(self.reset)
        #누르면 진행하던 작업과 함께 진행 표시줄을 초기화한다.

        self.timer = QBasicTimer()
        #진행 표시줄을 활성화하기 위한 타이머 객체를 생성한다.
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e):
        #각각의 QObject와 그 자손들은 timeEvent() 이벤트 핸들러를 가진다.
        #타이머 이벤트에 반응하기 위해 이벤트 핸들러를 재구성한다.
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self): #타이머를 시작하고 멈추도록 하는 doAction 메소드를 구현한다.
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(30, self)
            #(종료시간, 이벤트가 수행될 객체)
            self.btn.setText('Stop')

    def reset(self): #타이머를 멈추고 진행 중이던 작업을 초기화하는 reset 메소드이다.
        self.timer.stop()
        self.step = 0
        self.pbar.setValue(self.step)
        self.btn.setText('Start')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())