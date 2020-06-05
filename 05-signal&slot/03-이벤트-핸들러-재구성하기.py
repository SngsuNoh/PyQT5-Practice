## Ex 7-3. 이벤트 핸들러 재구성하기.
#자주 쓰이는 이벤트 핸들러들은 이미 구현되어 있는 경우가 많다. (keyPressEvent, keyReleaseEvent, mousePressEvent 등등)
#이벤트 핸들러를 수정함으로써 사용자가 해당 동작을 수행했을 때 실행되는 기능을 재구성할 수 있다.
#아래는 keyPressEvent를 수정해서, 특정 키가 눌렸을 때 위젯이 종료되거나 크기가 조정되도록 한 코드.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e): #입력으로 키보드의 이벤트를 받는다.
        #e.key()는 어떤 키를 누르거나 뗐는지를 반환한다.
        if e.key() == Qt.Key_Escape: #esc키가 눌렸다면 위젯을 종료한다.
            self.close()
        elif e.key() == Qt.Key_F: #f키가 눌렸다면 위젯의 크기를 최대화한다.
            self.showFullScreen()
        elif e.key() == Qt.Key_N: #n키가 눌렸다면 위젯의 크기를 보통으로 만든다.
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())