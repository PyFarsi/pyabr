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

    def openWifi_manager (self):
        try:
            app.switch('desktop')
            self.Env.RunApp ('wifi',[None])
            app.switch('desktop')
        except:
            pass

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]

        self.btnWifi = QToolButton()
        self.btnWifi.clicked.connect(self.openWifi_manager)
        self.btnWifi.setIconSize(QSize(15,15))
        self.btnWifi.setStyleSheet(f'background:none;border:none')

        if files.isfile('/etc/wifi/main.sa'):
            self.btnWifi.setIcon(QIcon(res.get('@icon/breeze-w100')))
        else:
            self.hide()

        self.setCentralWidget(self.btnWifi)

        self.setFixedSize(15,15)