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

