## Ex 3-7. 툴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
#메뉴는 어플리케이션에서 사용되는 모든 명령의 모음, 툴바는 자주 사용하는 명령들을 더 편하게 사용하도록 한다.

#간단한 툴바를 생성한다. 툴바에는 선택되었을 때에 애플리케이션을 종료하는 exitAction이 포함되었다.
class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        #메뉴바와 마찬가지로 QAction객체를 하나 생성한다.
        #상태바에 'Exit application' 을 보여주고, 클릭 시에 생성되는 시그널은 qApp.quit() 에 연결되어 있다.

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        #addToolBar()를 통해 툴바를 생성하고, exitAction 동작을 추가한다.

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())