## Ex 6-2. QColorDialog.
#색상을 선택할 수 있는 다이얼로그이다.
#http://doc.qt.io/qt-5/qcolordialog.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        #QColor를 사용해서 배경색이 될 검정색을 만들었다.

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130, 35, 100, 100)

        self.setWindowTitle('Color Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        #QColorDialog를 띄우고 getColor()를 통해 색상을 저장한다.

        if col.isValid(): #색상을 선택하고 Ok를 눌렀을 경우 col.isValid() 가 True가 된다.
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
            #선택한 색상을 frame의 배경색으로 설정한다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())