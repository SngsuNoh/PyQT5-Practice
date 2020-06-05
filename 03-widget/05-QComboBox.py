## Ex 5-5. QComboBox.
#QComboBox는 작은 공간을 차지하면서 여러 옵션을 제공하고, 그 중 하나를 선택할 수 있도록 하는 위젯이다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Option1', self)


        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        #QComboBox 위젯을 생성하고 선택 가능한 4개의 옵션을 추가해 주었다.


        cb.activated[str].connect(self.onActivated)
        #옵션을 선택하면 onActivated 메소드가 호출된다.

        vBox = QVBoxLayout()
        vBox.addWidget(cb)
        vBox.addWidget(self.lbl)

        self.setLayout(vBox)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text): #위에서 호출한 onActivated 메소드를 구현한다.
        self.lbl.setText(text)
        self.lbl.adjustSize()
        #선택한 항목의 텍스트를 라벨에 표시하고, adjustSize() 메소드를 통해 라벨의 크기를 자동으로 조절한다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())