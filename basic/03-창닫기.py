## Ex 3-3. 창 닫기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication #QtCore 모듈에서 QCoreApplication 클래스를 불러옴


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('Quit', self)
      #Push버튼 하나를 생성한다. 이 버튼(btn)은 QPushButton의 instance가 된다.
      #(버튼에 표시할 텍스트, 버튼이 위치할 부모위젯)
      btn.move(50, 50)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)
      #PyQt5에서 이벤트 처리는 시그널-슬롯 매커니즘으로 이루어진다.
      #btn이 클릭되면 clicked 시그널이 만들어지고 instance()는 현재 instance를 반환한다.
      #clicked 시그널은 quit 메소드에 전달된다. 발신자: btn - 수신자: app 간 커뮤니케이션

      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())