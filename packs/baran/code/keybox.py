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
from libabr import Files, Colors, Control, Res, Commands, App, Permissions
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
permissions = Permissions()

def getdata (name):
    return control.read_record (name,'/etc/gui')

class KeyListView(QListView):
    def format(self, it, text):
        if files.isfile(f'/usr/share/locales/{it.whatsThis()}.locale'):
            name = control.read_record('name',f'/usr/share/locales/{it.whatsThis()}.locale')
            logo = control.read_record('logo',f'/usr/share/locales/{it.whatsThis()}.locale')
            logo_selected = control.read_record('logo-selected', f'/usr/share/locales/{it.whatsThis()}.locale')

            if getdata("layout")==it.whatsThis():
                it.setIcon(QIcon(res.get(logo_selected)))
            else:
                it.setIcon(QIcon(res.get(logo)))
            it.setText(name)
            it.setFont(self.Env.font())

    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]
        self.Dialog = ports[2]
        
        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.username = self.Env.username

        self.setStyleSheet("""
                KeyListView,QListView {
                background-color: !whitez;
                color: !blackz;
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
            '#ABCDEF', getdata("menu.scroll.color-hover")).replace('!whitez', getdata("appw.body.bgcolor")).replace(
            '!blackz', getdata("appw.body.fgcolor")))

        self.listdir = files.list('/usr/share/locales')
        self.listdir.sort()

        # check supports or non support
        for text in self.listdir:
            if files.isfile(f'/usr/share/locales/{text}'):
                it = QStandardItem(text)
                it.setWhatsThis(text.replace('.locale',''))
                it.setFont(self.Env.font())
                self.format(it, text.replace('.locale',''))
                self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            if files.isfile(f'/usr/share/locales/{self.item.whatsThis()}.locale'):
                files.write('/proc/info/ksel',self.item.whatsThis())

# select box #
class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check('key'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        ## Finds ##
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('select',"logo"))))
        self.btnCancel = QPushButton()
        self.btnCancel.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnCancel.setText(res.get('@string/cancel'))
        self.btnCancel.setFont(self.Env.font())
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnCancel.setGeometry(0, int(self.Env.height() / 4) - 50, int(self.Env.width() / 8), 50)
        else:
            self.btnCancel.setGeometry(0,int(self.Env.height()/3)-50,int(self.Env.width()/6),50)
        self.btnCancel.clicked.connect(self.Widget.Close)
        self.layout().addWidget(self.btnCancel)

        self.btnSelect = QPushButton()
        self.btnSelect.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnSelect.setFont(self.Env.font())
        self.btnSelect.clicked.connect(self.inp)
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnSelect.setGeometry(int(self.Env.width() / 8), int(self.Env.height() / 4) - 50,
                                   int(self.Env.width() / 8), 50)
        else:
            self.btnSelect.setGeometry(int(self.Env.width()/6),int(self.Env.height()/3)-50,int(self.Env.width()/6),50)

        self.layout().addWidget(self.btnSelect)

        self.leSave = QLineEdit()
        self.leSave.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.leSave.setFont(self.Env.font())
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.leSave.setGeometry(0, int(self.Env.height() / 4)-90, int(self.Env.width() / 4), 40)
        else:
            self.leSave.setGeometry(0,int(self.Env.height()/3)-90,int(self.Env.width()/3),40)

        self.layout().addWidget(self.leSave)

        # widget #
        self.Widget.SetWindowTitle(res.get('@string/choose'))
        self.btnSelect.setText(res.get('@string/select'))
        self.xwid = KeyListView([self.Env,self.Widget,self])

        self.ywid = QMainWindow()
        self.ywid.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.ywid.resize(int(self.Env.width() / 4), int(self.Env.height() / 4) - 50)
        else:
            self.ywid.resize(int(self.Env.width()/3),int(self.Env.height()/3)-50)

        self.ywid.setCentralWidget(self.xwid)
        self.layout().addWidget(self.ywid)

        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.Widget.Resize(self,int(self.Env.width()/4),int(self.Env.height()/4))
        else:
            self.Widget.Resize(self,int(self.Env.width()/3),int(self.Env.height()/3))

        self.Widget.DisableFloat()

    def inp(self):
        control.write_record('layout',files.readall('/proc/info/ksel'),'/etc/gui')
        try:
            self.External[0]()
        except:
            pass
        self.Widget.close()

    def inp_once (self):
        self.Widget.Close()