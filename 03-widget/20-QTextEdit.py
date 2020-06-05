## Ex 5-20. QTextEdit.
#QTextEdit은 리치 텍스트와 플레인 텍스트 모두를 편집하고 표시할 수 있는 편집기 위젯을 제공한다.
#아래는 QTextEdit을 이용한 단어수 세기 프로그램

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        #QTextEdit 위젯을 생헝한다. setAcceptRichText()를 False로 설정하면 모두 플레인 텍스트로 인식한다.
        self.lbl2 = QLabel('The number of words is 0')

        self.te.textChanged.connect(self.text_changed)
        #텍스트 편집기의 텍스트가 편집될 때마다 text_changed 메소드가 호출된다.

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self): #텍스트 편집기의 텍스트가 편집될 때마다 호출되는 메소드이다.
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))
        #공백을 기준으로 텍스트를 분할해 리스트로 담았으니 리스트의 길이(len)과 텍스트의 단어수가 같다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())