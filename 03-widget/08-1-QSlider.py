## Ex 5-8. QSlider
#QSlider는 수평 또는 수직 방향의 슬라이더를 제공한다.
#https://doc.qt.io/qt-5/qslider.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QPushButton, QLabel
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Move slider to change value', self)

        self.slider = QSlider(Qt.Horizontal, self)
        #Qslider 위젯을 하나 생성하고 수평 또는 수직 방향임을 명시한다.
        self.slider.move(30, 30)
        self.slider.setRange(-100, 100)
        self.slider.setSingleStep(10)
        #값의 범위와 조절 가능한 최소 단위를 설정한다.

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        '''self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)'''
        btn.clicked.connect(self.button_clicked)

        self.slider.valueChanged.connect(self.showValue)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self): #Default 버튼을 누를 시 슬라이더의 값을 0으로 초기화한다.
        self.slider.setValue(0)

    def showValue(self):
        self.lbl.setText('Value is ' + str(self.slider.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())