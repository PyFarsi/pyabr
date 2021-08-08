#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		https://pyabr.ir
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

from PyQt5 import QtWidgets, uic, QtGui,QtCore
import sys, importlib, random,py_compile, baran
from libabr import System, App, Control, Files, Res, Commands
from PyQt5.QtCore import *

res = Res();files = Files();app = App();control=Control();cmd = Commands()

def getdata (name):
    return control.read_record (name,'/etc/gui')

class Barge (baran.BTextEdit):
    def __init__(self,ports):
        super(Barge, self).__init__()

        self.Env = ports[1]

class MainApp(QtWidgets.QMainWindow):
    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QtCore.QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,args):
        super(MainApp, self).__init__()

        # ports
        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        # Connect to onCloseProcess
        self.onCloseProcess()

        # resize
        self.Widget.Resize (self,700,500)
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QtGui.QIcon(res.get(res.etc(self.AppName,'logo'))))

        self.Widget.SetWindowTitle(res.get('@string/untitled'))

        # text box
        self.teEdit = Barge([None,self.Env])
        #self.teEdit.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        # self.text2.setStyleSheet(
        #             f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.teEdit.setStyleSheet("""
        Barge,QTextEdit {
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
            '#ABCDEF', getdata("menu.scroll.color-hover")).replace('!z',getdata("appw.body.bgcolor")).replace('!y',getdata("appw.body.fgcolor")))

        ## External Support Source Code ##
        if not self.External==None:
            if not self.External==[]:
                if not self.External[0]==None:
                    self.teEdit.setPlainText(files.readall(self.External[0]))
                    self.Widget.SetWindowTitle(files.output(self.External[0]))

        self.setCentralWidget(self.teEdit)

        # menubar
        self.menubar = self.menuBar()
        self.menubar.setFont(self.Env.font())
        self.menubar.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.file = self.menubar.addMenu(res.get('@string/file'))
        self.file.setStyleSheet('background:none;color: black;')
        self.file.setFont(self.Env.font())

        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)

        # file menu #
        self.new = self.file.addAction(res.get('@string/new'))
        self.new.setFont(self.Env.font())
        self.new.triggered.connect (self.new_act)
        self.new.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'text'))))
        self.new_page = self.file.addAction(res.get('@string/new_page'))
        self.new_page.triggered.connect (self.new_page_act)
        self.new_page.setFont(self.Env.font())
        self.new_page.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName, 'text'))))
        self.open = self.file.addAction(res.get('@string/open'))
        self.open.setShortcut('Ctrl+O')
        self.open.setFont(self.Env.font())
        self.open.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'open'))))
        self.open.triggered.connect (self.open_act)
        self.save = self.file.addAction(res.get('@string/save'))
        self.save.setShortcut('Ctrl+S')
        self.save.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'save'))))
        self.save.setFont(self.Env.font())
        self.save.triggered.connect (self.save_)
        self.saveas = self.file.addAction(res.get('@string/save_as'))
        self.saveas.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'save-as'))))
        self.saveas.setFont(self.Env.font())
        self.saveas.triggered.connect (self.save_as)
        self.exit = self.file.addAction(res.get('@string/exit'))
        self.exit.setFont(self.Env.font())
        self.exit.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'exit'))))
        self.exit.triggered.connect (self.Widget.Close)
        self.exit.setShortcut('Ctrl+X')

        # code menu
        self.code = self.menubar.addMenu(res.get('@string/code'))
        self.code.setStyleSheet('background:none;color: black;')
        self.code.setFont(self.Env.font())
        self.run = self.code.addAction(res.get('@string/run'))
        self.run.setFont(self.Env.font())
        self.run.triggered.connect (self.run_)
        self.run.setShortcut('Shift+F10')

        self.insert_c = self.code.addMenu(res.get('@string/icode'))
        self.insert_c.setStyleSheet('background:none;color: black;')
        self.insert_c.setFont(self.Env.font())

        # Codes #
        self.templist = files.list('/usr/share/templates')
        self.templist.sort()
        for i in self.templist:
            if i.endswith('.desk'):
                self.new_czx = self.insert_c.addAction(
                    control.read_record(f'name[{control.read_record("locale", "/etc/gui")}]', res.get(f'@temp/{i}')))
                self.new_czx.setFont(self.Env.font())
                self.new_czx.setObjectName(i)
                self.new_czx.triggered.connect(self.langcode)
                self.new_czx.setIcon(QtGui.QIcon(res.get(control.read_record('logo', res.get(f'@temp/{i}')))))

        # set font size
        self.teEdit.setFont(self.Env.font())

    def run_(self):
        control = Control()
        if not self.Widget.WindowTitle()==res.get('@string/untitled'):
            self.save_('')
        else:
            self.save_as()

        ## Run it #

        if self.Widget.WindowTitle().endswith ('.py'):
            # check graphical PyQt5 #
            if files.readall(self.Widget.WindowTitle()).__contains__('from PyQt5') and files.readall(self.Widget.WindowTitle()).__contains__('MainApp'):
                rand = str (random.randint(1000,9999))
                files.create(f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('name[en]','Debug App',f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('name[fa]','برنامه تستی',f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('logo','@icon/breeze-app',f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('exec',f"debug_{rand}",f'/usr/share/applications/debug_{rand}.desk')
                py_compile.compile(files.input(self.Widget.WindowTitle()),files.input(f'/usr/app/debug_{rand}.pyc'))
                self.Env.RunApp(f'debug_{rand}',[None])
                app.switch('barge')
                files.remove(f'/usr/share/applications/debug_{rand}.desk')
                files.remove(f'/usr/app/debug_{rand}.pyc')
            else:
                filename = self.Widget.WindowTitle()
                execname = filename.replace('.py','')
                files.write('/tmp/exec.sa', f'''
echo Running {execname} ...
echo
{execname}
echo
echo Finish running process with exit 0 ...
rm /tmp/exec.sa
pause
                            ''')
                self.Env.RunApp('commento', [None])
                app.switch('barge')

        elif self.Widget.WindowTitle().endswith ('.sa'):
            filename = self.Widget.WindowTitle()
            execname = filename.replace('.sa', '')
            files.write('/tmp/exec.sa', f'''
echo Running {execname} ...
echo
{execname}
echo
echo Finish running process with exit 0 ...
rm /tmp/exec.sa
pause
                                        ''')
            self.Env.RunApp('commento', [None])
            app.switch('barge')
        elif self.Widget.WindowTitle().endswith('.pashm'):
            filename = self.Widget.WindowTitle()
            files.write('/tmp/exec.sa', f'''
echo Running {filename} ...
echo
pashmak {filename}
echo
echo Finish running process with exit 0 ...
rm /tmp/exec.sa
pause
                                                ''')
            self.Env.RunApp('commento', [None])
            app.switch('barge')
        elif self.Widget.WindowTitle().endswith ('.ui'):
            filename = self.Widget.WindowTitle()
            app.switch('barge')
            self.Env.RunApp('uiv',[filename])
            app.switch('barge')
        elif self.Widget.WindowTitle().endswith ('.html') or self.Widget.WindowTitle().endswith ('.htm') or self.Widget.WindowTitle().endswith ('.xml') or self.Widget.WindowTitle().endswith ('.xhtml'):
            filename = self.Widget.WindowTitle()
            app.switch('barge')
            self.Env.RunApp('html', [filename])
            app.switch('barge')

    def new_page_act (self):
        self.Env.RunApp ('barge',None)
        app.switch('barge')

    def new_act (self):
        self.Widget.SetWindowTitle (res.get('@string/untitled'))
        self.teEdit.clear()

    def gettext (self,filename):
        self.teEdit.setPlainText(files.readall(filename))
        self.Widget.SetWindowTitle(files.output(filename))

        if self.Widget.WindowTitle()=='': self.Widget.SetWindowTitle (res.get('@string/untitled'))

    def saveas_ (self,filename):

        files.write(filename,self.teEdit.toPlainText())
        self.Widget.SetWindowTitle(files.output(filename))

        try:
            cmd.up([files.output(self.Widget.WindowTitle()).replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
        except:
            pass

    def save_ (self,filename):
        app.switch('barge')
        if not self.Widget.WindowTitle()==res.get('@string/untitled'):
            files.write(files.output(self.Widget.WindowTitle()),self.teEdit.toPlainText())

            try:
                cmd.up([files.output(self.Widget.WindowTitle()).replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
            except:
                pass

        else:
            app.switch('barge')
            self.Env.RunApp('select', [res.get('@string/saveafile'), 'save', self.saveas_])
            app.switch('barge')

    def open_act (self):
        app.switch('barge')
        self.Env.RunApp('select',[res.get('@string/chooseafile'),'open',self.gettext])
        app.switch('barge')

    def save_as (self):
        app.switch('barge')
        self.Env.RunApp('select', [res.get('@string/saveasfile'), 'save-as', self.saveas_])
        app.switch('barge')

    def langcode (self):
        code = f'@temp/{self.sender().objectName()}'
        connect = res.get(control.read_record('connect', res.get(code)))

        self.teEdit.setPlainText(files.readall(connect))