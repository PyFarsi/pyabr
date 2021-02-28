#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

from PyQt5 import QtWidgets, uic, QtGui,QtCore
import sys, importlib, random,py_compile
from libabr import System, App, Control, Files, Res, Commands

res = Res();files = Files();app = App();control=Control();cmd = Commands()

class MainApp(QtWidgets.QMainWindow):
    def __init__(self,args):
        super(MainApp, self).__init__()

        # ports
        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        # resize
        self.Widget.Resize (self,700,500)
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QtGui.QIcon(res.get(res.etc(self.AppName,'logo'))))

        self.Widget.SetWindowTitle(res.get('@string/untitled'))

        # text box
        self.teEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.teEdit)

        # menubar
        self.menubar = self.menuBar()
        self.file = self.menubar.addMenu(res.get('@string/file'))
        self.file.setFont(self.Env.font())

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
        self.open.setFont(self.Env.font())
        self.open.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'open'))))
        self.open.triggered.connect (self.open_act)
        self.save = self.file.addAction(res.get('@string/save'))
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

        # code menu
        self.code = self.menubar.addMenu(res.get('@string/code'))
        self.code.setFont(self.Env.font())
        self.run = self.code.addAction(res.get('@string/run'))
        self.run.setFont(self.Env.font())
        self.run.triggered.connect (self.run_)

        self.insert_c = self.code.addMenu(res.get('@string/icode'))
        self.insert_c.setFont(self.Env.font())

        # Codes #
        self.lang_c = self.insert_c.addAction(res.get('@string/c'))
        self.lang_c.setFont(self.Env.font())
        self.lang_c.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'c'))))
        self.lang_c.triggered.connect (self.langc)
        self.lang_cpp = self.insert_c.addAction(res.get('@string/c++'))
        self.lang_cpp.setFont(self.Env.font())
        self.lang_cpp.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'c++'))))
        self.lang_cpp.triggered.connect(self.langcpp)
        self.lang_cs = self.insert_c.addAction(res.get('@string/csharp'))
        self.lang_cs.setFont(self.Env.font())
        self.lang_cs.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'c#'))))
        self.lang_cs.triggered.connect(self.langcs)
        self.lang_java = self.insert_c.addAction(res.get('@string/java'))
        self.lang_java.setFont(self.Env.font())
        self.lang_java.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'java'))))
        self.lang_java.triggered.connect(self.langjava)
        self.lang_python = self.insert_c.addAction(res.get('@string/python'))
        self.lang_python.setFont(self.Env.font())
        self.lang_python.triggered.connect(self.langpython)
        self.lang_python.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'py'))))
        self.lang_pythongui = self.insert_c.addAction(res.get('@string/pythongui'))
        self.lang_pythongui.setFont(self.Env.font())
        self.lang_pythongui.triggered.connect(self.langpythonx)
        self.lang_pythongui.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'py'))))
        self.lang_pythonweb = self.insert_c.addAction(res.get('@string/pyweb'))
        self.lang_pythonweb.setFont(self.Env.font())
        self.lang_pythonweb.triggered.connect(self.langpythonweb)
        self.lang_pythonweb.setIcon(QtGui.QIcon(res.get('@icon/web-browser')))
        self.lang_saye = self.insert_c.addAction(res.get('@string/saye'))
        self.lang_saye.setFont(self.Env.font())
        self.lang_saye.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'sa'))))
        self.lang_saye.triggered.connect(self.langsaye)
        self.lang_html = self.insert_c.addAction(res.get('@string/html'))
        self.lang_html.setFont(self.Env.font())
        self.lang_html.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'html'))))
        self.lang_html.triggered.connect(self.langhtml)
        self.lang_php = self.insert_c.addAction(res.get('@string/php'))
        self.lang_php.setFont(self.Env.font())
        self.lang_php.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'php'))))
        self.lang_php.triggered.connect(self.langphp)
        self.lang_js = self.insert_c.addAction(res.get('@string/javascript'))
        self.lang_js.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'js'))))
        self.lang_js.setFont(self.Env.font())
        self.lang_js.triggered.connect(self.langjs)


        # set font size
        f = QtGui.QFont()
        f.setFamily('DejaVu Sans Mono')
        f.setPointSize(12)
        self.teEdit.setFont(f)

    def run_(self):
        control = Control()
        if not self.Widget.WindowTitle()==res.get('@string/untitled'):
            self.save_('')
        else:
            self.save_as()

        ## Run it ##
        if self.Widget.WindowTitle().endswith (".c") or self.Widget.WindowTitle().endswith('.cpp') or self.Widget.WindowTitle().endswith('.cxx') or self.Widget.WindowTitle().endswith('.c++'):
            filename = self.Widget.WindowTitle()
            execname = self.Widget.WindowTitle().replace('.cpp','').replace('.cxx','').replace('.c++','').replace('.c','')
            files.write('/tmp/exec.sa',f'''
say Compiling {filename} ...
cc {filename}
echo done
echo Running {execname} ...
echo
{execname}
echo
echo Finish runing process with exit 0 ...
rm /tmp/exec.sa
rm {execname}
pause
            ''')
            self.Env.RunApp('commento',[None])
            app.switch('barge')
            files.remove(execname)

        elif self.Widget.WindowTitle().endswith ('.py'):
            # check graphical PyQt5 #
            if files.readall(self.Widget.WindowTitle()).__contains__('from PyQt5') and files.readall(self.Widget.WindowTitle()).__contains__('MainApp'):
                rand = str (random.randint(1000,9999))
                files.create(f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('name[en]','Debug App',f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('name[fa]','برنامه تستی',f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('logo','@icon/app',f'/usr/share/applications/debug_{rand}.desk')
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
echo Finish runing process with exit 0 ...
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
echo Finish runing process with exit 0 ...
rm /tmp/exec.sa
pause
                                        ''')
            self.Env.RunApp('commento', [None])
            app.switch('barge')
        else:
            if not self.Widget.WindowTitle()==res.get('@string/untitled'):
                app.switch('barge')
                self.Env.RunApp('text', [res.get('@string/cs'), res.get('@string/csm')])
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

    def save_ (self,filename):
        if not self.Widget.WindowTitle()==res.get('@string/untitled'):
            files.write(files.output(self.Widget.WindowTitle()),self.teEdit.toPlainText())
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

    def langc (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.c')))

    def langcpp (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.cpp')))

    def langjava (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.java')))

    def langpython (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.py')))

    def langpythonx (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled-gui.py')))

    def langpythonweb (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled-web.py')))

    def langcs (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.cs')))

    def langsaye (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.sa')))

    def langhtml (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.html')))

    def langphp (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.php')))

    def langjs (self):
        self.teEdit.setPlainText(files.readall(res.get('@temp/untitled.js')))