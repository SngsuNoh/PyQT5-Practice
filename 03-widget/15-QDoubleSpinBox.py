## Ex 5-15. QDoubleSpinBox.
#QDoubleSpinBox는 실수를 선택하고 조절하는 더블 스핀 박스 위젯을 제공한다.
#QSpinBox의 setSingleStep()은 정수형 인자를 필요로 하므로 실수를 다룰 때에는 QDoubleSpinBox를 써야 함에 유의하자.
#https://doc.qt.io/qt-5/qdoublespinbox.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDoubleSpinBox, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100)
        #위젯의 범위를 설정하자. dafault는 0.0~99.99이다.
        self.dspinbox.setSingleStep(0.5)
        #single step을 0.5로 설정하자.
        self.dspinbox.setPrefix('$ ')
        #setPrefix()로 숫자 앞에 올 문자를 설정할 수 있다. 뒤에 오게 하려면 setSuffix()를 이용한다.
        self.dspinbox.setDecimals(1)
        #소수점 아래 표현할 자릿수를 설정하자.
        self.lbl2 = QLabel('Cost is 0.0 dollar')

        self.dspinbox.valueChanged.connect(self.value_changed)
        #dspinbox의 값이 바뀌면  value_changed 메소드를 호출한다.

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()
        #수직 박스 레이아웃을 통해 dspinbox와 라벨들을 정렬한다.

        self.setLayout(vbox)

        self.setWindowTitle('QDoubleSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText('Cost is ' + str(self.dspinbox.value())+ ' dollar')
        #dspinbox의 값이 바뀌었을 때 호출되어 lbl2에 dspinbox의 을 표시한다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())