## Ex 5-10. QGroupBox.
#그룹 박스는 상단 타이틀과 단축키(ShortCut) 을 제공하며, 안에 다양한 위젯들을 나타낼 수 있다.
#QGroupBox는 제목과 제목의 정렬을 가능하도록 해 주며 각 위젯의 사용 가능 여부를 설정할 수도 있다.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton
, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)
        #createBlaBla 메소드가 만드는 위젯들이 그리드 레이아웃을 통해 정렬된다.

        self.setLayout(grid)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    #아래는 각각의 GroupBox를 만드는 메소드들이다.
    def createFirstExclusiveGroup(self): #배타적 라디오버튼의 그룹박스를 생성한다.
        groupbox = QGroupBox('Exclusive Radio Buttons')

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3') #라디오 버튼 세 개를 만든다.
        radio1.setChecked(True) #1번 버튼이 기본적으로 체크되어 있도록 한다.

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox) #수직 박스 레이아웃으로 배치한다.

        return groupbox #해당 그룹박스를 return한다.

    def createSecondExclusiveGroup(self): #3개의 라디오 버튼과 체크박스 하나를 가지는 그룹박스이다.
        groupbox = QGroupBox('Exclusive Radio Buttons')
        groupbox.setCheckable(True) #그룹박스의 사용 여부를 선택할 수 있게 한다.
        groupbox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self): #배타적이지 않은 체크박스들의 그룹박스이다.
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True) #그룹박스를 평평하게 보이도록 한다.

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button') #3개의 상태를 가지는 체크박스이다.
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self): #Push버튼 여러 개를 갖는 그룹박스이다.
        groupbox = QGroupBox('Push Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(True) #createSecondExclusiveGroup과 다르게 실행 시부터 그룹박스가 선택되어 있도록 한다.

        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('Popup Button')
        menu = QMenu(self) #이 버튼은 여러 개의 요소 중 하나를 선택할 수 있도록 해 주는 버튼이다.
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())