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

class FileListView(QListView):
    def format(self, it, text):
        if files.isdir(self.dir + '/' + text):
            it.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
        else:
            format = it.whatsThis().split('.')
            format = max(format)
            if it.whatsThis().endswith(format):
                logo = control.read_record(format + '.icon', '/etc/ext')
                if not logo == None:
                    it.setIcon(QIcon(res.get(logo)))
                else:
                    it.setIcon(QIcon(res.get(res.etc('roller','file-icon'))))
            else:
                it.setIcon(QIcon(res.get(res.etc('roller','file-icon'))))

    def mkdir(self, dirname):
        it = QStandardItem(dirname)
        it.setWhatsThis(self.dir + "/" + dirname)
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
        files.write('/proc/info/dsel', self.dir)
        self.listdir = (files.list(self.dir))
        self.listdir.sort()

        for text in self.listdir:
            if files.isdir(self.dir+"/"+text):
                it = QStandardItem(text)
                it.setWhatsThis(self.dir + "/" + text)
                it.setFont(self.Env.font())
                self.format(it, text)
                self.entry.appendRow(it)

        for text in self.listdir:
            if files.isfile(self.dir+"/"+text):
                it = QStandardItem(text)
                it.setWhatsThis(self.dir + "/" + text)
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
                    if files.isdir(self.dir+"/"+text):
                        it = QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

                for text in self.listdir:
                    if files.isfile(self.dir+"/"+text):
                        it = QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
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
                    if files.isdir(self.dir+"/"+text):
                        it = QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

                for text in self.listdir:
                    if files.isfile(self.dir+"/"+text):
                        it = QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
                        it.setFont(self.Env.font())
                        self.format(it, text)
                        self.entry.appendRow(it)

            elif files.isfile(self.item.whatsThis()):
                files.write('/proc/info/fsel', self.item.whatsThis())  # Send File selected


class DirListView(QListView):
    def format(self, it, text):
        if files.isdir(self.dir + '/' + text):
            it.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))

    def mkdir(self, dirname):
        it = QStandardItem(dirname)
        it.setWhatsThis(self.dir + "/" + dirname)
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
        files.write('/proc/info/dsel', self.dir)
        self.listdir = (files.list(self.dir))
        self.listdir.sort()

        for text in self.listdir:
            if files.isdir(self.dir + "/" + text):
                it = QStandardItem(text)
                it.setWhatsThis(self.dir + "/" + text)
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
                    if files.isdir(self.dir + "/" + text):
                        it = QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
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
                    if files.isdir(self.dir + "/" + text):
                        it = QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
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
        self.btnCancel.setText(res.get('@string/cancel'))
        self.btnCancel.setFont(self.Env.font())
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnCancel.setGeometry(0, int(self.Env.height() / 2) - 50, int(self.Env.width() / 4), 50)
        else:
            self.btnCancel.setGeometry(0,int(self.Env.height()/1.5)-50,int(self.Env.width()/3),50)
        self.btnCancel.clicked.connect(self.Widget.Close)
        self.layout().addWidget(self.btnCancel)

        self.btnSelect = QPushButton()
        self.btnSelect.setFont(self.Env.font())
        self.btnSelect.clicked.connect(self.inp)
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnSelect.setGeometry(int(self.Env.width() / 4), int(self.Env.height() / 2) - 50,
                                   int(self.Env.width() / 4), 50)
        else:
            self.btnSelect.setGeometry(int(self.Env.width()/3),int(self.Env.height()/1.5)-50,int(self.Env.width()/3),50)

        self.layout().addWidget(self.btnSelect)

        self.leSave = QLineEdit()
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
        if self.mode=='select':
            inputx = files.readall('/proc/info/dsel')
            self.External[2](inputx)
        elif self.mode=='save' or self.mode=='save-as':
            self.leSave.setPlaceholderText(res.get('@string/fn'))
            inputx = files.readall('/proc/info/dsel')+'/'+self.leSave.text()
            self.External[2](inputx)
        else:
            inputx = files.readall('/proc/info/fsel')
            self.External[2](inputx)

        self.Widget.Close()