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

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from libabr import System, Files, Script, Control, Res, App

files = Files()
control = Control()
res = Res()
app = App()

def getdata (value):
    return control.read_record(value,'/etc/gui')

class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)
    def __init__(self,args):
        super(MainApp, self).__init__()

        self.calendar = QCalendarWidget()
        self.calendar.setStyleSheet('background: none;')

        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        self.onCloseProcess()

        self.Widget.Resize(self,int(res.etc(self.AppName,"width")),int(res.etc(self.AppName,"height")))

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc(self.AppName,"logo"))))

        ## Data base ##
        try:
            sweek = files.readall("/proc/info/sweek")
        except:
            sweek = 'Sat'

        ## Calender widget ##

        self.calendar.setFont(self.Env.font())
        self.calendar.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        ## Start week ##
        if sweek=="Sat":
            self.calendar.setFirstDayOfWeek(Qt.Saturday)
        elif sweek=="Sun":
            self.calendar.setFirstDayOfWeek(Qt.Sunday)
        elif sweek=="Mon":
            self.calendar.setFirstDayOfWeek(Qt.Monday)
        elif sweek=="Tue":
            self.calendar.setFirstDayOfWeek(Qt.Tuesday)
        elif sweek=="Wed":
            self.calendar.setFirstDayOfWeek(Qt.Wednesday)
        elif sweek=="Thu":
            self.calendar.setFirstDayOfWeek(Qt.Thursday)
        elif sweek=="Fri":
            self.calendar.setFirstDayOfWeek(Qt.Friday)

        self.calendar.setGridVisible(True) # https://www.tutorialspoint.com/pyqt/pyqt_qcalender_widget.htm

        self.setCentralWidget(self.calendar)
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')