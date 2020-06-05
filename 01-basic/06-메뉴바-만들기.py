## Ex 3-6. 메뉴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

#GUI 애플리케이션에서 메뉴바는 흔하게 사용되며 다양한 명령들의 모음이 메뉴바에 위치한다

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        #아이콘(exit.png)과 라벨(Exit) 을 가지는 하나의 action을 만들고 단축기(shortcut)을 지정한다.
        #메뉴에 포인터를 올렸을 때 상태바에 표시할 메세지(Exit application)을 지정했다.
        exitAction.triggered.connect(qApp.quit)
        #이 동작이 선택되었을 때 생성된(triggered) 시그널이 QApplication 위젯의 quit() 메소드에 연결되고 애플리케이션을 종료한다.

        self.statusBar()

        menubar = self.menuBar()
        #메뉴바를 생성한다.
        menubar.setNativeMenuBar(False)
        #이 코드를 통해 mac os에서도 menubar가 windows 환경과 동일하게 작동하도록 한다.
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        #'file' 메뉴를 만들고 exitAction이라는 동작을 추가한다.
        #F앞에 ampersand를 넣음으로서 alt+F가 이 메뉴의 단축키가 되도록 한다.

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())