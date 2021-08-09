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

from libabr import System, Control, Files, Colors, Script, App, Res
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

control = Control()
files = Files()
colors = Colors()
app = App()
res = Res()
def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainApp(QWidget):

    def onCloseProcess (self):
        if not app.check('about'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self, ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        self.Widget.Resize(self, 600, 500)
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('about',"logo"))))
        self.vmbox = QVBoxLayout()
        self.btnInfo = QToolButton()
        self.btnInfo.setMinimumSize(128,128)
        self.btnInfo.setIconSize(QSize(128,128))
        self.btnInfo.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};border-radius: 64% 64%;margin-left: {str(int(self.width()/2.666666))}%;')
        self.btnInfo.setIcon(QIcon(res.get(control.read_record('logo','/etc/gui'))))
        self.vmbox.addWidget(self.btnInfo)
        self.extral = QWidget()
        self.vmbox.addWidget(self.extral)
        self.hbox = QHBoxLayout()
        self.setLayout(self.vmbox)
        self.extral.setLayout(self.hbox)
        self.text1 = QTextBrowser()
        self.extral.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.text1.setAlignment(Qt.AlignRight)
        self.text1.append(f'Static hostname:')
        self.text1.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.text1.append(f'Cloud Software:')
        self.text1.append(f'Desktop Enviroment:')
        self.text1.append(f'Kernel:')
        self.text1.append(f'Build date:')
        self.text1.append(f'Operating System:')
        self.text1.append(f'Switched user:')
        self.text1.append(f'Interface:')
        self.text1.setFont(self.Env.font())


        self.text2 = QTextBrowser()
        self.text2.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.text2.append(files.readall('/proc/info/host'))
        self.text2.append(f"{files.readall('/proc/info/cs')} {files.readall('/proc/info/ver')} ({files.readall('/proc/info/cd')})")
        self.text2.append(files.readall('/proc/info/de'))
        self.text2.append(f"{files.readall('/proc/info/kname')} {files.readall('/proc/info/kver')}")
        self.text2.append(files.readall('/proc/info/bl'))
        self.text2.append(files.readall('/proc/info/os'))
        self.text2.append(files.readall('/proc/info/su'))
        self.text2.append(files.readall('/proc/info/inter'))
        self.text2.setAlignment(Qt.AlignLeft)
        self.text2.setFont(self.Env.font())

        self.hbox.addWidget(self.text1)
        self.hbox.addWidget(self.text2)

        self.Widget.DisableFloat()
