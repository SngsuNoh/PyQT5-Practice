## Ex 6-3. QFontDialog.
#폰트를 선택할 수 있도록 하는 다이얼로그이다.
#http://doc.qt.io/qt-5/qfontdialog.html

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout
, QPushButton, QSizePolicy, QLabel, QFontDialog)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #버튼의 크기가 sizeHint()가 나타내는 크기로 고정된다.
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)

        vbox = QVBoxLayout()
        vbox.addWidget(btn)

        self.lbl = QLabel('HAIL PyQt5 Practice', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setWindowTitle('Font Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        #폰트 다이얼로그를 띄우고 getFont()를 통해 사용한 폰트와 boolean 값을 반환받는다.

        if ok: #Ok버튼이 눌리면 선택한 폰트를 라벨의 폰트로 설정한다.
           self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())