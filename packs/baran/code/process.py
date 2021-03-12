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

import sys, os
from libabr import Files, Colors, Control, Res, Commands, App
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

files = Files()
colors = Colors()
control = Control()
res = Res()
app = App()
commands = Commands()

class IDListView(QListView):

    def format(self, it, text):

        if res.etc(it.whatsThis(),'logo'):
            it.setIcon(QIcon(res.get(res.etc(it.whatsThis(),'logo'))))
        else:
            it.setIcon(QIcon(res.get('@icon/runner')))

        if res.etc(it.whatsThis(),f'name[{self.Env.__locale__}]'):
            it.setText(res.etc(it.whatsThis(),f'name[{self.Env.__locale__}]'))

    def __init__(self,Env):
        super().__init__()
        self.Env = Env
        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.username = self.Env.username

        self.setStyleSheet('background:white;')

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
                }""".replace('white', self.Env.__menu_scroll_bgcolor__).replace('#123456', self.Env.__menu_scroll_color__).replace('6',
                                                                                                         self.Env.__menu_scroll_round_size__).replace(
            '#ABCDEF', self.Env.__menu_scroll_color_hover__))

        self.dir = files.readall('/proc/info/pwd')
        files.write('/proc/info/isel', self.dir)
        self.listdir = (files.list('/proc/id'))
        if 'desktop' in self.listdir:
            self.listdir.remove ('desktop')
        self.listdir.sort()

        for text in self.listdir:
            it = QStandardItem(text)
            it.setWhatsThis(text)
            it.setFont(self.Env.font())
            self.format(it, text)
            self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            if app.check(self.item.whatsThis()):
                files.write('/proc/info/isel', self.item.whatsThis())  # Send Directory selected

# select box #
class MainApp (QMainWindow):

    def onCloseProcess (self):
        if not app.check('process'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def refreshx (self):
        self.x = IDListView(self.Env)
        self.setCentralWidget(self.x)

    def kill (self):
        commands.kill([files.readall('/proc/info/isel')])
        self.refreshx()

    def restart (self):
        self.Env.RunApp (files.readall('/proc/info/isel'),None)
        self.refreshx()

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.x = IDListView(self.Env)
        self.setCentralWidget(self.x)

        self.onCloseProcess()

        self.setStyleSheet('background-color: white;')
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('process','logo'))))
        self.Widget.SetWindowTitle (res.get('@string/app_name'))

        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)

        self.menubar.setFont(self.Env.font())
        self.restart_act = self.menubar.addAction(res.get('@string/restart'))
        self.kill_act = self.menubar.addAction(res.get('@string/kill'))
        self.kill_act.triggered.connect (self.kill)
        self.restart_act.triggered.connect (self.restart)
        self.refresh = self.menubar.addAction(res.get('@string/refresh'))
        self.refresh.triggered.connect (self.refreshx)