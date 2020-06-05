## Ex 5-14. QSpinBox.
#QSpinbox는 정수를 선택하고 조절할 수 있는 spinbox 위젯을 제공한다.
#https://doc.qt.io/qt-5/qspinbox.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('QSpinBox')

        self.spinbox = QSpinBox()
        #스핀박스 위젯을 하나 생성한다.
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        # self.spinbox.setRange(-10, 30)로도 범위를 설정할 수 있다. default 범위는 0~99
        self.spinbox.setSingleStep(2)
        #하나의 스탭을 2로 설정한다. default는 1
        self.lbl2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.value_changed)
        #스핀박스의 값이 바뀌면 value_changed 메소드를 호출한다.

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()
        #수직 박스 위젯을 통해 라벨들을 배치한다.

        self.setLayout(vbox)

        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self): #스핀박스의 값이 바뀌었을 때 호출되어 lbl2에 스핀박스의 값을 표시한다.
        self.lbl2.setText(str(self.spinbox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())