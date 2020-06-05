## Ex 6-4. QFileDialog.
#QFileDialog를 통해 사용자는 파일이나 경로를 선택할 수 있다. 선택한 파일을 열어서 수정하거나 저장할 수 있다.
#http://doc.qt.io/qt-5/qfiledialog.html

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        #QFileDialog를 띄우고 getOpenFileName()을 통해 파일을 선택한다.
        #세 번째 매개변수를 통해 파일의 기본 경로를 선택할 수 있으며 기본적으로 모든 파일(*)을 열도록 설정되어 있다.

        if fname[0]: #선택한 파일을 열어서 텍스트 편집 위젯에 불러온다.
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())