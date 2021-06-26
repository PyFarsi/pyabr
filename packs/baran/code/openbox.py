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
class AppListView(QListView):
    def format(self, it, text):
        if files.isfile(f'/usr/share/applications/{it.whatsThis()}.desk'):
            name = res.etc(it.whatsThis(), f'name[{getdata("locale")}]')
            logo = res.etc(it.whatsThis(), f'logo')

            it.setIcon(QIcon(res.get(logo)))
            it.setText(name)

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
                        AppListView,QListView {
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
        self.listdir = files.list('/usr/share/applications')
        self.listdir.sort()

        # check supports or non support
        can_supportlist = []

        splitext = files.readall('/proc/info/wsel').split('.')
        ext = max(splitext)

        for text in self.listdir:
            if files.isfile(f'/usr/share/applications/{text}'):
                application = res.etc(text.replace('.desk',''),'application')
                external = res.etc(text.replace('.desk',''),'external')
                support = control.read_record(f'{ext}.external.{text.replace(".desk","")}','/etc/ext')

                if application=='Yes' and external=='Yes' and support=='Yes':
                    it = QStandardItem(text)
                    it.setWhatsThis(text.replace('.desk',''))
                    it.setFont(self.Env.font())
                    self.format(it, text.replace('.desk',''))
                    self.entry.appendRow(it)
                    can_supportlist.append(text)

        if can_supportlist==[]:
            if ext=='pyc' or ext=='jar' or ext=='exe':
                self.Env.RunApp('bool', [res.get('@string/isexe'), res.get('@string/isexem'),self.exec_file])
            else:
                self.Env.RunApp('text',[res.get('@string/unk'),res.get('@string/unkm')])
            self.Widget.Close()

        self.itemOld = QStandardItem("text")

    def exec_file (self,yes):
        if yes:
            self.execute_act()

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            if files.isfile(f'/usr/share/applications/{self.item.whatsThis()}.desk'):
                files.write('/proc/info/asel',self.item.whatsThis())

    def execute_act (self):
        if permissions.check(files.readall('/proc/info/wsel'),'x',self.Env.username):
            execute_file = files.readall('/proc/info/wsel').replace ('.pyc','').replace ('.py','').replace ('.jar','').replace ('.exe','').replace ('.sa','')

            files.write('/tmp/exec.sa', f'''
{execute_file}
rm /tmp/exec.sa
pause
            ''')
            self.Env.RunApp('commento', [None])
            app.switch('roller')
        else:
            self.Env.RunApp('text', ['Permission denied','Cannot execute this file; Permission denied'])

# select box #
class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check('open'):
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
        self.btnOpenOnce = QPushButton()
        self.btnOpenOnce.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.btnOpenOnce.setText(res.get('@string/atonce'))
        self.btnOpenOnce.setFont(self.Env.font())
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnOpenOnce.setGeometry(0, int(self.Env.height() / 4) - 50, int(self.Env.width() / 8), 50)
        else:
            self.btnOpenOnce.setGeometry(0,int(self.Env.height()/3)-50,int(self.Env.width()/6),50)
        self.btnOpenOnce.clicked.connect(self.inp_once)
        self.layout().addWidget(self.btnOpenOnce)

        self.btnOpenAlways = QPushButton()
        self.btnOpenAlways.setFont(self.Env.font())
        self.btnOpenAlways.clicked.connect(self.inp)
        self.btnOpenAlways.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.btnOpenAlways.setGeometry(int(self.Env.width() / 8), int(self.Env.height() / 4) - 50,
                                   int(self.Env.width() / 8), 50)
        else:
            self.btnOpenAlways.setGeometry(int(self.Env.width()/6),int(self.Env.height()/3)-50,int(self.Env.width()/6),50)

        self.layout().addWidget(self.btnOpenAlways)

        self.leSave = QLineEdit()
        self.leSave.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};padding-left: 5%;padding-right: 5%')
        self.leSave.setFont(self.Env.font())
        if self.Env.width() > 1000 and self.Env.height() > 720:
            self.leSave.setGeometry(0, int(self.Env.height() / 4)-90, int(self.Env.width() / 4), 40)
        else:
            self.leSave.setGeometry(0,int(self.Env.height()/3)-90,int(self.Env.width()/3),40)

        self.layout().addWidget(self.leSave)

        # widget #
        self.Widget.SetWindowTitle(res.get('@string/choose'))
        self.btnOpenAlways.setText(res.get('@string/always'))
        self.xwid = AppListView([self.Env,self.Widget,self])

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
        self.inp_once()

        splitext = files.output(files.readall('/proc/info/wsel')).split ('.')
        ext = max (splitext)

        control.write_record(f'{ext}.always',files.readall('/proc/info/asel'),'/etc/ext')

    def inp_once (self):
        self.Widget.Close()
        if files.readall('/proc/info/asel')=='persia':
            self.Env.RunApp('persia', [None, files.readall('/proc/info/wsel')])
        else:
            self.Env.RunApp(files.readall('/proc/info/asel'), [files.readall('/proc/info/wsel')])