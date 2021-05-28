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

import sys, subprocess,os,shutil,requests

from libabr import Files, Control, Permissions, Colors, Process, Modules, Package, Commands, Res, System,App

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
pack = Package()
commands = Commands()
res = Res()
app = App()

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def getdata (name):
    return control.read_record (name,'/etc/gui')

class DriveListView (QListView):
    def format(self, it):
        it.setFont(self.Env.font())

        value = control.read_record('value', f'/dev/{it.whatsThis()}')

        if not value==None:
            it.setText(value+f" - ({it.whatsThis()}:)")
        else:
            it.setText(f"New Cloud Drive - ({it.whatsThis()}:)")

        it.setIcon(QIcon(res.get('@icon/harddrive')))

    def __init__(self, ports):
        super().__init__()
        self.ports = ports

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(80, 80))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()

        self.setStyleSheet("""
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
            '#ABCDEF', getdata("menu.scroll.color-hover")))
        # on the given model index to get a pointer to the item

        self.listdir = files.list('/dev')
        self.listdir.sort()

        for text in self.listdir:
            it = QStandardItem(text)
            it.setWhatsThis(text)
            self.format(it)
            self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    ssid = ''

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            app.switch('cloudroller')

            try:
                commands.mount([self.item.whatsThis()])
                files.write('/proc/info/mnt',self.item.whatsThis())
                self.Env.RunApp('roller', [f'/stor/{self.item.whatsThis()}'])
            except:
                self.Env.RunApp ('text',[res.get('@string/e'),res.get('@string/em')])

            app.switch('cloudroller')

class MainApp (QMainWindow):

    def onCloseProcess (self):
        if not app.check('cloudroller'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def refresh (self):
        self.x = DriveListView([self.Backend,self.Env,self.Widget,self.AppName,self.External])
        self.setCentralWidget(self.x)

    def connectcloud_act (self):
        self.Widget.Close()
        self.Env.RunApp('connectcloud',[None])

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('cloudroller','logo'))))

        self.x = DriveListView(ports)
        self.setCentralWidget(self.x)

        self.menubar = QMenuBar()
        self.menubar.setFont(self.Env.font())
        self.setMenuBar(self.menubar)

        self.adddrive = self.menubar.addAction(res.get('@string/add'))
        self.adddrive.triggered.connect (self.connectcloud_act)
        
        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)
