## Ex 5-11. QTabWidget.
#탭을 이용하면 프로그램 안의 구성요소들을 적은 면적으로 카테고리에 따라 분류할 수 있다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QGroupBox, QGridLayout, QRadioButton, QCheckBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tab1 = QWidget()
        tab2 = QWidget()

        grid1 = QGridLayout()
        grid1.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid2 = QGridLayout()
        grid2.addWidget(self.createNonExclusiveGroup(), 0, 0)

        tab1.setLayout(grid1)
        tab2.setLayout(grid2)
        #각각의 탭이 비어있으면 재미없으므로 10번 파일과 같이 그룹박스를 생성해 탭에 담아주자.

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')
        #QTabWidget() 을 통해 탭 위젯을 만들고 위에서 만든 위젯들을 탭에 추가해주자.

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        #수직 박스 레이아웃을 만들어 탭 위젯을 넣어주자.

        self.setLayout(vbox)
        #위에서 생성한 vbox를 self의 레이아웃으로 설정한다.

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())