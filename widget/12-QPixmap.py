## Ex 5-12. QPixmap.
#Pixmap은 이미지 파일을 나타낼 때 사용하는 위젯이다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('../basic/test.png')
        #담을 이미지를 선택하고 픽스맵 위젯을 생성한다.
        pixmap=pixmap.scaledToHeight(300)
        #픽스맵 위젯의 사이즈를 조절해준다. weight를 이용해 조절할 수도 있다.

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        #라벨을 만들고 setPixmap을 통해 라벨에 표시될 이미지로 위에서 생성한 픽스맵 위젯을 선택한다.
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)
        #픽스맵 위젯의 너비와 높이를 표시할 라벨을 만들고 가운데 정렬한다.

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)
        #수평 박스 레이아웃을 통해 이미지 라벨과 사이즈 표시 라벨을 정렬해 준다.

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())