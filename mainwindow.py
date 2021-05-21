# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')
        self.ui.show()

        #Operators
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_power.clicked.connect(self.power)
        self.ui.btn_point.clicked.connect(self.point)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_percent.clicked.connect(self.percent)
        self.ui.btn.clicked.connect(self.btn)
        self.ui.btn_equal.clicked.connect(self.equal)

        #numbers
        self.ui.number1.clicked.connect(self.number_1)
        self.ui.number2.clicked.connect(self.number_2)
        self.ui.number3.clicked.connect(self.number_3)
        self.ui.number4.clicked.connect(self.number_4)
        self.ui.number5.clicked.connect(self.number_5)
        self.ui.number6.clicked.connect(self.number_6)
        self.ui.number7.clicked.connect(self.number_7)
        self.ui.number8.clicked.connect(self.number_8)
        self.ui.number9.clicked.connect(self.number_9)
        self.ui.number0.clicked.connect(self.number_0)

    def equal(self):
        self.number_2 = float(self.ui.lineEdit_1.text())
        if self.op=="-":
            self.ui.lineEdit_1.setText(str(self.number_1 - self.number_2))
        elif self.op=="+":
            self.ui.lineEdit_1.setText(str(self.number_1 + self.number_2))
        elif self.op == "*":
            self.ui.lineEdit_1.setText(str(self.number_1 * self.number_2))
        elif self.op == "/":
            self.ui.lineEdit_1.setText(str(self.number_1 / self.number_2))
        elif self.op == "^":
            self.ui.lineEdit_1.setText(str(self.number_1 ** self.number_2))

    def sub(self):
        self.op = '-'
        self.number_1=float(self.ui.lineEdit_1.text())
        self.ui.lineEdit_1.clear()

    def sum(self):
        self.op = '+'
        self.number_1=float(self.ui.lineEdit_1.text())
        self.ui.lineEdit_1.clear()
    def mul(self):
        self.op = '*'
        self.number_1 = float(self.ui.lineEdit_1.text())
        self.ui.lineEdit_1.clear()

    def div(self):
        self.op = '/'
        self.number_1 =float(self.ui.lineEdit_1.text())
        self.ui.lineEdit_1.clear()

    def power(self):
        self.op = '^'
        self.number_1 =float(self.ui.lineEdit_1.text())
        self.ui.lineEdit_1.clear()

    def point(self):
        self.op = '.'
        self.number_1 = self.ui.lineEdit_1.text()
        if self.number_1.count(".")==0:
            self.ui.lineEdit_1.setText(str(self.number_1+'.'))
        self.ui.lineEdit_1.clear()

    def clear(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text()[:len(self.ui.lineEdit_1.text())-1])

    def percent(self):
        self.number_1 = int(self.ui.lineEdit_1.text())
        self.ui.lineEdit_1.setText(str(self.number_1 /100))
    def btn(self):
        self.number_1 = int(self.ui.lineEdit_1.text())
        self.number_1 *=-1
        self.ui.lineEdit_1.setText(str(self.number_1))
        self.number_1=int(self.number_1)

    def number_1(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text()+'1')
    def number_2(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text()+'2')

    def number_3(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text() + '3')

    def number_4(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text() + '4')

    def number_5(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text() + '5')

    def number_6(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text() + '6')

    def number_7(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text() + '7')

    def number_8(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text() + '8')

    def number_9(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text() + '9')

    def number_0(self):
        self.ui.lineEdit_1.setText(self.ui.lineEdit_1.text() + '0')



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())
