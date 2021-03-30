from PyQt5 import QtWidgets,QtCore,QtGui

from libabr import *

commands = Commands()

class MainApp:
    def Error (self):
        self.abr.Env.RunApp('text', ['Error', 'Error'])

    def __init__(self,abr):
        self.abr = abr
        abr.label = abr.findChild(QtWidgets.QLabel, 'label')
        abr.label.setText("Hello World")
        abr.setStyleSheet("background-color: black;color: white")

        QtCore.QTimer.singleShot(50,self.Error)