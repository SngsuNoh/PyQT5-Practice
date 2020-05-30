## Ex 5-4. QRadioButton.
#일반적으로 사용자에게 여러 옵션 중 하나를 선택하도록 할 때 사용한다. 하나를 선택하면 나머지는 선택 해제된다.
#http://doc.qt.io/qt-5/qradiobutton.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton
#참고로 한 위젯 안에 여러 버튼 그룹을 배치하고 싶다면 QButtonGroup()을 사용한다.
#http://doc.qt.io/qt-5/qbuttongroup.html

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton('First Button', self)
        #QRadioButton을 하나 생성한다.
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)
        #setChecked(True)는 프로그램 실행 시 버튼이 선택되도록 한다.

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())