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
            commands.mkdir([dirname])
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
            commands.cat (['-c',filename])
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

        self.dir = files.readall('/proc/info/pwd')
        files.write('/proc/info/dsel', self.dir)
        self.listdir = (files.list(self.dir))
        self.listdir.sort()

        #self.clicked[QtCore.QModelIndex].connect(self.on_clicked)
        self.doubleClicked[QtCore.QModelIndex].connect (self.on_clicked)

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

    def __init__(self,args):
        super().__init__()

        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]



        if not self.External == None:
            if not self.External[0]==None:
                if permissions.check(files.output(self.External[0]), "r", files.readall("/proc/info/su")):
                    if files.isdir (files.output(self.External[0])):
                        files.write('/proc/info/pwd',files.output(self.External[0]))

        ## Menubar ##

        self.x = FileListView([self.Env])

        self.menubar = self.menuBar()
        self.menubar.setFont(self.Env.font())

        self.file = self.menubar.addMenu(res.get('@string/file'))
        self.file.setFont(self.Env.font())

        ## File menu

        self.new_file = self.file.addAction(res.get('@string/newfile'))
        self.new_file.setFont(self.Env.font())
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
        ##

        self.new_folder = self.file.addAction(res.get('@string/newfolder'))
        self.new_folder.triggered.connect(self.New_Folder)
        self.new_folder.setFont(self.Env.font())
        self.new_folder.setIcon(QIcon(res.get(res.etc("roller","folder-icon"))))

        self.exit = self.file.addAction(res.get('@string/exit'))
        self.exit.triggered.connect(self.Widget.Close)
        self.exit.setFont(self.Env.font())
        self.exit.setIcon(QIcon(res.get(res.etc("roller","exit-icon"))))

        ## end File menu

        ## end Menubar

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QtGui.QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.Widget.Resize (self,int(res.etc(self.AppName,"width")),int(res.etc(self.AppName,"height")))

        self.setCentralWidget(self.x)

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