#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

import sys
import math
from libabr import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

res = Res();app = App();control = Control()

def getdata (value): return control.read_record(value,'/etc/gui')

class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        f = QFont()
        f.setPointSize(int(res.etc('calculator','fontsize')))
        self.setFont(f)
        self.setText(text)
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 32)
        size.setWidth(max(size.width(), size.height()))
        return size


class MainApp(QWidget):
    NumDigitButtons = 10

    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)
    def __init__(self,args):
        super(MainApp, self).__init__()

        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        self.onCloseProcess()

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''

        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True

        self.display = QLineEdit(res.num('0'))
        self.display.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%;')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        f = QFont()
        f.setFamily(self.Env.font().family())
        f.setPointSize(20)
        self.display.setFont(f)

        self.digitButtons = []

        for i in range(MainApp.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                                                       self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.pointButton.setFont(self.Env.font())
        self.changeSignButton = self.createButton(u"\N{PLUS-MINUS SIGN}",
                                                  self.changeSignClicked)
        self.changeSignButton.setFont(self.Env.font())

        self.backspaceButton = self.createButton(res.get('@string/backspace'),
                                                 self.backspaceClicked)
        self.backspaceButton.setFont(self.Env.font())
        self.clearButton = self.createButton(res.get('@string/clear'), self.clear)
        self.clearButton.setFont(self.Env.font())
        self.clearAllButton = self.createButton(res.get('@string/clearall'), self.clearAll)
        self.clearAllButton.setFont(self.Env.font())

        self.clearMemoryButton = self.createButton("MC", self.clearMemory)
        self.clearMemoryButton.setFont(self.Env.font())
        self.readMemoryButton = self.createButton("MR", self.readMemory)
        self.readMemoryButton.setFont(self.Env.font())
        self.setMemoryButton = self.createButton("MS", self.setMemory)
        self.setMemoryButton.setFont(self.Env.font())
        self.addToMemoryButton = self.createButton("M+", self.addToMemory)
        self.addToMemoryButton.setFont(self.Env.font())

        self.divisionButton = self.createButton(u"\N{DIVISION SIGN}",
                                                self.multiplicativeOperatorClicked)
        self.divisionButton.setFont(self.Env.font())
        self.timesButton = self.createButton(u"\N{MULTIPLICATION SIGN}",
                                             self.multiplicativeOperatorClicked)
        self.timesButton.setFont(self.Env.font())
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.minusButton.setFont(self.Env.font())
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)
        self.plusButton.setFont(self.Env.font())

        self.squareRootButton = self.createButton("Sqrt",
                                                  self.unaryOperatorClicked)
        self.squareRootButton.setFont(self.Env.font())
        self.powerButton = self.createButton(u"x\N{SUPERSCRIPT TWO}",
                                             self.unaryOperatorClicked)
        self.powerButton.setFont(self.Env.font())
        self.reciprocalButton = self.createButton("1/x",
                                                  self.unaryOperatorClicked)
        self.reciprocalButton.setFont(self.Env.font())
        self.equalButton = self.createButton("=", self.equalClicked)
        self.equalButton.setFont(self.Env.font())

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 6)
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

        mainLayout.addWidget(self.clearMemoryButton, 2, 0)
        mainLayout.addWidget(self.readMemoryButton, 3, 0)
        mainLayout.addWidget(self.setMemoryButton, 4, 0)
        mainLayout.addWidget(self.addToMemoryButton, 5, 0)

        for i in range(1, MainApp.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.timesButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)

        mainLayout.addWidget(self.squareRootButton, 2, 5)
        mainLayout.addWidget(self.powerButton, 3, 5)
        mainLayout.addWidget(self.reciprocalButton, 4, 5)
        mainLayout.addWidget(self.equalButton, 5, 5)
        self.setLayout(mainLayout)

        self.Widget.SetWindowTitle(res.get("@string/app_name"))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('calculator',"logo"))))

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == res.num('0') and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(res.num(digitValue)))

    def unaryOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if clickedOperator == "Sqrt":
            if operand < 0.0:
                self.abortOperation()
                return

            result = math.sqrt(operand)
        elif clickedOperator == u"x\N{SUPERSCRIPT TWO}":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return

            result = 1.0 / operand

        self.display.setText(str(res.num(result)))
        self.waitingForOperand = True

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(res.num(str(self.factorSoFar)))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(res.num(str(self.sumSoFar)))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(res.num(str(self.factorSoFar)))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(res.num(str(self.sumSoFar)))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText(res.num('0'))

        if "." not in self.display.text():
            self.display.setText(res.num(self.display.text() + "."))

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(res.num(text))

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = res.num('0')
            self.waitingForOperand = True

        self.display.setText(text)

    def clear(self):
        if self.waitingForOperand:
            return

        self.display.setText(res.num('0'))
        self.waitingForOperand = True

    def clearAll(self):
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.display.setText(res.num('0'))
        self.waitingForOperand = True

    def clearMemory(self):
        self.sumInMemory = 0.0

    def readMemory(self):
        self.display.setText(res.num(str(self.sumInMemory)))
        self.waitingForOperand = True

    def setMemory(self):
        self.equalClicked()
        self.sumInMemory = float(self.display.text())

    def addToMemory(self):
        self.equalClicked()
        self.sumInMemory += float(self.display.text())

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def abortOperation(self):
        self.clearAll()
        self.display.setText("####")

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == u"\N{MULTIPLICATION SIGN}":
            self.factorSoFar *= rightOperand
        elif pendingOperator == u"\N{DIVISION SIGN}":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True