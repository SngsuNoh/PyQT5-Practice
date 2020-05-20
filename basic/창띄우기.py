## Ex 3-1. 창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget
#QtWidgets: UI 구성요소를 제공하는 위젯이 포함된 모듈

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') #타이틀바에 나타나는 창의 제목을 설정
        self.move(300, 300) #스크린에서 위젯을 해당 위치로 이동시킴 (x,y)
        self.resize(400, 200) #위젯의 크기를 설정 (너비, 높이)
        self.show() #위젯을 스크린에 표


if __name__ == '__main__':
    #__name__: 현재 모듈의 이름을 저장하는 내장 변수
    #프로그램이 직접 실행되는지, 모듈을 통해 실행되는지 판단한다. 직접 실행할 경우 __name__=__main__
   app = QApplication(sys.argv) #PyQt5 어플리케이션이므로 어플리케이션 객체를 생성
   ex = MyApp()
   sys.exit(app.exec_())