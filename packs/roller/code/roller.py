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

import sys , os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from libabr import Files, Control, System, Res, Commands, Permissions, App

res = Res()
files = Files()
control = Control()
commands = Commands()
permissions = Permissions()
app = App()

## Get data ##
def getdata (name):
    return control.read_record (name,'/etc/gui')

class FileListView (QtWidgets.QListView):
    AppName = "roller"

    def format(self, it, text):
        if text.startswith ('.') and not files.readall('/etc/default/hidden_files')=='Yes':
            it.clearData()
        else:
            if files.isdir(self.dir + '/' + text):
                it.setIcon(QtGui.QIcon(res.get(res.etc("roller","folder-icon"))))
            else:
                format = it.whatsThis().split('.')
                format = max(format)
                if it.whatsThis().endswith(format):
                    logo = control.read_record(format + '.icon', '/etc/ext')
                    if not logo == None:
                        it.setIcon(QtGui.QIcon(res.get(logo)))
                    else:
                        it.setIcon(QtGui.QIcon(res.get(res.etc("roller",'file-icon'))))
                else:
                    it.setIcon(QtGui.QIcon(res.get(res.etc("roller",'file-icon'))))

    def mkdir (self,dirname):
        if files.isfile(dirname):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isfile'),res.get('@string/isfile_msg').replace('{0}',dirname)])
            app.switch('roller')
        else:
            it = QtGui.QStandardItem(dirname)
            it.setWhatsThis(self.dir + "/" + dirname)
            it.setIcon(QtGui.QIcon(res.get(res.etc("roller",'folder-icon'))))
            self.entry.appendRow(it)

            try:
                commands.mkc([it.whatsThis().replace(f'/stor/{files.readall("/proc/info/mnt")}/','')])
            except:
                files.mkdir(dirname)

            it.setFont(self.Env.font())
            x = self.Env.font()

    def mkfile (self,filename):
        if files.isdir(filename ):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                                                         res.get('@string/isdir_msg').replace("{0}",filename)])
            app.switch('roller')
        else:
            it = QtGui.QStandardItem(filename)
            it.setWhatsThis(self.dir + "/" + filename)
            it.setIcon(QtGui.QIcon(res.get(res.etc('roller','file-icon'))))
            self.entry.appendRow(it)
            self.format(it, filename)
            files.create(filename)

            try:
                commands.up([it.whatsThis().replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
            except:
                pass

            it.setFont(self.Env.font())

    def mkcode (self,filename):
        self.code = files.readall('/tmp/code.tmp')
        self.ext = control.read_record('ext',res.get(self.code))

        if files.isdir(filename+f".{self.ext}"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),res.get('@string/isdir_msg').replace("{0}",filename+f".{self.ext}")])
            app.switch('roller')
        else:
            self.mkfile(filename+f".{self.ext}")

            files.write(self.dir + "/" + filename+f'.{self.ext}',files.readall(res.get(control.read_record('connect',res.get(self.code)))))

            try:
                commands.up([str(self.dir + "/" + filename+f".{self.ext}").replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
            except:
                pass

    def __init__(self,ports):
        super().__init__()
        self.Env = ports[0]
        self.Widget = ports[1]
        self.Dialog = ports[2]

        self.entry = QtGui.QStandardItemModel()
        self.parentdir = QtGui.QStandardItem()
        self.parentdir.setIcon(QtGui.QIcon(res.get(res.etc("roller",'folder-icon'))))
        self.entry.appendRow(self.parentdir)
        self.setModel(self.entry)
        iconsize = int(res.etc("roller","icon-size"))
        self.setIconSize(QtCore.QSize(iconsize,iconsize))

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

        #self.w.hide()

        #self.clicked[QtCore.QModelIndex].connect(self.on_clicked)
        self.doubleClicked[QtCore.QModelIndex].connect (self.on_clicked)
        self.clicked[QModelIndex].connect (self.onSelect)

        for text in self.listdir:
            if files.isdir(self.dir+"/"+text):
                it = QtGui.QStandardItem(text)
                it.setWhatsThis(self.dir + "/" + text)
                self.format(it, text)
                self.entry.appendRow(it)
                it.setFont(self.Env.font())

        for text in self.listdir:
            if files.isfile(self.dir + "/" + text):
                it = QtGui.QStandardItem(text)
                it.setWhatsThis(self.dir + "/" + text)
                self.format(it, text)
                self.entry.appendRow(it)
                it.setFont(self.Env.font())

        self.itemOld = QtGui.QStandardItem("text")

    def onSelect (self,index):
        self.item = self.entry.itemFromIndex(index)
        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            if files.isdir(self.item.whatsThis()):
                files.write('/proc/info/wsel', self.item.whatsThis())  # Send Directory selected
            elif files.isfile(self.item.whatsThis()):
                files.write('/proc/info/wsel', self.item.whatsThis())  # Send File selected


    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)
        x = hasattr(self.item,'whatsThis') # W3CSHCOOL.COM LEARN IT

        if x == True:
            if self.item.whatsThis() == "<parent>":
                commands.cd (['..'])
                self.dir = files.readall('/proc/info/pwd')
                files.write('/proc/info/dsel',self.dir)
                self.listdir = files.list(self.dir)
                self.listdir.sort() # Credit: https://www.geeksforgeeks.org/sort-in-python/

                self.entry = QtGui.QStandardItemModel()
                self.setModel(self.entry)
                self.setIconSize(QtCore.QSize(int(res.etc(self.AppName,"icon-size")), int(res.etc(self.AppName,"icon-size"))))
                self.clicked[QtCore.QModelIndex].connect(self.on_clicked)
                self.parentdir = QtGui.QStandardItem()
                self.parentdir.setIcon(QtGui.QIcon(res.get(res.etc("roller","folder-icon"))))
                self.parentdir.setWhatsThis('<parent>')
                self.entry.appendRow(self.parentdir)

                for text in self.listdir:
                    if files.isdir(self.dir+"/"+text):
                        it = QtGui.QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
                        self.format(it, text)
                        self.entry.appendRow(it)
                        it.setFont(self.Env.font())

                for text in self.listdir:
                    if files.isfile(self.dir+"/"+text):
                        it = QtGui.QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
                        self.format(it, text)
                        self.entry.appendRow(it)
                        it.setFont(self.Env.font())

            elif files.isdir(self.item.whatsThis()):
                files.write('/proc/info/dsel', self.item.whatsThis())  # Send Directory selected
                commands.cd ([self.item.whatsThis()])
                self.dir = files.readall("/proc/info/pwd")
                self.listdir = files.list(self.dir)
                self.listdir.sort()

                self.entry = QtGui.QStandardItemModel()
                self.setModel(self.entry)
                self.setIconSize(QtCore.QSize(int(res.etc(self.AppName,"icon-size")), int(res.etc(self.AppName,"icon-size"))))
                self.clicked[QtCore.QModelIndex].connect(self.on_clicked)
                self.parentdir = QtGui.QStandardItem()
                self.parentdir.setIcon(QtGui.QIcon(res.get(res.etc("roller","folder-icon"))))
                self.parentdir.setWhatsThis('<parent>')
                self.entry.appendRow(self.parentdir)

                for text in self.listdir:
                    if files.isdir(self.dir+"/"+text):
                        it = QtGui.QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
                        self.format(it, text)
                        self.entry.appendRow(it)
                        it.setFont(self.Env.font())
                for text in self.listdir:
                    if files.isfile(self.dir+"/"+text):
                        it = QtGui.QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
                        self.format(it, text)
                        self.entry.appendRow(it)
                        it.setFont(self.Env.font())

            elif files.isfile (self.item.whatsThis()):
                files.write ('/proc/info/fsel',self.item.whatsThis()) # Send File selected


class MainApp (QtWidgets.QMainWindow):

    def contextMenuEvent(self, event):
        self.file.setGeometry(int(self.width()/2),int(self.height()/2),self.file.width(),self.file.height())
        try:
            if not files.isfile (files.readall('/proc/info/wsel')) and not files.readall('/proc/info/wsel')==files.output('/'):
                self.open.setVisible(False)
                self.openwith.setVisible(False)
                self.execute.setVisible(False)
                self.delete.setVisible(True)
                self.copy.setVisible(True)
                self.paste.setVisible(True)
                self.cut.setVisible(True)
                self.rename.setVisible(True)
                #self.archivex.setVisible(True)
                self.extractx.setVisible(False)
            elif files.readall('/proc/info/wsel')==files.output('/'):
                self.open.setVisible(False)
                self.openwith.setVisible(False)
                self.execute.setVisible(False)
                self.delete.setVisible(False)
                self.copy.setVisible(False)
                self.paste.setVisible(True)
                self.cut.setVisible(False)
                self.rename.setVisible(False)
                #self.archivex.setVisible(False)
                self.extractx.setVisible(False)
            else:
                self.open.setVisible(True)
                self.openwith.setVisible(True)
                self.execute.setVisible(True)
                self.delete.setVisible(True)
                self.copy.setVisible(True)
                self.paste.setVisible(True)
                self.cut.setVisible(True)
                self.rename.setVisible(True)
                #self.archivex.setVisible(True)
                self.extractx.setVisible(True)

            self.exit.setVisible(False)
        except:
            pass

        action = self.file.exec_()

    def format (self,it,text):
        if os.path.isdir(self.dir + '/' + text):
            it.setIcon(QtGui.QIcon(res.get(res.etc("roller","folder-icon"))))
        else:
            format = it.whatsThis().split('.')
            format = max(format)
            if it.whatsThis().endswith(format):
                logo = control.read_record(format + '.icon', '/etc/ext')
                if not logo==None:
                    it.setIcon(QtGui.QIcon(res.get(logo)))
                else:
                    it.setIcon(QtGui.QIcon(res.get(res.etc("roller","file-icon"))))
            else:
                it.setIcon(QtGui.QIcon(res.get(res.etc("roller","file-icon"))))

    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QtCore.QTimer.singleShot(1,self.onCloseProcess)

    def refresh (self):
        self.x = FileListView([self.Env,self.Widget,self])
        self.setCentralWidget(self.x)

    def delete_act (self):
        try:
            self.wsel = files.readall('/proc/info/wsel')
            if files.isdir(self.wsel):
                app.switch('roller')
                self.Env.RunApp('bool',[res.get('@string/delete'),res.get('@string/deletem'),self.delete_act_])
                app.switch('roller')
            else:
                app.switch('roller')
                self.Env.RunApp('bool', [res.get('@string/delete'), res.get('@string/deletemf'), self.delete_act_])
                app.switch('roller')
        except:
            pass

    def delete_act_ (self,yes):
        if yes:
            try:
                if files.isdir(self.wsel) or files.isfile(self.wsel):
                    if files.isfile(self.wsel):
                        try:
                            commands.rem([str(self.wsel).replace(
                                f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                        except:
                            commands.rm([self.wsel])
                    else:
                        commands.rm([self.wsel])

                self.refresh()
            except: pass

    def rename_act (self):
        try:
            self.wsel = files.readall('/proc/info/wsel')
            app.switch('roller')
            self.Env.RunApp('input',[res.get('@string/rename'),self.rename_act_])
            app.switch('roller')
        except: pass

    def rename_act_(self,text):
        if files.isdir(self.wsel) or files.isfile(self.wsel):
            if files.isfile(self.wsel):
                try:
                    commands.cp([self.wsel, text])
                    commands.up([str(files.output(text)).replace(
                        f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                    commands.rem([str(self.wsel).replace(
                        f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                except:
                    commands.mv([self.wsel, text])
            else:
                commands.mv([self.wsel, text])

        self.refresh()

    def copy_act (self):
        try:
            self.wsel = files.readall('/proc/info/wsel')

            if files.isdir('/tmp/roller-copy'): files.removedirs('/tmp/roller-copy')
            elif files.isfile('/tmp/roller-copy'): files.remove('/tmp/roller-copy')

            files.write('/tmp/roller-src.tmp',self.wsel)

            if files.isdir(self.wsel) or files.isfile(self.wsel):
                commands.cp([self.wsel,'/tmp/roller-copy'])
        except:
            pass

    def open_act (self):
        try:
            commands.down([files.readall('/proc/info/wsel').replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
        except:
            pass

        splitext = files.output(files.readall('/proc/info/wsel')).split('.')
        ext = max(splitext)

        always = control.read_record (f'{ext}.always','/etc/ext')

        if always==None:
            self.open_with_act()
        elif always=='persia':
            self.Env.RunApp('persia', [None,files.readall('/proc/info/wsel')])
        else:
            self.Env.RunApp(always, [files.readall('/proc/info/wsel')])

    def open_with_act (self):
        try:
            commands.down([files.readall('/proc/info/wsel').replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
        except:
            pass

        self.Env.RunApp('open',[files.readall('/proc/info/wsel')])

    def cut_act(self):
        try:
            self.wsel = files.readall('/proc/info/wsel')

            if files.isdir('/tmp/roller-copy'):
                files.removedirs('/tmp/roller-copy')

            elif files.isfile('/tmp/roller-copy'):
                files.remove('/tmp/roller-copy')

            files.write('/tmp/roller-src.tmp', self.wsel)

            if files.isdir(self.wsel) or files.isfile(self.wsel):

                if files.isfile(self.wsel):
                    try:
                        commands.cp([self.wsel, '/tmp/roller-copy'])
                        commands.rem([str(self.wsel).replace(
                            f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                    except:
                        commands.mv([self.wsel, '/tmp/roller-copy'])
                else:
                    commands.mv ([self.wsel,'/tmp/roller-copy'])

            self.refresh()
        except: pass

    def execute_act (self):
        try:
            if permissions.check(files.readall('/proc/info/wsel'),'x',self.Env.username):
                try:
                    commands.down(
                        [files.readall('/proc/info/wsel').replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                except:
                    pass

                execute_file = files.readall('/proc/info/wsel')

                if execute_file.endswith ('.pashm'):
                    files.write('/tmp/exec.sa', f'''pashmak {execute_file}
rm /tmp/exec.sa
pause''')
                    self.Env.RunApp('commento', [None])
                    app.switch('roller')
                else:
                    files.write('/tmp/exec.sa', f'''{execute_file.replace ('.pyc','').replace ('.sa','')}
rm /tmp/exec.sa
pause''')
                    self.Env.RunApp('commento', [None])
                    app.switch('roller')
            else:
                app.switch('roller')
                self.Env.RunApp('text', [res.get('@string/perm'),res.get('@string/permm')])
                app.switch('roller')
        except:
            pass

    def zip_act (self):
        try:
            if permissions.check(files.readall('/proc/info/wsel'),'r',self.Env.username) and permissions.check(f"{files.readall('/proc/info/wsel')}.zip",'w',self.Env.username):
                if files.isdir (files.readall("/proc/info/wsel")):
                    commands.zip ([files.readall("/proc/info/wsel")])
                    if files.isfile (f"{files.readall('/proc/info/wsel')}.tar.zip"):
                        try:
                            commands.up(
                                [(f"{files.readall('/proc/info/wsel')}.tar.zip").replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                        except:
                            pass
            else:
                app.switch('roller')
                self.Env.RunApp('text', [res.get('@string/perm'),res.get('@string/permm')])
                app.switch('roller')
            self.refresh()
        except:
            pass

    def tar_act (self):
        try:
            if permissions.check(files.readall('/proc/info/wsel'),'r',self.Env.username) and permissions.check(f"{files.readall('/proc/info/wsel')}.tar",'w',self.Env.username):
                if files.isdir (files.readall("/proc/info/wsel")):
                    commands.tar ([files.readall("/proc/info/wsel")])
                    if files.isfile (f"{files.readall('/proc/info/wsel')}.tar"):
                        try:
                            commands.up(
                                [(f"{files.readall('/proc/info/wsel')}.tar").replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                        except:
                            pass
            else:
                app.switch('roller')
                self.Env.RunApp('text', [res.get('@string/perm'),res.get('@string/permm')])
                app.switch('roller')
            self.refresh()
        except:
            pass

    def gztar_act (self):
        try:
            if permissions.check(files.readall('/proc/info/wsel'),'r',self.Env.username) and permissions.check(f"{files.readall('/proc/info/wsel')}.tar.gz",'w',self.Env.username):
                if files.isdir (files.readall("/proc/info/wsel")):
                    commands.gzip ([files.readall("/proc/info/wsel")])
                    if files.isfile (f"{files.readall('/proc/info/wsel')}.tar.gz"):
                        try:
                            commands.up(
                                [(f"{files.readall('/proc/info/wsel')}.tar.gz").replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                        except:
                            pass
            else:
                app.switch('roller')
                self.Env.RunApp('text', [res.get('@string/perm'),res.get('@string/permm')])
                app.switch('roller')
            self.refresh()
        except:
            pass

    def xztar_act (self):
        try:
            if permissions.check(files.readall('/proc/info/wsel'),'r',self.Env.username) and permissions.check(f"{files.readall('/proc/info/wsel')}.tar.xz",'w',self.Env.username):
                if files.isdir (files.readall("/proc/info/wsel")):
                    commands.xzip ([files.readall("/proc/info/wsel")])
                    if files.isfile (f"{files.readall('/proc/info/wsel')}.tar.xz"):
                        try:
                            commands.up(
                                [(f"{files.readall('/proc/info/wsel')}.tar.xz").replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                        except:
                            pass
            else:
                app.switch('roller')
                self.Env.RunApp('text', [res.get('@string/perm'),res.get('@string/permm')])
                app.switch('roller')
            self.refresh()
        except:
            pass

    def bz2tar_act (self):
        try:
            if permissions.check(files.readall('/proc/info/wsel'),'r',self.Env.username) and permissions.check(f"{files.readall('/proc/info/wsel')}.tar.bz2",'w',self.Env.username):
                if files.isdir (files.readall("/proc/info/wsel")):
                    commands.bzip ([files.readall("/proc/info/wsel")])
                    if files.isfile (f"{files.readall('/proc/info/wsel')}.tar.bz2"):
                        try:
                            commands.up(
                                [(f"{files.readall('/proc/info/wsel')}.tar.bz2").replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                        except:
                            pass
            else:
                app.switch('roller')
                self.Env.RunApp('text', [res.get('@string/perm'),res.get('@string/permm')])
                app.switch('roller')
            self.refresh()
        except:
            pass

    def extract_act (self):
        try:
            wsel = files.readall('/proc/info/wsel')
            fselx = wsel.replace ('.zip','').replace ('.tar.xz','').replace ('.tar.gz','').replace ('.tar.bz2','').replace ('.tar','').replace ('.pa','').replace ('.apk','').replace ('.jar','')
            if permissions.check(wsel,'r',self.Env.username) and permissions.check(fselx,'w',self.Env.username):
                if wsel.endswith('.zip') or wsel.endswith('.pa') or wsel.endswith('.apk') or wsel.endswith('.jar'):
                    commands.unzip ([wsel,fselx])
                elif wsel.endswith('.tar.bz2'):
                    commands.bunzip ([wsel,fselx])
                elif wsel.endswith('.tar.gz'):
                    commands.gunzip ([wsel,fselx])
                elif wsel.endswith('.tar.xz'):
                    commands.xunzip ([wsel,fselx])
                elif wsel.endswith('.tar'):
                    commands.untar ([wsel,fselx])
                self.refresh()
            else:
                app.switch('roller')
                self.Env.RunApp('text', [res.get('@string/perm'),res.get('@string/permm')])
                app.switch('roller')
        except:
            pass

    def paste_act (self):
        try:
            self.src = files.readall('/tmp/roller-src.tmp')
            self.dest = files.output(files.filename(self.src))

            if files.isdir(self.dest):
                pass
            elif files.isfile(self.dest):
                pass
            else:
                if files.isdir('/tmp/roller-copy') or files.isfile('/tmp/roller-copy'):
                    commands.mv (['/tmp/roller-copy',self.dest])

                    if files.isfile (self.dest):
                        try:
                            commands.up(
                                [self.dest.replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
                        except:
                            pass
        except:
            pass
        self.refresh()

    def __init__(self,args):
        super().__init__()

        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]
        self.onCloseProcess()


        if not self.External == None:
            if not self.External[0]==None:
                if permissions.check(files.output(self.External[0]), "r", files.readall("/proc/info/su")):
                    if files.isdir (files.output(self.External[0])):
                        files.write('/proc/info/pwd',files.output(self.External[0]))

        ## Menubar ##
        self.x = FileListView([self.Env,self.Widget,self])
        self.setCentralWidget(self.x)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuEvent)

        self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.menubar = self.menuBar()
        self.menubar.setFont(self.Env.font())
        self.menubar.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)

        self.file = self.menubar.addMenu(res.get('@string/file'))
        self.file.setStyleSheet('background:none;color: black;')
        self.file.setFont(self.Env.font())
        ## File menu

        self.new_file = self.file.addAction(res.get('@string/newfile'))
        self.new_file.setFont(self.Env.font())
        self.new_file.setShortcut('Ctrl+Alt+F')
        self.new_file.triggered.connect(self.New_File)
        self.new_file.setIcon(QIcon(res.get(res.etc("roller","file-icon"))))

        self.new_code = self.file.addMenu(res.get('@string/newcode'))
        self.new_code.setStyleSheet('background:none;color: black;')
        self.new_code.setFont(self.Env.font())
        self.new_code.setIcon(QIcon(res.get(res.etc('roller','c'))))

        ##
        self.templist = files.list('/usr/share/templates')
        self.templist.sort()
        for i in self.templist:
            if i.endswith('.desk'):
                self.new_cz = self.new_code.addAction(control.read_record(f'name[{control.read_record("locale","/etc/gui")}]',res.get(f'@temp/{i}')))
                self.new_cz.setFont(self.Env.font())
                self.new_cz.setObjectName(i)
                self.new_cz.triggered.connect(self.New_Code)
                self.new_cz.setIcon(QIcon(res.get(control.read_record('logo',res.get(f'@temp/{i}')))))

        self.new_folder = self.file.addAction(res.get('@string/newfolder'))
        self.new_folder.triggered.connect(self.New_Folder)
        self.new_folder.setShortcut('Ctrl+Alt+D')
        self.new_folder.setFont(self.Env.font())
        self.new_folder.setIcon(QIcon(res.get('@icon/breeze-newfolder')))

        self.open = self.file.addAction(res.get('@string/open'))
        self.open.setIcon(QIcon(res.get('@icon/breeze-open')))
        self.open.triggered.connect(self.open_act)
        self.open.setShortcut('Ctrl+O')
        self.open.setFont(self.Env.font())

        self.openwith = self.file.addAction(res.get('@string/openwith'))
        self.openwith.triggered.connect(self.open_with_act)
        self.openwith.setShortcut('Ctrl+Alt+O')
        self.openwith.setIcon(QIcon(res.get('@icon/breeze-open')))
        self.openwith.setFont(self.Env.font())

        self.execute = self.file.addAction(res.get('@string/execute'))
        self.execute.triggered.connect(self.execute_act)
        self.execute.setFont(self.Env.font())
        self.execute.setIcon(QIcon(res.get('@icon/breeze-execute')))
        self.execute.setShortcut('Ctrl+Alt+X')

        self.cut = self.file.addAction(res.get('@string/cut'))
        self.cut.triggered.connect(self.cut_act)
        self.cut.setShortcut('Ctrl+X')
        self.cut.setIcon(QIcon(res.get('@icon/breeze-cut')))
        self.cut.setFont(self.Env.font())

        self.copy = self.file.addAction(res.get('@string/copy'))
        self.copy.triggered.connect(self.copy_act)
        self.copy.setIcon(QIcon(res.get('@icon/breeze-copy')))
        self.copy.setFont(self.Env.font())
        self.copy.setShortcut('Ctrl+C')

        self.paste = self.file.addAction(res.get('@string/paste'))
        self.paste.triggered.connect(self.paste_act)
        self.paste.setFont(self.Env.font())
        self.paste.setIcon(QIcon(res.get('@icon/breeze-paste')))
        self.paste.setShortcut('Ctrl+V')

        self.delete = self.file.addAction(res.get('@string/delete'))
        self.delete.setIcon(QIcon(res.get('@icon/breeze-delete')))
        self.delete.setShortcut('Ctrl+T')
        self.delete.triggered.connect (self.delete_act)
        self.delete.setFont(self.Env.font())

        self.rename = self.file.addAction(res.get('@string/rename'))
        self.rename.triggered.connect(self.rename_act)
        self.rename.setShortcut('F2')
        self.rename.setIcon(QIcon(res.get('@icon/breeze-rename')))
        self.rename.setFont(self.Env.font())

        self.archivex = self.file.addMenu (res.get('@string/archive'))
        self.archivex.setIcon (QIcon(res.get('@icon/breeze-compress')))
        self.archivex.setStyleSheet('background:none;color: black;')
        self.archivex.setFont(self.Env.font())

        self.zipa = self.archivex.addAction('zip')
        self.zipa.triggered.connect(self.zip_act)
        self.zipa.setIcon(QIcon(res.get('@icon/breeze-zip')))
        self.zipa.setFont(self.Env.font())

        self.tar = self.archivex.addAction('tar')
        self.tar.triggered.connect(self.tar_act)
        self.tar.setIcon(QIcon(res.get('@icon/breeze-tar')))
        self.tar.setFont(self.Env.font())

        self.xztar = self.archivex.addAction('tar.xz')
        self.xztar.triggered.connect(self.xztar_act)
        self.xztar.setIcon(QIcon(res.get('@icon/breeze-xz')))
        self.xztar.setFont(self.Env.font())

        self.gztar = self.archivex.addAction('tar.gz')
        self.gztar.triggered.connect(self.gztar_act)
        self.gztar.setIcon(QIcon(res.get('@icon/breeze-gz')))
        self.gztar.setFont(self.Env.font())

        self.bz2tar = self.archivex.addAction('tar.bz2')
        self.bz2tar.triggered.connect(self.bz2tar_act)
        self.bz2tar.setIcon(QIcon(res.get('@icon/breeze-bz')))
        self.bz2tar.setFont(self.Env.font())

        self.extractx = self.file.addAction (res.get('@string/extract'))
        self.extractx.setIcon (QIcon(res.get('@icon/breeze-extract')))
        self.extractx.triggered.connect(self.extract_act)
        self.extractx.setFont(self.Env.font())

        self.exit = self.file.addAction(res.get('@string/exit'))
        self.exit.triggered.connect(self.Widget.Close)
        self.exit.setFont(self.Env.font())
        self.exit.setShortcut('Alt+F4')
        self.exit.setIcon(QIcon(res.get('@string/breeze-exit')))

        self.open.setVisible(False)
        self.openwith.setVisible(False)
        self.execute.setVisible(False)
        self.delete.setVisible(False)
        self.copy.setVisible(False)
        self.paste.setVisible(True)
        self.cut.setVisible(False)
        self.rename.setVisible(False)
        self.extractx.setVisible(False)
        self.archivex.setVisible(False)

        ## end File menu

        ## end Menubar

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QtGui.QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.Widget.Resize (self,int(res.etc(self.AppName,"width")),int(res.etc(self.AppName,"height")))

    def New_Folder (self):
        app.switch('roller')
        self.Env.RunApp('input',[res.get('@string/foldername'),self.x.mkdir])
        app.switch('roller')

    def New_File (self):
        app.switch('roller')
        self.Env.RunApp('input',[res.get('@string/filename'),self.x.mkfile])
        app.switch('roller')

    def New_Code (self):
        files.write('/tmp/code.tmp','@temp/'+self.sender().objectName())
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkcode])
        app.switch('roller')