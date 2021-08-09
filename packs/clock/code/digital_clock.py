'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, Apt, Dpkg, PyPI
    * License:          GNU General Publice License v3.0

    * Source code:      https://github.com/PyFarsi/pyabr
    * PyPI:             https://pypi.org/project/pyabr

    - Download Pyabr OS

    * AMD64, Intel64:   https://dl.pyabr.ir/pyabr-x86_64.iso     
    * ARM64:            https://dl.pyabr.ir/pyabr-arm64.img
    * Platform:         https://dl.pyabr.ir/stor.sb
    * Wheel Package:    https://dl.pyabr.ir/pyabr.whl
    
    - Channels:

    * Official Website: https://pyabr.ir
    * Telegram Channel: https://t.me/pyfarsi
    * Gap Channel:      https://gap.im/pyabr
    * Sorosh Channel:   https://splus.ir/pyabr
    * Instagram:        https://instagram.com/pyabrir
    * Hoorsa:           https://hoorsa.com/pyabr
    * Aparat:           https://aparat.com/pyabr

'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from libabr import *
from PyQt5 import uic
import requests,shutil,os,importlib
app = App()
res = Res()
files = Files()
control = Control()
commands = Commands()
def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainApp(QMainWindow):
    def showTime_lock (self):

        try:
        # getting current time
            current_time = QTime.currentTime()

        # converting QTime object to string
            label_time = current_time.toString('hh:mm')

        # showing it to the label
            self.lbl.setText(res.num(label_time))
        except:
            pass

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]

        self.lbl = QLabel()
        self.lbl.setText('18:36')

        self.setCentralWidget(self.lbl)

        self.setFixedHeight(15)

        ## Clock ##
        # creating a timer object
        timer = QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.showTime_lock)

        # update the timer every second
        timer.start(1000)

        self.lbl.setFont(self.Env.font())
        self.lbl.setAlignment(Qt.AlignCenter)

