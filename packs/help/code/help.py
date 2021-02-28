#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

from PyQt5.QtCore import  *
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import  *

class MainApp (QMainWindow):
    def RunIt (self):
        self.Env.RunApp('wapp', ['http://pyabr.rf.gd/category/tutorials/'])

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]
        self.hide()
        self.close()
        self.Widget.Close()
        QTimer.singleShot(10,self.RunIt)