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
        self.btnWifi.setIcon(QIcon(res.get('@icon/breeze-w100')))
        self.setCentralWidget(self.btnWifi)

        self.setFixedSize(15,15)