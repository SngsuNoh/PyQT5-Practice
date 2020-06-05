#04-1에서 언급된 QButtonGroup에 대해서 더 알아보도록 하자
#하나가 선택될 시 다른 버튼들이 선택 해제되는 radio 버튼들을 그룹화한다.
import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton,
                             QPushButton, QVBoxLayout,
                             QApplication, QWidget,
                             QButtonGroup)


class basicRadiobuttonExample(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Which city do you live in?')
        self.rbtn1 = QRadioButton('New York')
        self.rbtn2 = QRadioButton('Houston')
        self.label2 = QLabel("")
        #radio 버튼이 선택될 시 내용을 표시할 라벨이다.

        self.label3 = QLabel('Which state do you live in?')
        self.rbtn3 = QRadioButton('New York')
        self.rbtn4 = QRadioButton('Texas')
        self.label4 = QLabel("")

        self.btngroup1 = QButtonGroup()
        self.btngroup2 = QButtonGroup()

        self.btngroup1.addButton(self.rbtn1)
        self.btngroup1.addButton(self.rbtn2)
        self.btngroup2.addButton(self.rbtn3)
        self.btngroup2.addButton(self.rbtn4)

        self.rbtn1.toggled.connect(self.onClickedCity)
        self.rbtn2.toggled.connect(self.onClickedCity)

        self.rbtn3.toggled.connect(self.onClickedState)
        self.rbtn4.toggled.connect(self.onClickedState)
        #각 버튼이 선택될 시 해당 함수를 호출한다. (onClickedBlabla)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
        layout.addWidget(self.label2)

        layout.addWidget(self.label3)
        layout.addWidget(self.rbtn3)
        layout.addWidget(self.rbtn4)
        layout.addWidget(self.label4)

        self.setGeometry(200, 200, 300, 300)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Radio Button Example')

        self.show()

    def onClickedCity(self):
        radioBtn = self.sender()
        if radioBtn.isChecked(): #시그널을 보낸 버튼이 선택될 시 label의 텍스트를 변경해준다.
            self.label2.setText("You live in " + radioBtn.text())

    def onClickedState(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label4.setText("You live in " + radioBtn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = basicRadiobuttonExample()
    sys.exit(app.exec_())