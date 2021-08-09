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

from libabr import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

res = Res()
app = App()
control = Control()
from pyqtconsole.console import PythonConsole
def getdata (name):
    return control.read_record (name,'/etc/gui')
class MainApp(PythonConsole):
    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)
    def __init__(self,args):
        super(MainApp, self).__init__()

        self.Widget = args[2]
        self.AppName = args[3]

        self.onCloseProcess()

        #self.Widget.Resize (700,500)
        self.Widget.Resize (self,int(res.etc(self.AppName,"width")),int(res.etc(self.AppName,"height")))
        self.Widget.SetWindowTitle (res.get("@string/app_name"))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc(self.AppName,'logo'))))

        self.setStyleSheet("""
        MainApp, PythonConsole {
        background-color: !z;
                        color: !y;
        }
                       QScrollBar
                       {
                       background : white;
                       }
                       QScrollBar::handle
                       {
                       background : #123456;
                       border-radius: 6% 6%;
                       }
                       QScrollBar::handle::pressed
                       {
                       background : #ABCDEF;
                       border-radius: 6% 6%;
                       }""".replace('white', getdata("menu.scroll.bgcolor")).replace('#123456',
                                                                                     getdata(
                                                                                         "menu.scroll.color")).replace(
            '6',
            getdata(
                "menu.scroll.round-size")).replace(
            '#ABCDEF', getdata("menu.scroll.color-hover")).replace('!z', getdata("appw.body.bgcolor")).replace(
            '!y', getdata("appw.body.fgcolor")))

        f = QFont()
        f.setFamily('DejaVu Sans Mono')
        self.setFont(f)
        self.eval_in_thread()
