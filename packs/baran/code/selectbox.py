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

import sys, os, baran
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
class LineEdit (baran.BLineEdit):
    def __init__(self,ports):
        super(LineEdit, self).__init__()
        self.Env = ports[1]

class FileListView(QListView):
    def format(self, it, text):
        if files.isdir(f'{self.dir}/{text}'):
            it.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
        else:
            format = it.whatsThis().split('.')
            format = max(format)
            if it.whatsThis().endswith(format):
                logo = control.read_record(  f'{format}.icon', '/etc/ext')
                if not logo == None:
                    it.setIcon(QIcon(res.get(logo)))
                else:
                    it.setIcon(QIcon(res.get(res.etc('roller','file-icon'))))
            else:
                it.setIcon(QIcon(res.get(res.etc('roller','file-icon'))))

    def mkdir(self, dirname):
        it = QStandardItem(dirname)
        it.setWhatsThis( f"{self.dir}/{dirname}" )
        it.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
        self.entry.appendRow(it)
        it.setFont(self.Env.font())

        commands.mkdir([dirname])

    def __init__(self,Env):
        super().__init__()
        self.Env = Env
        self.entry = QStandardItemModel()
        self.parentdir = QStandardItem()
        self.parentdir.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
        self.entry.appendRow(self.parentdir)
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.username = self.Env.username

        self.setStyleSheet("""
                        FileListView,QListView {
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
        files.write('/proc/info/dsel', self.dir)
        self.listdir = (files.list(self.dir))
        self.listdir.sort()

        for text in self.listdir:
            if files.isdir(f"{self.dir}/{text}"):
                it = QStandardItem(text)
                it.setWhatsThis(f"{self.dir}/{text}")
                it.setFont(self.Env.font())
                self.format(it, text)
                self.entry.appendRow(it)

        for text in self.listdir:
            if files.isfile(f"{self.dir}/{text}"):
                it = QStandardItem(text)
                it.setWhatsThis(f"{self.dir}/{text}")
                it.setFont(self.Env.font())
                self.format(it, text)
                self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:

            if self.item.whatsThis() == "<parent>":
                commands.cd(['..'])
                self.dir = files.readall('/proc/info/pwd')
                files.write('/proc/info/dsel', self.dir)
                self.listdir = files.list(self.dir)
                self.listdir.sort()  # Credit: https://www.geeksforgeeks.org/sort-in-python/

                self.entry = QStandardItemModel()
                self.setModel(self.entry)
                self.setIconSize(QSize(64, 64))
                self.clicked[QModelIndex].connect(self.on_clicked)
                self.parentdir = QStandardItem()
                self.parentdir.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
                self.parentdir.setWhatsThis('<parent>')
                self.entry.appendRow(self.parentdir)

                for text in self.listdir:
                    if files.isdir(f"{self.dir}/{text}"):
                        it = QStandardItem(text)
                        it.setWhatsThis(f"{self.dir}/{text}")
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

                for text in self.listdir:
                    if files.isfile(f"{self.dir}/{text}"):
                        it = QStandardItem(text)
                        it.setWhatsThis(f"{self.dir}/{text}")
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

            elif files.isdir(self.item.whatsThis()):
                files.write('/proc/info/dsel', self.item.whatsThis())  # Send Directory selected
                commands.cd([self.item.whatsThis()])
                self.dir = files.readall("/proc/info/pwd")
                self.listdir = files.list(self.dir)
                self.listdir.sort()

                self.entry = QStandardItemModel()
                self.setModel(self.entry)
                self.setIconSize(QSize(64, 64))
                self.clicked[QModelIndex].connect(self.on_clicked)
                self.parentdir = QStandardItem()
                self.parentdir.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
                self.parentdir.setWhatsThis('<parent>')
                self.entry.appendRow(self.parentdir)

                for text in self.listdir:
                    if files.isdir(f"{self.dir}/{text}"):
                        it = QStandardItem(text)
                        it.setWhatsThis(f"{self.dir}/{text}")
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

                for text in self.listdir:
                    if files.isfile(f"{self.dir}/{text}"):
                        it = QStandardItem(text)
                        it.setWhatsThis(f"{self.dir}/{text}")
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

            elif files.isfile(self.item.whatsThis()):
                files.write('/proc/info/fsel', self.item.whatsThis())  # Send File selected


class DirListView(QListView):
    def format(self, it, text):
        if files.isdir(f"{self.dir}/{text}"):
            it.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))

    def mkdir(self, dirname):
        it = QStandardItem(dirname)
        it.setWhatsThis(f"{self.dir}/{dirname}")
        it.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
        self.entry.appendRow(it)

        commands.mkdir([dirname])

    def __init__(self,Env):
        super().__init__()
        self.Env = Env
        self.entry = QStandardItemModel()
        self.parentdir = QStandardItem()
        self.parentdir.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
        self.entry.appendRow(self.parentdir)
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.username = self.Env.username

        self.setStyleSheet("""
                        DirListView,QListView {
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
        files.write('/proc/info/dsel', self.dir)
        self.listdir = (files.list(self.dir))
        self.listdir.sort()

        for text in self.listdir:
            if files.isdir(f"{self.dir}/{text}"):
                it = QStandardItem(text)
                it.setWhatsThis(f"{self.dir}/{text}")
                it.setFont(self.Env.font())
                self.format(it, text)
                self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:

            if self.item.whatsThis() == "<parent>":
                commands.cd(['..'])
                self.dir = files.readall('/proc/info/pwd')
                files.write('/proc/info/dsel', self.dir)
                self.listdir = files.list(self.dir)
                self.listdir.sort()  # Credit: https://www.geeksforgeeks.org/sort-in-python/

                self.entry = QStandardItemModel()
                self.setModel(self.entry)
                self.setIconSize(QSize(64, 64))
                self.clicked[QModelIndex].connect(self.on_clicked)
                self.parentdir = QStandardItem()
                self.parentdir.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
                self.parentdir.setWhatsThis('<parent>')
                self.entry.appendRow(self.parentdir)

                for text in self.listdir:
                    if files.isdir(f"{self.dir}/{text}"):
                        it = QStandardItem(text)
                        it.setWhatsThis(f"{self.dir}/{text}")
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

            elif files.isdir(self.item.whatsThis()):
                files.write('/proc/info/dsel', self.item.whatsThis())  # Send Directory selected
                commands.cd([self.item.whatsThis()])
                self.dir = files.readall("/proc/info/pwd")
                self.listdir = files.list(self.dir)
                self.listdir.sort()

                self.entry = QStandardItemModel()
                self.setModel(self.entry)
                self.setIconSize(QSize(64, 64))
                self.clicked[QModelIndex].connect(self.on_clicked)
                self.parentdir = QStandardItem()
                self.parentdir.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
                self.parentdir.setWhatsThis('<parent>')
                self.entry.appendRow(self.parentdir)

                for text in self.listdir:
                    if files.isdir(f"{self.dir}/{text}"):
                        it = QStandardItem(text)
                        it.setWhatsThis(f"{self.dir}/{text}")
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

# select box #
class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check('select'):
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

        self.setStyleSheet('background-color: white;')
        ## Finds ##
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('select',"logo"))))
        self.btnCancel = QPushButton()
        self.btnCancel.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnCancel.setText(res.get('@string/cancel'))
        self.btnCancel.setFont(self.Env.font())
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnCancel.setGeometry(0, int(self.Env.height() / 2) - 50, int(self.Env.width() / 4), 50)
        else:
            self.btnCancel.setGeometry(0,int(self.Env.height()/1.5)-50,int(self.Env.width()/3),50)
        self.btnCancel.clicked.connect(self.Widget.Close)
        self.layout().addWidget(self.btnCancel)

        self.btnSelect = QPushButton()
        self.btnSelect.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnSelect.setFont(self.Env.font())
        self.btnSelect.clicked.connect(self.inp)
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnSelect.setGeometry(int(self.Env.width() / 4), int(self.Env.height() / 2) - 50,
                                   int(self.Env.width() / 4), 50)
        else:
            self.btnSelect.setGeometry(int(self.Env.width()/3),int(self.Env.height()/1.5)-50,int(self.Env.width()/3),50)

        self.layout().addWidget(self.btnSelect)

        self.leSave = LineEdit(ports)
        self.leSave.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leSave.setFont(self.Env.font())
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.leSave.setGeometry(0, int(self.Env.height() / 2)-90, int(self.Env.width() / 2), 40)
        else:
            self.leSave.setGeometry(0,int(self.Env.height()/1.5)-90,int(self.Env.width()/1.5),40)

        self.layout().addWidget(self.leSave)

        if self.External[1]==None:
            mode = control.read_record('select.mode', '/etc/configbox')
            self.mode = mode
        else:
            self.mode = self.External[1]

        # widget #
        if self.External[0]==None or self.External[0]=="":
            if self.mode == 'select':
                self.Widget.SetWindowTitle(res.get('@string/dir'))
                self.btnSelect.setText(res.get('@string/choose'))
                self.xwid = DirListView(self.Env)
            elif self.mode == 'open':
                self.Widget.SetWindowTitle(res.get('@string/file'))
                self.btnSelect.setText(res.get('@string/open'))
                self.xwid = FileListView(self.Env)
            elif self.mode == 'save':
                self.Widget.SetWindowTitle(res.get('@string/dir'))
                self.btnSelect.setText(res.get('@string/save'))
                self.xwid = FileListView(self.Env)
            elif self.mode == 'save-as':
                self.Widget.SetWindowTitle(res.get('@string/dir'))
                self.btnSelect.setText(res.get('@string/save'))
                self.xwid = FileListView(self.Env)
            else:
                self.xwid = FileListView(self.Env)
        else:
            if self.mode == 'select':
                self.Widget.SetWindowTitle(self.External[0])
                self.btnSelect.setText(res.get('@string/choose'))
                self.xwid = DirListView(self.Env)
            elif self.mode == 'open':
                self.Widget.SetWindowTitle(self.External[0])
                self.btnSelect.setText(res.get('@string/open'))
                self.xwid = FileListView(self.Env)
            elif self.mode == 'save':
                self.Widget.SetWindowTitle(self.External[0])
                self.btnSelect.setText(res.get('@string/save'))
                self.xwid = FileListView(self.Env)
            elif self.mode == 'save-as':
                self.Widget.SetWindowTitle(self.External[0])
                self.btnSelect.setText(res.get('@string/save'))
                self.xwid = FileListView(self.Env)
            else:
                self.xwid = FileListView(self.Env)

        self.ywid = QMainWindow()
        self.ywid.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        if self.External[1].startswith('save'):
            if self.Env.width() > 1000 and self.Env.height() > 720:
                self.ywid.resize(int(self.Env.width()/2),int(self.Env.height()/2)-90)
            else:
                self.ywid.resize(int(self.Env.width()/1.5),int(self.Env.height()/1.5)-90)
        else:
            if self.Env.width() > 1000 and self.Env.height() > 720:
                self.ywid.resize(int(self.Env.width() / 2), int(self.Env.height() / 2) - 50)
            else:
                self.ywid.resize(int(self.Env.width()/1.5),int(self.Env.height()/1.5)-50)

        self.ywid.setCentralWidget(self.xwid)
        self.layout().addWidget(self.ywid)

        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.Widget.Resize(self,int(self.Env.width()/2),int(self.Env.height()/2))
        else:
            self.Widget.Resize(self,int(self.Env.width()/1.5),int(self.Env.height()/1.5))

        self.Widget.DisableFloat()

    def inp(self):
        try:
            if self.mode=='select':
                inputx = files.readall('/proc/info/dsel')
                self.External[2](inputx)
            elif self.mode=='save' or self.mode=='save-as':
                self.leSave.setPlaceholderText(res.get('@string/fn'))
                inputx = f"{files.readall('/proc/info/dsel')}/{self.leSave.text()}"
                self.External[2](inputx)
            else:
                inputx = files.readall('/proc/info/fsel')
                self.External[2](inputx)
        except:
            self.External[2]('')

        self.Widget.Close()