from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
check = True
import math
class window(QMainWindow):

    def __init__(self):
        super(window, self) .__init__()
        uic.loadUi("calexp.ui", self)

        n = None
        r = None
        h = None
        l = None

        self.val = ""

        self.show()
        self.pushButton.clicked.connect(self.num1)
        self.pushButton_5.clicked.connect(self.num2)
        self.pushButton_6.clicked.connect(self.num3)
        self.pushButton_4.clicked.connect(self.num4)
        self.pushButton_3.clicked.connect(self.num5)
        self.pushButton_7.clicked.connect(self.num6)
        self.pushButton_8.clicked.connect(self.num7)
        self.pushButton_9.clicked.connect(self.num8)
        self.pushButton_10.clicked.connect(self.num9)
        self.pushButton_11.clicked.connect(self.num0)
        self.pushButton_12.clicked.connect(self.deci)
        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_14.clicked.connect(self.minus)
        self.pushButton_15.clicked.connect(self.divide)
        self.pushButton_17.clicked.connect(self.openbrac)
        self.pushButton_18.clicked.connect(self.closebrac)
        self.pushButton_13.clicked.connect(self.mltply)
        self.pushButton_19.clicked.connect(self.dlt)
        self.pushButton_16.clicked.connect(self.eql)
        self.pushButton_20.clicked.connect(self.clr)
        self.pushButton_21.clicked.connect(self.sqrt)
        self.pushButton_22.clicked.connect(self.sqr)
        self.pushButton_23.clicked.connect(self.circA)
        self.pushButton_24.clicked.connect(self.Ccirc)
        self.pushButton_25.clicked.connect(self.inv)
        self.pushButton_29.clicked.connect(self.Vcone)
        self.pushButton_33.clicked.connect(self.Vcyl)
        self.pushButton_26.clicked.connect(self.cs)
        self.pushButton_27.clicked.connect(self.sn)
        self.pushButton_28.clicked.connect(self.tn)


        self.on()

    def on(self):
        global check
        if not check:
         self.lineEdit.setText("0")
        if check:
          self.lineEdit.setText("0")
        check = False

    def num1(self):
        global check
        if check:
           self.val = self.lineEdit.setText(self.lineEdit.text() + "1")
        if not check:
           self.lineEdit.setText("1")
        check = True

    def num2(self):
        global check
        if check:
          self.Val = self.lineEdit.setText(self.lineEdit.text() + "2")
        if not check:
          self.lineEdit.setText("2")
        check = True

    def num3(self):
        global check
        if check:
         self.val = self.lineEdit.setText(self.lineEdit.text() + "3")
        if not check:
            self.lineEdit.setText("3")
        check = True

    def num4(self):
        global check
        if check:
         self.val = self.lineEdit.setText(self.lineEdit.text()+ "4")
        if not check:
            self.lineEdit.setText("4")
        check = True

    def num5(self):
        global check
        if check:
         self.val = self.lineEdit.setText(self.lineEdit.text() + "5")
        if not check:
            self.lineEdit.setText("5")
        check = True

    def num6(self):
        global check
        if check:
         self.val = self.lineEdit.setText(self.lineEdit.text() + "6")
        if not check:
            self.lineEdit.setText("6")
        check = True

    def num7(self):
        global check
        
        if check:
         self.val = self.lineEdit.setText(self.lineEdit.text() + "7")
        if not check:
            self.lineEdit.setText("7")
        check = True

    def num8(self):
        global check
        if check:
         self.val = self.lineEdit.setText(self.lineEdit.text() + "8")
        if not check:
            self.lineEdit.setText("8")
        check = True

    def num9(self):
        global check
        if check:
         self.val = self.lineEdit.setText(self.lineEdit.text() + "9")
        if not check:
            self.lineEdit.setText("9")
        check =True

    def num0(self):
        global check
        if check:
          self.val = self.lineEdit.setText(self.lineEdit.text() + "0")
        if not check:
           self.lineEdit.setText("0")
        check = True

    def deci(self):
        global check
        self.val = self.lineEdit.setText(self.lineEdit.text() + ".")
        check = True

    def add(self):
        global check
        self.val = self.lineEdit.setText(self.lineEdit.text() + "+")
        check = True

    def minus(self):
        global check
        self.val = self.lineEdit.setText(self.lineEdit.text() + "-")
        check = True

    def divide(self):
        global check
        self.val = self.lineEdit.setText(self.lineEdit.text() + "/")
        check = True

    def openbrac(self):
        global check
        self.val = self.lineEdit.setText(self.lineEdit.text() + "(")
        check = True

    def closebrac(self):
        global check
        self.val = self.lineEdit.setText(self.lineEdit.text() + ")")
        check = True

    def mltply(self):
        global check
        self.val = self.lineEdit.setText(self.lineEdit.text() + "*")
        check = True

    def dlt(self):

        self.val = self.lineEdit.setText(self.lineEdit.text()[0:-1])

    def clr(self):
        global check
        if check:
          self.val = self.lineEdit.setText("0")
        if not check:
            self.lineEdit.setText("0")
        check = False

    def sqrt(self):
        global n
        global check
        n = float(self.lineEdit.text())
        if check:
            k = str((n**(1/2)))
            self.val = self.lineEdit.setText(k)
        if not check:
            k = str((n ** (1 / 2)))
            self.val = self.lineEdit.setText(k)
        check = False

    def sqr(self):
        try:
            global n
            global check
            n = float(self.lineEdit.text())
            if check:
                k = str((n**2))
                self.val = self.lineEdit.setText(k)
            if not check:
                k = str((n**2))
                self.val = self.lineEdit.setText(k)
            check = False
        except SyntaxError:
            self.lineEdit.setText("Impossible Operation")

    def inv(self):
        try:
            global n
            global check
            n = float(self.lineEdit.text())
            if check:
                k = str((1/n))
                self.val = self.lineEdit.setText(k)
            if not check:
                k = str((1/n))
                self.val = self.lineEdit.setText(k)
            check = False
        except SyntaxError:
            self.lineEdit.setText("Impossible Operation")
        except ZeroDivisionError:
            self.lineEdit.setText("Cannot be divided by Zero")

    def circA(self):
        try:
            global n
            global check
            n = float(self.lineEdit.text())
            if check:
                k = str(((n**2)*math.pi))
                self.val = self.lineEdit.setText(k)
            if not check:
                k = str(((n**2)*math.pi))
                self.val = self.lineEdit.setText(k)
            check = False
        except SyntaxError:
            self.lineEdit.setText("Impossible Operation")

    def Ccirc(self):

        try:
            global n
            global check
            n = float(self.lineEdit.text())
            if check:
                k = str((n * 2.0 * math.pi))
                self.val = self.lineEdit.setText(k)
            if not check:
                k = str((n * 2.0 * math.pi))
                self.val = self.lineEdit.setText(k)
            check = False
        except SyntaxError:
            self.lineEdit.setText("Impossible Operation")

    def Vcone(self):
        global n
        global check

        j = []

        n = float(self.lineEdit.text())
        j.append(n)
        sz = len(j)
        sm = sum(j[0:sz])
        b = float(sm**2)
        if check:
            k = str(((1 / 3) * math.pi*b))
            self.val = self.lineEdit.setText(k)

        if not check:
            k = str(((1 / 3) * math.pi*b))
            self.val = self.lineEdit.setText(k)

        check = True

    def Vcyl(self):
        global n
        global check

        n = float(self.lineEdit.text())
        if check:
            k = str((math.pi * (n**2)))
            self.val = self.lineEdit.setText(k)
        if not check:

            k = str((math.pi * (n ** 2)))
            self.val = self.lineEdit.setText(k)
        check = True

    def cs(self):
        global n
        global check
        n = float(self.lineEdit.text())
        if check:
            k = str(math.cos(n))
            self.val = self.lineEdit.setText(k)
        if not check:
            k = str(math.cos(n))
            self.val = self.lineEdit.setText(k)
        check = False

    def sn(self):
        global n
        global check
        n = float(self.lineEdit.text())
        if check:
            k = str(math.sin(n))
            self.val = self.lineEdit.setText(k)
        if not check:
            k = str(math.sin(n))
            self.val = self.lineEdit.setText(k)
        check = False

    def tn(self):
        global n
        global check
        n = float(self.lineEdit.text())
        if check:
            k = str(math.tan(n))
            self.val = self.lineEdit.setText(k)
        if not check:
            k = str(math.tan(n))
            self.val = self.lineEdit.setText(k)
        check = False


    def eql(self):
        try:
            global check
            self.val = self.lineEdit.setText(str(eval(self.lineEdit.text())))
            check = False

        except ZeroDivisionError:
            self.lineEdit.setText("cannot divide by zero")

        except SyntaxError:
            self.lineEdit.setText("Invalid operation")

        except Exception:
            self.lineEdit.setText("Error")



























































