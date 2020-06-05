## Ex 3-8. 창을 화면의 가운데로.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
#창을 화면 가운데에 띄워보도록 하자.
#10번 파일에서 언급하겠으나 굳이 이 과정 없이도 위치를 설정하지 않으면 default로 화면 중앙에 창이 띄워지는 듯 하다.

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center()
        #center() 메소드를 통해 창이 화면의 가운데에 위치하게 된다.
        self.show()

    def center(self): #center() 메소드를 구현해보자
        qr = self.frameGeometry()
        #frameGeometry() 메소드를 통해 창의 위치와 크기 정보를 가져오도록 하자
        cp = QDesktopWidget().availableGeometry().center()
        #사용하는 모니터 화면의 가운데 위치를 파악한다.
        qr.moveCenter(cp)
        #창의 직사각형 위치를 화면 중심 위치로 이동한다.
        self.move(qr.topLeft())
        #현재 창을 qr(화면의 중심으로 이동한 직사각형) 의 위치로 이동시킨다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())