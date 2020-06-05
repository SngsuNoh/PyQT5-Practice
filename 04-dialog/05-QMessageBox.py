## Ex 6-5. QMessageBox.
#QMessageBox는 사용자에게 정보를 제공하거나 질문/대답을 할 수 있는 다이얼로그를 제공한다.
#흔히 어떤 동작에 대한 확인이 필요할 때에 사용한다.
#상황을 설명하고, 정보를 전달하거나 사용자의 의사를 묻는 텍스트를 표시할 수 있다.
#http://doc.qt.io/qt-5/qmessagebox.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def closeEvent(self, event):
        #이제 창을 닫을 때 QCloseEvent가 생성되어 위젯에 전달된다.
        #위젯의 동작을 수정하기 위해 closeEvent 이벤트 핸들러를 손봐주도록 하자.
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #(부모 위젯 이름, '타이틀바에 나타날 문자열', '대화창에 나타날 문자열', 보여질 버튼의 종류, default로 선택될 버튼)
        #반환값은 reply에 저장된다.

        if reply == QMessageBox.Yes: #Yes를 눌렀을 경우 close event가 받아들여져 창이 닫힌다.
            event.accept()
        else: #Yes가 선택되지 않았을 경우 close event를 무시한다.
            event.ignore()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())