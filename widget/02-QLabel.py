## Ex 5-2. QLabel.
#계속 간접적으로 다루어 본 QLabel에 대해 알아보도록 하자. 텍스트 또는 이미지 라벨을 만들 때 쓰이며 사용자와의 상호작용은 없다.
#기본적으로 수평 방향으로는 왼쪽, 수직 방향으로는 가운데 정렬이지만 setAlignment() 를 통해 조절할 수 있다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('First Label', self)
        #QLabel을 하나 생성한다. ('라벨의 텍스트', 부모 위젯)
        label1.setAlignment(Qt.AlignCenter)
        #setAlignment() 메소드로 라벨의 배치를 조절한다.
        #Qt.AlignCenter를 사용하면 수평, 수직 방향 모두 가운데에 위치하게 된다.

        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignVCenter)
        #Qt.AlignVCenter와 Qt.AlignHCenter는 라벨을 각각 수직, 수평 방향에서 가운데로 정렬시켜 준다.

        font1 = label1.font()
        font1.setPointSize(20)
        #label1에 사용할 폰트를 생성하고 크기를 20px로 설정한다. default는 13px

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)
        #label2에 사용할 폰트를 생성하고 폰트 종류를 'Times New Roman'으로 설정한다.
        #setBold(True)를 사용해 텍스트를 bold 처리한다.

        label1.setFont(font1)
        label2.setFont(font2)
        #각 라벨에 폰트를 적용한다.

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        #각 라벨을 수직 방향으로 정렬해 준다.

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())