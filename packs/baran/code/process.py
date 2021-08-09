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
def getdata (name):
    return control.read_record (name,'/etc/gui')
class IDListView(QListView):

    def format(self, it, text):

        if res.etc(it.whatsThis(),'logo'):
            it.setIcon(QIcon(res.get(res.etc(it.whatsThis(),'logo'))))
        else:
            it.setIcon(QIcon(res.get('@icon/runner')))

        if res.etc(it.whatsThis(),f'name[{getdata("locale")}]'):
            it.setText(res.etc(it.whatsThis(),f'name[{getdata("locale")}]'))

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

        self.setStyleSheet("""
                        IDListView,QListView {
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
        try:
            commands.kill([files.readall('/proc/info/isel')])
            self.refreshx()
        except:
            pass

    def restart (self):
        try:
            self.Env.RunApp (files.readall('/proc/info/isel'),None)
            self.refreshx()
        except:
            pass

    def __init__(self, ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.x = IDListView(self.Env)
        self.setCentralWidget(self.x)

        self.onCloseProcess()

        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('process','logo'))))
        self.Widget.SetWindowTitle (res.get('@string/app_name'))

        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)

        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)

        self.menubar.setFont(self.Env.font())
        self.menubar.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.restart_act = self.menubar.addAction(res.get('@string/restart'))
        self.kill_act = self.menubar.addAction(res.get('@string/kill'))
        self.kill_act.triggered.connect (self.kill)
        self.restart_act.triggered.connect (self.restart)
        self.refresh = self.menubar.addAction(res.get('@string/refresh'))
        self.refresh.triggered.connect (self.refreshx)