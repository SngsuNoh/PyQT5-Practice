## Ex 3-2. 어플리케이션 아이콘 넣기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('ICON.jpg')) #어플리케이션 아이콘을 삽입하기 위해 QIcon객체를 생성
      self.setGeometry(300, 300, 300, 200) #창의 위치와 크기를 결정 (x,y,너비,높이) = move+resize
      self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())