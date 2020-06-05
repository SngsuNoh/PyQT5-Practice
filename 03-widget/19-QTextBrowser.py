## Ex 5-19. QTextBrowser.
#QTextBrowser는 하이퍼텍스트 내비게이션을 포함하는 리치 텍스트를 제공한다.
#읽기 전용이므로 편집 가능한 리치 텍스트 편집기가 필요한 경우 QTextEdit을 사용해야 한다.
#하이퍼텍스트 내비게이션이 없는 텍스트 브라우저는 QTextEdit에서 setOnlyRead()를 통해 사용하며 짧은 리치 텍스트는 QLabel을 사용한다.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)
        #줄 편집기를 하나 생성한다. enter키를 누르면 append_text 메소드가 호출된다.

        self.tb = QTextBrowser()
        #텍스트 브라우저를 하나 만들었다.
        self.tb.setAcceptRichText(True)
        #setAcceptRichText() 를 True로 설정하여 리치 텍스트를 사용할 수 있게 한다. default가 True이므로 없어도 된다.
        self.tb.setOpenExternalLinks(True)
        #setOpenExternalLinks() 를 True로 설정하여 외부 링크로의 연결이 가능하게 한다.

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)
        #clear_btn 버튼을 누르면 clear_text 메소드가 호출된다.

        vbox = QVBoxLayout()
        vbox.addWidget(self.le)
        vbox.addWidget(self.tb)
        vbox.addWidget(self.clear_btn)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self): #줄 편집기에서 enter 버튼을 누르면 호출되는 메소드이다.
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()
        #텍스트 브라우저에 줄 편집기의 텍스트를 추가한다. 줄 편집기의 텍스트는 없애준다.

    def clear_text(self): #clear 버튼을 누르면 호출되는 메소드이다.
        self.tb.clear()
        #텍스트 브라우저의 모든 텍스트를 없애준다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())