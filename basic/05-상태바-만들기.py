## Ex 3-5. 상태바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
#QMainWindow 클래스를 통해 QMenuBar, QToolBar, QDockWidget, QStatusBar를 가지는 main window를 생성할 수 있다
#가운데 영역인 central widget은 어떠한 위젯도 들어올 수 있다


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        #상태바는 어플리케이션의 상태를 알려주기 위해 어플리케이션 하단에 위치한다
        #텍스트를 표시하기 위해 showMessage() 메소드를 사용
        #clearMessage()를 통해 텍스트를 사라지게 하거나, 텍스트가 표시되는 시간을 조정할 수 있음
        #상태바에 표시되는 텍스트를 가져오고 싶을 땐 currentMessage() 를 사용
        #QStatusBar은 상태바의 텍스트가 바뀔 때 마다 messageChanged() 시그널을 반환함

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())