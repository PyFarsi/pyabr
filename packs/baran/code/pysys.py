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
import sys

from pyabr.core import *
from pyabr.quick import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtQml import *

control = Control()
files = Files()
colors = Colors()
app = App()
res = Res()

def getdata (name):
    return control.read_record (name,'/etc/gui')

application = QGuiApplication(sys.argv)
app.switch('pysys')
application.setWindowIcon(QIcon(res.get('@icon/breeze-about')))

class MainApp (MainApp):

    def loop (self):
        if self.background_text.property('text')=='shutdown':
            self.close()
            app.signal('shutdown')
        elif self.background_text.property('text')=='lock':
            self.close()
            app.signal('lock')
        elif self.background_text.property('text')=='logout':
            self.close()
            app.signal('logout')
        elif self.background_text.property('text')=='reboot':
            self.close()
            app.signal('restart')
        elif self.background_text.property('text')=='suspend':
            self.close()
            app.signal('sleep')
        elif self.background_text.property('text')=='switchuser':
            self.close()
            app.signal('switchuser')

        self.background_text.setProperty('text','')
        QTimer.singleShot(10,self.loop)

    def __init__(self):
        super(MainApp, self).__init__()

        self.load(res.get('@layout/pysys'))
        self.setProperty('title',res.get('@string/app_name'))
        self.background_text = self.findChild('background_text')

        self.loop()

w = MainApp()
application.exec()