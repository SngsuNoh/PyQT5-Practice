## Ex 3-4. 툴팁 나타내기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont
#툴팁이란 어떤 위젯의 기능을 설명하는 등의 역할을 하는 말풍선 형태의 도움말이다
#위젯에 있는 구성 요소에 대해 툴팁이 나타나도록 할 수 있다. setToolTip() 메소드를 통해 툴팁을 만들 수 있음

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        #툴팁에 사용할 폰트를 설정한다. 여기서는 10px의 SansSerif를 사용함
        #setToolTip() 메소드를 사용해 툴팁에 표시될 텍스트를 설정한다.

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # push 버튼을 하나 생성하고 툴팁을 달아준다.
        btn.move(50, 50)
        btn.resize(btn.sizeHint()) #sizeHint() 메소드는 버튼이 적절한 크기로 설정되도록 도와준다.

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())