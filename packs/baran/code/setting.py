from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from libabr import *

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
    def format(self, it):
        if files.isfile (it.whatsThis()):
            name = it.text().replace('.desk','')
            subname = res.etc(name,f'name[{getdata("locale")}]')
            icon = res.etc(name,'logo')
            it.setText(subname)
            it.setFont(self.Env.font())
            it.setIcon(QIcon(res.get(icon)))

    def __init__(self,ports):
        super().__init__()
        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.username = self.Env.username

        self.setStyleSheet("""
                        AppListView,QListView {
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
        # Get font #

        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.listdir = files.list('/usr/share/applications')
        self.listdir.sort()

        for text in self.listdir:

            if res.etc(text.replace('.desk',''),'setting')=='Yes':
                it = QStandardItem(text.replace('.desk',''))
                it.setWhatsThis(f'/usr/share/applications/{text}')
                self.format(it)
                self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            self.Env.RunApp(self.item.whatsThis().replace('.desk','').replace('/usr/share/applications/',''),None)
            files.write('/proc/info/id','desktop')

class MainApp (QMainWindow):
    def onCloseProcess (self):
        if not app.check('setting'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.External = ports[3]

        self.onCloseProcess()
        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('setting','logo'))))

        self.x = AppListView(ports)
        self.setCentralWidget(self.x)

        self.Widget.Resize(self,1000,600)