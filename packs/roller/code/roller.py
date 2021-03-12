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
            files.mkdir(dirname)
            it.setFont(self.Env.font())
            x = self.Env.font()
            print(x.family())

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
            it.setFont(self.Env.font())

    def mkc (self,filename):
        if files.isdir(filename +".c"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                                                         res.get('@string/isdir_msg').replace("{0}",filename+".c")])
            app.switch('roller')
        else:
            self.mkfile(filename+".c")
            files.write(self.dir + "/" + filename+'.c',files.readall(res.get('@temp/untitled.c')))

    def mkcpp (self,filename):
        if files.isdir(filename+".cpp"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".cpp")])
            app.switch('roller')
        else:
            self.mkfile(filename+".cpp")
            files.write(self.dir + "/" + filename+'.cpp',files.readall(res.get('@temp/untitled.cpp')))

    def mkjava (self,filename):
        if files.isdir(filename+".java"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".java")])
            app.switch('roller')
        else:
            self.mkfile(filename+".java")
            files.write(self.dir + "/" + filename+'.java',files.readall(res.get('@temp/untitled.java')).replace("MainApp",filename))

    def mkjs (self,filename):
        if files.isdir(filename+".js"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".js")])
            app.switch('roller')
        else:
            self.mkfile(filename+".js")
            files.write(self.dir + "/" + filename+'.js',files.readall(res.get('@temp/untitled.js')))

    def mkui (self,filename):
        if files.isdir(filename+".ui"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".ui")])
            app.switch('roller')
        else:
            self.mkfile(filename+".ui")
            files.write(self.dir + "/" + filename+'.ui',files.readall(res.get('@temp/untitled.ui')))

    def mkphp (self,filename):
        if files.isdir(filename+".php"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".php")])
            app.switch('roller')
        else:
            self.mkfile(filename+".php")
            files.write(self.dir + "/" + filename+".php",files.readall(res.get('@temp/untitled.php')))

    def mkhtml (self,filename):
        if files.isdir(filename+".html"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".html")])
            app.switch('roller')
        else:
            self.mkfile(filename+".html")
            files.write(self.dir + "/" + filename+".html",files.readall(res.get('@temp/untitled.html')))

    def mkcs (self,filename):
        if files.isdir(filename+".cs"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".cs")])
            app.switch('roller')
        else:
            self.mkfile(filename+".cs")
            files.write(self.dir + "/" + filename+".cs",files.readall(res.get('@temp/untitled.cs')))

    def mksa (self,filename):
        if files.isdir(filename+".sa"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".sa")])
            app.switch('roller')
        else:
            self.mkfile(filename+".sa")
            files.write(self.dir + "/" + filename+".sa",files.readall(res.get('@temp/untitled.sa')))

    def mkpy (self,filename):
        if files.isdir(filename+".py"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".py")])
            app.switch('roller')
        else:
            self.mkfile(filename+".py")
            files.write(self.dir + "/" + filename+".py",files.readall(res.get('@temp/untitled.py')))

    def mkpygui (self,filename):
        if files.isdir(filename+".py"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".py")])
            app.switch('roller')
        else:
            self.mkfile(filename+".py")
            files.write(self.dir + "/" + filename+".py",files.readall(res.get('@temp/untitled-gui.py')))

    def mkpyweb (self,filename):
        if files.isdir(filename+".py"):
            app.switch('roller')
            self.Env.RunApp('text', [res.get('@string/isdir'),
                                     res.get('@string/isdir_msg').replace("{0}", filename + ".py")])
            app.switch('roller')
        else:
            self.mkfile(filename+".py")
            files.write(self.dir + "/" + filename+".py",files.readall(res.get('@temp/untitled-web.py')))

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

        self.setStyleSheet(f'background:{res.etc("roller","bgcolor")};')

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
        if not files.isfile (files.readall('/proc/info/wsel')) and not files.readall('/proc/info/wsel')==files.output('/'):
            self.open.setVisible(False)
            self.openwith.setVisible(False)
            self.execute.setVisible(False)
            self.delete.setVisible(True)
            self.copy.setVisible(True)
            self.paste.setVisible(True)
            self.cut.setVisible(True)
            self.rename.setVisible(True)
        elif files.readall('/proc/info/wsel')==files.output('/'):
            self.open.setVisible(False)
            self.openwith.setVisible(False)
            self.execute.setVisible(False)
            self.delete.setVisible(False)
            self.copy.setVisible(False)
            self.paste.setVisible(True)
            self.cut.setVisible(False)
            self.rename.setVisible(False)
        else:
            self.open.setVisible(True)
            self.openwith.setVisible(True)
            self.execute.setVisible(True)
            self.delete.setVisible(True)
            self.copy.setVisible(True)
            self.paste.setVisible(True)
            self.cut.setVisible(True)
            self.rename.setVisible(True)

        self.exit.setVisible(False)

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
        self.wsel = files.readall('/proc/info/wsel')
        if files.isdir(self.wsel):
            app.switch('roller')
            self.Env.RunApp('bool',[res.get('@string/delete'),'Do you want to delete this directory? ',self.delete_act_])
            app.switch('roller')
        else:
            app.switch('roller')
            self.Env.RunApp('bool', [res.get('@string/delete'), 'Do you want to delete this file? ', self.delete_act_])
            app.switch('roller')

    def delete_act_ (self,yes):
        if yes:
            if files.isdir(self.wsel) or files.isfile(self.wsel):
                commands.rm ([self.wsel])

            self.refresh()

    def rename_act (self):
        self.wsel = files.readall('/proc/info/wsel')
        app.switch('roller')
        self.Env.RunApp('input',[res.get('@string/rename'),self.rename_act_])
        app.switch('roller')

    def rename_act_(self,text):
        if files.isdir(self.wsel) or files.isfile(self.wsel):
            commands.mv ([self.wsel,text])

        self.refresh()

    def copy_act (self):
        self.wsel = files.readall('/proc/info/wsel')

        if files.isdir('/tmp/roller-copy'): files.removedirs('/tmp/roller-copy')
        elif files.isfile('/tmp/roller-copy'): files.remove('/tmp/roller-copy')

        files.write('/tmp/roller-src.tmp',self.wsel)

        if files.isdir(self.wsel) or files.isfile(self.wsel):
            commands.cp([self.wsel,'/tmp/roller-copy'])

    def open_act (self):
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
        self.Env.RunApp('open',[files.readall('/proc/info/wsel')])

    def cut_act(self):
        self.wsel = files.readall('/proc/info/wsel')

        if files.isdir('/tmp/roller-copy'):
            files.removedirs('/tmp/roller-copy')
        elif files.isfile('/tmp/roller-copy'):
            files.remove('/tmp/roller-copy')

        files.write('/tmp/roller-src.tmp', self.wsel)

        if files.isdir(self.wsel) or files.isfile(self.wsel):
            commands.mv ([self.wsel,'/tmp/roller-copy'])

        self.refresh()

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
            app.switch('roller')
            self.Env.RunApp('text', ['Permission denied','Cannot execute this file; Permission denied'])
            app.switch('roller')

    def paste_act (self):
        self.src = files.readall('/tmp/roller-src.tmp')
        self.dest = files.output(files.filename(self.src))

        if files.isdir(self.dest):
            pass
        elif files.isfile(self.dest):
            pass
        else:
            if files.isdir('/tmp/roller-copy') or files.isfile('/tmp/roller-copy'):
                commands.mv (['/tmp/roller-copy',self.dest])

        self.refresh()

    def __init__(self,args):
        super().__init__()

        self.Backend = args[0]
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

        self.file = self.menubar.addMenu(res.get('@string/file'))
        self.file.setFont(self.Env.font())
        ## File menu

        self.new_file = self.file.addAction(res.get('@string/newfile'))
        self.new_file.setFont(self.Env.font())
        self.new_file.setShortcut('Ctrl+Alt+F')
        self.new_file.triggered.connect(self.New_File)
        self.new_file.setIcon(QIcon(res.get(res.etc("roller","file-icon"))))

        self.new_code = self.file.addMenu(res.get('@string/newcode'))
        self.new_code.setFont(self.Env.font())
        self.new_code.setIcon(QIcon(res.get(res.etc('roller','c'))))

        ##
        self.new_c = self.new_code.addAction(res.get('@string/c'))
        self.new_c.setFont(self.Env.font())
        self.new_c.triggered.connect(self.New_C)
        self.new_c.setIcon(QIcon(res.get(res.etc("roller", "c"))))

        self.new_cpp = self.new_code.addAction(res.get('@string/c++'))
        self.new_cpp.triggered.connect(self.New_Cpp)
        self.new_cpp.setFont(self.Env.font())
        self.new_cpp.setIcon(QIcon(res.get(res.etc("roller", "c++"))))

        self.new_cs = self.new_code.addAction(res.get('@string/csharp'))
        self.new_cs.triggered.connect(self.New_Csharp)
        self.new_cs.setFont(self.Env.font())
        self.new_cs.setIcon(QIcon(res.get(res.etc("roller", "c#"))))

        self.new_html = self.new_code.addAction(res.get('@string/html'))
        self.new_html .triggered.connect(self.New_Html)
        self.new_html.setFont(self.Env.font())
        self.new_html.setIcon(QIcon(res.get(res.etc("roller", "html"))))

        self.new_java = self.new_code.addAction(res.get('@string/java'))
        self.new_java.triggered.connect(self.New_Java)
        self.new_java.setFont(self.Env.font())
        self.new_java.setIcon(QIcon(res.get(res.etc("roller", "java"))))

        self.new_js = self.new_code.addAction(res.get('@string/javascript'))
        self.new_js.triggered.connect(self.New_Js)
        self.new_js.setFont(self.Env.font())
        self.new_js.setIcon(QIcon(res.get(res.etc("roller", "js"))))

        self.new_Php = self.new_code.addAction(res.get('@string/php'))
        self.new_Php.triggered.connect(self.New_Php)
        self.new_Php.setFont(self.Env.font())
        self.new_Php.setIcon(QIcon(res.get(res.etc("roller", "php"))))

        self.new_py = self.new_code.addAction(res.get('@string/python'))
        self.new_py.triggered.connect(self.New_Py)
        self.new_py.setFont(self.Env.font())
        self.new_py.setIcon(QIcon(res.get(res.etc("roller", "py"))))

        self.new_sa = self.new_code.addAction(res.get('@string/saye'))
        self.new_sa.triggered.connect(self.New_Sa)
        self.new_sa.setFont(self.Env.font())
        self.new_sa.setIcon(QIcon(res.get(res.etc("roller", "sa"))))

        self.new_pygui = self.new_code.addAction(res.get('@string/pythongui'))
        self.new_pygui.triggered.connect(self.New_PyGui)
        self.new_pygui.setFont(self.Env.font())
        self.new_pygui.setIcon(QIcon(res.get(res.etc("roller", "py"))))

        self.new_pyweb = self.new_code.addAction(res.get('@string/newpyweb'))
        self.new_pyweb.triggered.connect(self.New_PyWeb)
        self.new_pyweb.setFont(self.Env.font())
        self.new_pyweb.setIcon(QIcon(res.get('@icon/web-browser')))

        self.new_ui = self.new_code.addAction(res.get('@string/uix'))
        self.new_ui.setFont(self.Env.font())
        self.new_ui.triggered.connect(self.New_UI)
        self.new_ui.setIcon(QIcon(res.get('@icon/application-x-designer')))
        ##

        self.new_folder = self.file.addAction(res.get('@string/newfolder'))
        self.new_folder.triggered.connect(self.New_Folder)
        self.new_folder.setShortcut('Ctrl+Alt+D')
        self.new_folder.setFont(self.Env.font())
        self.new_folder.setIcon(QIcon(res.get(res.etc("roller","folder-icon"))))

        self.open = self.file.addAction(res.get('@string/open'))
        self.open.setIcon(QIcon(res.get('@icon/blue-fileopen')))
        self.open.triggered.connect(self.open_act)
        self.open.setShortcut('Ctrl+O')
        self.open.setFont(self.Env.font())

        self.openwith = self.file.addAction(res.get('@string/openwith'))
        self.openwith.triggered.connect(self.open_with_act)
        self.openwith.setShortcut('Ctrl+Alt+O')

        self.openwith.setIcon(QIcon(res.get('@icon/blue-fileopen')))
        self.openwith.setFont(self.Env.font())

        self.execute = self.file.addAction(res.get('@string/execute'))
        self.execute.triggered.connect(self.execute_act)
        self.execute.setFont(self.Env.font())
        self.execute.setIcon(QIcon(res.get('@icon/execute')))
        self.execute.setShortcut('Ctrl+Alt+X')

        self.cut = self.file.addAction(res.get('@string/cut'))
        self.cut.triggered.connect(self.cut_act)
        self.cut.setShortcut('Ctrl+X')
        self.cut.setIcon(QIcon(res.get('@icon/cut')))
        self.cut.setFont(self.Env.font())

        self.copy = self.file.addAction(res.get('@string/copy'))
        self.copy.triggered.connect(self.copy_act)
        self.copy.setIcon(QIcon(res.get('@icon/copy')))
        self.copy.setFont(self.Env.font())
        self.copy.setShortcut('Ctrl+C')

        self.paste = self.file.addAction(res.get('@string/paste'))
        self.paste.triggered.connect(self.paste_act)
        self.paste.setFont(self.Env.font())
        self.paste.setIcon(QIcon(res.get('@icon/paste')))
        self.paste.setShortcut('Ctrl+V')

        self.delete = self.file.addAction(res.get('@string/delete'))
        self.delete.setIcon(QIcon(res.get('@icon/delete')))
        self.delete.setShortcut('Ctrl+T')
        self.delete.triggered.connect (self.delete_act)
        self.delete.setFont(self.Env.font())

        self.rename = self.file.addAction(res.get('@string/rename'))
        self.rename.triggered.connect(self.rename_act)
        self.rename.setShortcut('F2')
        self.rename.setIcon(QIcon(res.get('@icon/rename')))
        self.rename.setFont(self.Env.font())

        self.exit = self.file.addAction(res.get('@string/exit'))
        self.exit.triggered.connect(self.Widget.Close)
        self.exit.setFont(self.Env.font())
        self.exit.setShortcut('Alt+F4')
        self.exit.setIcon(QIcon(res.get(res.etc("roller","exit-icon"))))

        self.open.setVisible(False)
        self.openwith.setVisible(False)
        self.execute.setVisible(False)
        self.delete.setVisible(False)
        self.copy.setVisible(False)
        self.paste.setVisible(True)
        self.cut.setVisible(False)
        self.rename.setVisible(False)

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

    def New_C (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkc])
        app.switch('roller')

    def New_Cpp (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkcpp])
        app.switch('roller')

    def New_Csharp (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkcs])
        app.switch('roller')

    def New_Html (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkhtml])
        app.switch('roller')

    def New_Java (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkjava])
        app.switch('roller')

    def New_Js (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkjs])
        app.switch('roller')

    def New_Php (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkphp])
        app.switch('roller')

    def New_Py (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkpy])
        app.switch('roller')

    def New_PyGui (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkpygui])
        app.switch('roller')

    def New_PyWeb (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkpyweb])
        app.switch('roller')

    def New_Sa (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mksa])
        app.switch('roller')

    def New_UI (self):
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkui])
        app.switch('roller')