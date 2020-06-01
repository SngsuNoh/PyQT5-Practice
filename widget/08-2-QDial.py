## Ex 5-8. QSlider & QDial.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QPushButton
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(-50, 50)

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        '''self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)'''
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())