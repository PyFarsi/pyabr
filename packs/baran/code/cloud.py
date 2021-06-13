from libabr import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

commands = Commands()
res = Res ()

class MainApp:
    def __init__(self,cl):
        super(MainApp, self).__init__()

        cl.setWindowTitle ("Hi")
        cl.setWindowIcon (QIcon(res.get('@icon/breeze-calculator')))

        self.btn = cl.findChild (QPushButton,'btnMe')
        self.btn.clicked.connect (self.click_)

    def click_(self):
        commands.cl(['abr://projop.ir/signin'])