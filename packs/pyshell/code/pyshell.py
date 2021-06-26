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

        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

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
