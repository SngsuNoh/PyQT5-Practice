## Ex 7-4. 이벤트 핸들러 재구성하기2.
#아래는 mouseMoveEvent 슬롯을 재구성하여 마우스의 위치를 트래킹하는 코드.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 0
        y = 0

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)
        #x와 y의 값을 self.text로 저장하고 라벨에 담아 표시한다.

        self.setMouseTracking(True)
        #setMouseTracking()을 True로 설정하면 마우스의 위치를 트래킹한다.
        #default값은 False여서 마우스 버튼이 클릭되거나 떼어질 때에만 mouseEvent가 발생한다.

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mouseMoveEvent(self, e): #이벤트 핸들러의 인자 e는 이벤트 정보가 들어 있는 객체이다. 이벤트 유형마다 다르다.
        x = e.x()
        y = e.y() #이벤트 발생 시의 마우스 커서 위치를 반환한다.

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text) #마우스의 현재 위치를 label에 표시한다.
        self.label.adjustSize() #라벨의 크기가 자동으로 조절되게 한다. 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())