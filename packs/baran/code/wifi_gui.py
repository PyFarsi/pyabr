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

class WifiListView (QListView):
    def format(self, it, text):
        it.setFont(self.Env.font())

        signal = control.read_list('/etc/wifi/signal')[int(it.whatsThis())]

        if not signal=='':
            signal = int(signal)
            if signal <= 20:
                it.setIcon(QIcon(res.get(res.etc('wifi','wifi-020'))))
            elif signal <= 40:
                it.setIcon(QIcon(res.get(res.etc('wifi','wifi-040'))))
            elif signal <= 80:
                it.setIcon(QIcon(res.get(res.etc('wifi','wifi-080'))))
            else:
                it.setIcon(QIcon(res.get(res.etc('wifi','wifi-100'))))

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
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        self.setStyleSheet("""
                        WifiListView,QListView {
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
        # on the given model index to get a pointer to the item

        files.write('/etc/wifi/list',subprocess.check_output(['nmcli','-t','-f','SSID','device','wifi','list']).decode('utf-8'))
        files.write('/etc/wifi/signal',subprocess.check_output(['nmcli', '-t', '-f', 'SIGNAL', 'device', 'wifi', 'list']).decode('utf-8'))
        self.listdir = control.read_list('/etc/wifi/list')
        self.listdir.sort()
        self.listdir.remove ('')

        r = 0

        for text in self.listdir:
            it = QStandardItem(text)
            it.setWhatsThis(str(r))
            it.setText(text)
            self.format(it, text)
            self.entry.appendRow(it)
            r+=1

        self.itemOld = QStandardItem("text")

    ssid = ''

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            app.switch('wifi')
            self.ssid = self.item.text()
            self.Env.RunApp ('bool',['Connect to '+self.item.text(),'Do you want to connect to this network?',self.connect_])
            app.switch('wifi')

    def _enter_password_ (self,password):
        status = subprocess.check_output(f'nmcli device wifi connect "{self.ssid}" password "{password}"', shell=True).decode()
        files.write('/etc/wifi/status', status)

        QTimer.singleShot(500, self.check_password_)

    def enter_password_(self):
        app.switch('wifi')
        self.Env.RunApp('input', ['Enter network password',self._enter_password_])
        app.switch('wifi')

    def check_password_(self):
        status = control.read_list('/etc/wifi/status')[1]

        if status.startswith('D'):
            app.switch('wifi')
            self.Env.RunApp('text', ['Successfully connected', 'Successfully connected to this network'])
            app.switch('wifi')
        else:
            app.switch('wifi')
            self.Env.RunApp('text', ['Incorrect password', 'Your entered password is incorrect'])
            app.switch('wifi')

    def check_connection_(self):
        status = control.read_list('/etc/wifi/status')[1]

        if status.startswith ('D'):
            app.switch('wifi')
            self.Env.RunApp('text',['Successfully connected','Successfully connected to this network'])
            app.switch('wifi')
        else:
            control.write_record('input.password_hint','Yes','/etc/configbox')
            QTimer.singleShot(100,self.enter_password_)

    def connect_(self,yes):
        if yes:
            status = subprocess.check_output(f'nmcli device wifi connect "{self.ssid}"',shell=True).decode()
            files.write('/etc/wifi/status',status)

            QTimer.singleShot(500,self.check_connection_)

class MainApp (QMainWindow):

    def onCloseProcess (self):
        if not app.check('wifi'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def refresh (self):
        self.x = WifiListView([self.Backend,self.Env,self.Widget,self.AppName,self.External])
        self.setCentralWidget(self.x)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        #  nmcli device wifi connect "J-Home Network"
        #  nmcli device wifi connect "J-Home Network" password ""
        #  D -> Connected
        #  E -> password
        #  D ->
        #  E -> Wrong password

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        subprocess.call(['nmcli','radio','wifi','on'])
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('wifi','logo'))))

        self.x = WifiListView(ports)
        self.setCentralWidget(self.x)

        self.menubar = QMenuBar()
        self.menubar.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.menubar.setFont(self.Env.font())
        self.setMenuBar(self.menubar)

        self.scan = QAction()
        self.scan.setText(res.get('@string/scan'))
        self.scan.triggered.connect (self.refresh)
        self.menubar.addAction(self.scan)

        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)
