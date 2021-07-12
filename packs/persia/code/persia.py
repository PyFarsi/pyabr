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

from PyQt5.QtGui import  *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtWidgets, QtCore, Qsci
import sys, importlib, random,py_compile,imp, baran
from libabr import System, App, Control, Files, Res, Commands

res = Res();files = Files();app = App();control=Control();commands = Commands()

f = QtGui.QFont()
f.setFamily('Fira Code')
f.setPointSize(12)
def getdata (name):
    return control.read_record (name,'/etc/gui')

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

        self.setFont(self.editor.Env.font())

    def mkdir(self, dirname):
        if files.isfile(dirname):
            self.editor.Env.RunApp('text', [res.get('@string/isfile'),res.get('@string/isfile_msg').replace('{0}',dirname)])
            app.switch('persia')
        else:
            it = QStandardItem(dirname)
            it.setWhatsThis(self.dir + "/" + dirname)
            it.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
            self.entry.appendRow(it)

            try:
                commands.mkc([str(self.dir+"/"+dirname).replace(f'/stor/{files.readall("/proc/info/mnt")}/', '')])
            except:
                commands.mkdir([dirname])

    def mkfile (self,filename):
        if files.isdir(filename + ".c"):
            self.editor.Env.RunApp('text', [res.get('@string/isdir'),res.get('@string/isdir_msg').replace('{0}',filename)])
            app.switch('persia')
        else:
            it = QtGui.QStandardItem(filename)
            it.setWhatsThis(self.dir + "/" + filename)
            it.setIcon(QtGui.QIcon(res.get(res.etc('roller','file-icon'))))
            self.entry.appendRow(it)
            self.format(it, filename)
            commands.cat (['-c',filename])
            it.setFont(self.editor.Env.font())


    def genpa (self,filename):
        it = QtGui.QStandardItem(filename+".pa")
        it.setWhatsThis(self.dir + "/" + filename+".pa")
        self.entry.appendRow(it)
        self.format(it, filename+".pa")
        it.setFont(self.editor.Env.font())

    def mkcode (self,filename):
        self.code = files.readall('/tmp/code.tmp')
        self.ext = control.read_record('ext', res.get(self.code))

        if files.isdir(filename + f".{self.ext}"):
            self.editor.Env.RunApp('text', [res.get('@string/isdir'),res.get('@string/isdir_msg').replace('{0}',filename+f".{self.ext}")])
            app.switch('persia')
        else:
            self.mkfile(filename+f".{self.ext}")
            files.write(self.dir + "/" + filename+f'.{self.ext}',files.readall(res.get(control.read_record('connect',res.get(self.code)))))

    def __init__(self,editor):
        super().__init__()
        self.editor = editor
        self.entry = QStandardItemModel()
        self.parentdir = QStandardItem()
        self.parentdir.setIcon(QIcon(res.get(res.etc('roller','folder-icon'))))
        self.entry.appendRow(self.parentdir)
        self.setModel(self.entry)
        self.setIconSize(QSize(64, 64))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()
        # on the given model index to get a pointer to the item

        self.username = self.editor.Env.username

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
            if files.isdir(self.dir+"/"+text):
                it = QStandardItem(text)
                it.setWhatsThis(self.dir + "/" + text)
                self.format(it, text)
                self.entry.appendRow(it)

        for text in self.listdir:
            if files.isfile(self.dir+"/"+text):
                it = QStandardItem(text)
                it.setWhatsThis(self.dir + "/" + text)
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
                        self.format(it, text)
                        self.entry.appendRow(it)

                for text in self.listdir:
                    if files.isfile(self.dir+"/"+text):
                        it = QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
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
                        self.format(it, text)
                        self.entry.appendRow(it)

                for text in self.listdir:
                    if files.isfile(self.dir+"/"+text):
                        it = QStandardItem(text)
                        it.setWhatsThis(self.dir + "/" + text)
                        self.format(it, text)
                        self.entry.appendRow(it)

            elif files.isfile(self.item.whatsThis()):
                files.write('/proc/info/fsel', self.item.whatsThis())  # Send File selected

                self.lang = self.item.whatsThis().lower()

                if self.lang.endswith('.py'):
                    lexer = Qsci.QsciLexerPython()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.diff'):
                    lexer = Qsci.QsciLexerDiff()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.f') or self.lang.endswith('.for') or self.lang.endswith('.f90'):
                    lexer = Qsci.QsciLexerFortran()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.d'):
                    lexer = Qsci.QsciLexerD()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.bat'):
                    lexer = Qsci.QsciLexerBatch()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.sh'):
                    lexer = Qsci.QsciLexerBash()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.js'):
                    lexer = Qsci.QsciLexerJavaScript()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.java'):
                    lexer = Qsci.QsciLexerJava()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.cs'):
                    lexer = Qsci.QsciLexerCSharp()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.xml') or self.lang.endswith('.dtd'):
                    lexer = Qsci.QsciLexerXML()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.c') or self.lang.endswith('.cpp') or self.lang.endswith('.hpp') or self.lang.endswith('.h') or self.lang.endswith('.c++') or self.lang.endswith('.cxx') or self.lang.endswith('.C') or self.lang.endswith('.hxx') or self.lang.endswith('.h++'):
                    lexer = Qsci.QsciLexerCPP()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang=='makefile':
                    lexer = Qsci.QsciLexerMakefile()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.html') or self.lang.endswith('.htm') or self.lang.endswith('.asp') or self.lang.endswith('.aspx') or self.lang.endswith('.php'):
                    lexer = Qsci.QsciLexerHTML()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.css'):
                    lexer = Qsci.QsciLexerCSS()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.rb'):
                    lexer = Qsci.QsciLexerRuby()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.json'):
                    lexer = Qsci.QsciLexerJSON()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.avs'):
                    lexer = Qsci.QsciLexerAVS()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.lua'):
                    lexer = Qsci.QsciLexerLua()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.m') or self.lang.endswith('.p') or self.lang.__contains__('.mex') or self.lang.endswith('.mat'):
                    lexer = Qsci.QsciLexerMatlab()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.pas'):
                    lexer = Qsci.QsciLexerPascal()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.perl'):
                    lexer = Qsci.QsciLexerPerl()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.sql'):
                    lexer = Qsci.QsciLexerSQL()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.properties'):
                    lexer = Qsci.QsciLexerProperties()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.ps'):
                    lexer = Qsci.QsciLexerPostScript()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.tcl'):
                    lexer = Qsci.QsciLexerTCL()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.md'):
                    lexer = Qsci.QsciLexerMarkdown()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                elif self.lang.endswith('.yaml'):
                    lexer = Qsci.QsciLexerYAML()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)
                else:
                    lexer = Qsci.QsciLexerPython()
                    lexer.setDefaultFont(font)
                    self.editor.teEdit.setLexer(lexer)

                self.editor.teEdit.setText(files.readall(self.item.whatsThis()))

import sip
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython

font = QFont()
font.setFamily('Fira Code')
font.setFixedPitch(True)
font.setPointSize(16)

class SimplePythonEditor(baran.BCodeEdit):
    ARROW_MARKER_NUM = 8

    def __init__(self,ports):
        super(SimplePythonEditor, self).__init__()

        self.Env = ports[1]

        # Set the default font
        font = QFont()
        font.setFamily('Fira Code')
        font.setFixedPitch(True)
        font.setPointSize(16)
        self.setFont(font)
        self.setMarginsFont(font)

        # Margin 0 is used for line numbers
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))

        # Clickable margin 1 for showing markers
        self.setMarginSensitivity(1, True)
        self.marginClicked.connect(self.on_margin_clicked)
        self.markerDefine(QsciScintilla.RightArrow,
            self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ee1111"),
            self.ARROW_MARKER_NUM)

        # Brace matching: enable for a brace immediately before or after
        # the current position
        #
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Current line visible with special background color
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#ffe4e4")) # ffe4e4

        # Set Python lexer
        # Set style for Python comments (style number 1) to a fixed-width
        # courier.
        #

        lexer = QsciLexerPython()

        lexer.setDefaultFont(font)
        self.setLexer(lexer)

        text = bytearray(str.encode("Arial"))
# 32, "Courier New"
        self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, text)

        # Don't want to see the horizontal scrollbar at all
        # Use raw message to Scintilla here (all messages are documented
        # here: http://www.scintilla.org/ScintillaDoc.html)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        # not too small
        self.setMinimumSize(600, 450)

    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)

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

        self.onCloseProcess()

        self.project_folder = 'Projects'

        # resize
        self.Widget.Resize (self,self.Env.width(),self.Env.height())
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QtGui.QIcon(res.get(res.etc(self.AppName,'logo'))))


        # text box
        self.teEdit = SimplePythonEditor(args)
        # Set the default font

        self.teEdit.setStyleSheet("""

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
            '#ABCDEF', getdata("menu.scroll.color-hover")))

        #self.teEdit.setLexer(Qsci.QsciLexerPython())

        ## External Support : Open with persia ##

        if self.External==None:
            self.Widget.SetWindowTitle(res.get('@string/untitled'))
        else:
            if self.External==[]:
                self.Widget.SetWindowTitle(res.get('@string/untitled'))
            else:
                if self.External[1]==None:
                    pass
                else:
                    self.Widget.SetWindowTitle(self.External[1])
                    self.teEdit.setText(files.readall(self.External[1]))

        self.teEdit.setGeometry(int(self.Env.width()/5),40,self.Env.width()-int(self.Env.width()/5),self.Env.height())
        self.layout().addWidget(self.teEdit)

        self.xfile = QMainWindow()
        self.x = FileListView(self)
        self.xfile.setCentralWidget(self.x)
        self.xfile.setGeometry(0,25,int(self.Env.width()/5),self.Env.height())
        self.layout().addWidget(self.xfile)

        # menubar
        self.menubar = self.menuBar()
        self.menubar.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)
        self.menubar.setFont(self.Env.font())
        self.file = self.menubar.addMenu(res.get('@string/file'))
        self.file.setStyleSheet('background:none;color: black;')
        self.file.setFont(self.Env.font())

        # file menu #
        self.new_code = self.file.addMenu(res.get('@string/new'))
        self.new_code.setFont(self.Env.font())
        self.new_code.setStyleSheet('background:none;color: black;')
        self.new_code.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'text'))))

        ## new file

        self.new_file = self.new_code.addAction(res.get('@string/newfile'))
        self.new_file.setFont(self.Env.font())
        self.new_file.triggered.connect(self.New_File)
        self.new_file.setIcon(QIcon(res.get('@icon/breeze-txt')))

        self.new_fldr = self.new_code.addAction(res.get('@string/newfolder'))
        self.new_fldr.triggered.connect(self.New_Folder)
        self.new_fldr.setIcon(QIcon(res.get('@icon/breeze-folder')))
        self.new_fldr.setFont(self.Env.font())

        self.templist = files.list('/usr/share/templates')
        self.templist.sort()
        for i in self.templist:
            if i.endswith('.desk'):
                self.new_cz = self.new_code.addAction(
                    control.read_record(f'name[{control.read_record("locale", "/etc/gui")}]', res.get(f'@temp/{i}')))
                self.new_cz.setFont(self.Env.font())
                self.new_cz.setObjectName(i)
                self.new_cz.triggered.connect(self.New_Code)
                self.new_cz.setIcon(QIcon(res.get(control.read_record('logo', res.get(f'@temp/{i}')))))
        ##

        self.new_project = self.file.addMenu(res.get('@string/new_page'))
        self.new_project.setStyleSheet('background:none;color: black;')
        self.new_project.setFont(self.Env.font())
        self.new_project.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName, 'py'))))

        self.new_page = self.new_project.addAction(res.get('@string/empty'))
        self.new_page.triggered.connect(self.new_empty_act)
        self.new_page.setFont(self.Env.font())
        self.new_page.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName, 'py'))))

        self.new_gui = self.new_project.addAction(res.get('@string/gui'))
        self.new_gui.triggered.connect(self.new_gui_act)
        self.new_gui.setFont(self.Env.font())
        self.new_gui.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName, 'py'))))

        self.new_web = self.new_project.addAction(res.get('@string/web'))
        self.new_web.triggered.connect(self.new_web_act)
        self.new_web.setFont(self.Env.font())
        self.new_web.setIcon(QtGui.QIcon(res.get('@icon/breeze-browser')))

        self.open = self.file.addAction(res.get('@string/open'))
        self.open.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'open'))))
        self.open.setFont(self.Env.font())
        self.open.setShortcut('Ctrl+O')
        self.open.triggered.connect (self.open_act)
        self.save = self.file.addAction(res.get('@string/save'))
        self.save.setShortcut('Ctrl+S')
        self.save.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'save'))))
        self.save.triggered.connect (self.save_)
        self.save.setFont(self.Env.font())
        self.saveas = self.file.addAction(res.get('@string/save_as'))
        self.saveas.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'save-as'))))
        self.saveas.setFont(self.Env.font())
        self.saveas.triggered.connect (self.save_as)
        self.exit = self.file.addAction(res.get('@string/exit'))
        self.exit.setIcon(QtGui.QIcon(res.get(res.etc(self.AppName,'exit'))))
        self.exit.triggered.connect (self.Widget.Close)
        self.exit.setFont(self.Env.font())
        self.exit.setShortcut('Ctrl+X')

        # code menu
        self.code = self.menubar.addMenu(res.get('@string/code'))
        self.code.setStyleSheet('background:none;color: black;')
        self.code.setFont(self.Env.font())
        self.run = self.code.addAction(res.get('@string/run'))
        self.run.triggered.connect (self.run_)

        self.run = self.code.addAction(res.get('@string/runp'))
        self.run.triggered.connect (self.run_project_)
        self.run.setShortcut('Shift+F10')

        self.build = self.code.addMenu(res.get('@string/build'))
        self.build.setStyleSheet('background:none;color: black;')
        self.build.setFont(self.Env.font())

        self.generate_source = self.build.addAction(res.get('@string/pack'))
        self.generate_pa = self.build.addAction(res.get('@string/pa'))
        self.generate_pa.setFont(self.Env.font())
        self.generate_pa.triggered.connect (self.generate_pa_)
        self.install = self.build.addAction(res.get('@string/buildi'))
        self.install.triggered.connect (self.install_)
        self.install.setFont(self.Env.font())

        self.publish = self.code.addAction(res.get('@string/publish'))
        self.publish.setFont(self.Env.font())

        self.insert_c = self.code.addMenu(res.get('@string/insert'))
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
                self.new_czx.setIcon(QIcon(res.get(control.read_record('logo', res.get(f'@temp/{i}')))))

        # set font size
        self.teEdit.setFont(f)

    def run_(self):
        control = Control()
        file = files.readall('/proc/info/fsel')

        ## Run it ##
        if file.endswith (".c") or file.endswith('.cpp') or file.endswith('.cxx') or file.endswith('.c++'):
            filename = file
            execname = file.replace('.cpp', '').replace('.cxx', '').replace('.c++', '').replace(
                '.c', '')
            files.write('/tmp/exec.sa', f'''
say Compiling {filename} ...
cc {filename}
echo done
echo Running {execname} ...
echo
{execname}
echo
echo Finish running process with exit 0 ...
rm /tmp/exec.sa
pause
                        ''')
            self.Env.RunApp('commento', [None])
            app.switch('persia')
            files.remove(execname+".out")

        elif file.endswith ('.py'):
            # check graphical PyQt5 #
            if files.readall(file).__contains__('from PyQt5') and files.readall(file).__contains__('MainApp'):
                rand = str (random.randint(1000,9999))
                files.create(f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('name[en]','Debug App',f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('name[fa]','برنامه تستی',f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('logo','@icon/breeze-app',f'/usr/share/applications/debug_{rand}.desk')
                control.write_record('exec',f"debug_{rand}",f'/usr/share/applications/debug_{rand}.desk')
                app.switch('persia')
                py_compile.compile(files.input(file),files.input(f'/usr/app/debug_{rand}.pyc'))
                self.Env.RunApp(f'debug_{rand}',[None])
                app.switch('persia')
                files.remove(f'/usr/share/applications/debug_{rand}.desk')
                files.remove(f'/usr/app/debug_{rand}.pyc')
            else:
                execname = file.replace('.py', '')
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
                app.switch('persia')

        elif file.endswith ('.sa'):
            execname = file.replace('.sa', '')
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
            app.switch('persia')
        elif file.endswith('.pashm'):
            files.write('/tmp/exec.sa', f'''
echo Running {file} ...
echo
pashmak {file}
echo
echo Finish running process with exit 0 ...
rm /tmp/exec.sa
pause
                                                ''')
            self.Env.RunApp('commento', [None])
            app.switch('persia')
        elif file.endswith('.ui'):
            app.switch('persia')
            self.Env.RunApp('uiv', [file])
            app.switch('persia')
        elif file.endswith ('.html') or file.endswith('.htm') or file.endswith('.xml') or file.endswith('.xhtml'):
            app.switch('persia')
            self.Env.RunApp('html', [file])
            app.switch('persia')
        else:
            app.switch('persia')
            self.Env.RunApp('text', [res.get('@string/spc'), res.get('@string/spcm')])
            app.switch('persia')


    def run_project_(self):

        # config files #
        project = files.readall('/proc/info/psel')
        user = files.readall('/proc/info/su')
        if not user=='root':
            path = f'/desk/{user}/{self.project_folder}/{project}'
        else:
            path = f'/root/{self.project_folder}/{project}'

        config = path+"/config"

        rand = str(random.randint(1000,9999))

        compile = files.readall(f'{path}/{project}/control/compile')
        compile = compile.replace(f'{project}.pyc', f'{project}_{rand}.pyc')
        files.write(f'{path}/{project}/control/compile', compile)

        if control.read_record('project_type',config)=='gui' or control.read_record('project_type',config)=='web':
            control.write_record('exec', f'{project}_{rand}',f'{path}/{project}/data/usr/share/applications/{project}.desk')
            files.cut(f'{path}/{project}/data/usr/share/applications/{project}.desk',
                      f'{path}/{project}/data/usr/share/applications/{project}_{rand}.desk')

            System(f'paye pak {path}/{project}')
            System(f'paye upak {path}/{project}.pa')
            app.switch('persia')
            self.Env.RunApp(f'{project}_{rand}', [None])
            app.switch('persia')

            files.cut(f'{path}/{project}/data/usr/share/applications/{project}_{rand}.desk',
                      f'{path}/{project}/data/usr/share/applications/{project}.desk')
        else:
            System(f'paye pak {path}/{project}')
            System(f'paye upak {path}/{project}.pa')
            app.switch('persia')
            filename = self.Widget.WindowTitle()
            execname = filename.replace('.py', '')
            files.write('/tmp/exec.sa', f'''
{project}_{rand}
rm /tmp/exec.sa
pause
                                        ''')
            self.Env.RunApp('commento', [None])
            app.switch('persia')

        if files.isfile(f'{path}/{project}.pa'): files.remove(f'{path}/{project}.pa')
        System(f'paye rm {project}')

        compile = files.readall(f'{path}/{project}/control/compile')
        compile = compile.replace(f'{project}_{rand}.pyc', f'{project}.pyc')
        files.write(f'{path}/{project}/control/compile', compile)

    def new_empty_act (self):
        app.switch('persia')
        self.Env.RunApp('input', [res.get('@string/proname'), self.project_create])
        app.switch('persia')

    def new_gui_act (self):
        app.switch('persia')
        self.Env.RunApp('input', [res.get('@string/proname'), self.project_create_gui])
        app.switch('persia')

    def new_web_act (self):
        app.switch('persia')
        self.Env.RunApp('input', [res.get('@string/proname'), self.project_create_web])
        app.switch('persia')

    def project_create (self,projectname):
        su = files.readall('/proc/info/su')

        if not su=='root':
            System (f"paye crt /desk/{su}/{self.project_folder}/{projectname}")
            commands.cd([f'/desk/{su}/{self.project_folder}/{projectname}'])
        else:
            System(f"paye crt /root/{self.project_folder}/{projectname}")
            commands.cd([f'/root/{self.project_folder}/{projectname}'])

        commands.mv(['app', f'{projectname}'])
        commands.mv([f'{projectname}/code/hello.py', f'{projectname}/code/{projectname}.py'])
        files.write(f'{projectname}/control/manifest', f'name: {projectname}\ncopyright: (c) 2020 Your name\nlicense: Your license\nunpack: /\nbuild: year-month-day\nversion: 0.0.1\ndescription: Your application description\ncompile: Yes')

        files.write(f'{projectname}/control/compile', f'{projectname}.py:usr/app/{projectname}.pyc')
        files.write(f'{projectname}/control/list', f'/usr/app/{projectname}.pyc')

        files.write('/proc/info/psel', projectname)
        files.create("config")

        control.write_record('project_name', projectname, "config")
        control.write_record('project_type', 'empty', "config")
        control.write_record('project_lang', 'python', 'config')
        control.write_record('project_pack', projectname + '.pa', 'config')
        control.write_record('project_dir', projectname,'config')
        app.switch('persia')
        self.Env.RunApp ('persia',[projectname,None])
        app.switch('persia')

    def project_create_gui (self,projectname):
        su = self.Env.username

        if not su=='root':
            System (f"paye crt gui /desk/{su}/{self.project_folder}/{projectname}")
            commands.cd([f'/desk/{su}/{self.project_folder}/{projectname}'])
        else:
            System(f"paye crt gui /root/{self.project_folder}/{projectname}")
            commands.cd([f'/root/{self.project_folder}/{projectname}'])

        commands.mv(['app',f'{projectname}'])
        commands.mv([f'{projectname}/code/hello.py',f'{projectname}/code/{projectname}.py'])
        commands.mv([f'{projectname}/data/usr/share/applications/hello.desk',f'{projectname}/data/usr/share/applications/{projectname}.desk'])
        files.write (f'{projectname}/control/manifest',f'name: {projectname}\ncopyright: (c) 2020 Your name\nlicense: Your license\nunpack: /\nbuild: year-month-day\nversion: 0.0.1\ndescription: Your application description\ncompile: Yes')
        files.write(f'{projectname}/control/compile', f'{projectname}.py:usr/app/{projectname}.pyc')
        files.write(f'{projectname}/control/list',f'/usr/app/{projectname}.pyc\n/usr/share/application/{projectname}.desk')
        files.write(f'{projectname}/data/usr/share/applications/{projectname}.desk',f'name[en]: {projectname}\nlogo: @icon/breeze-app\nexec: {projectname}')

        files.write('/proc/info/psel', projectname)
        files.create("config")

        control.write_record('project_name', projectname, "config")
        control.write_record('project_type', 'gui', "config")
        control.write_record('project_lang','python','config')
        control.write_record('project_pack', projectname + '.pa', 'config')
        control.write_record('project_dir', projectname,'config')
        app.switch('persia')
        self.Env.RunApp ('persia',[projectname,None])
        app.switch('persia')

    def project_create_web (self,projectname):
        su = self.Env.username

        if not su=='root':
            System (f"paye crt web /desk/{su}/{self.project_folder}/{projectname}")
            commands.cd([f'/desk/{su}/{self.project_folder}/{projectname}'])
        else:
            System(f"paye crt web /root/{self.project_folder}/{projectname}")
            commands.cd([f'/root/{self.project_folder}/{projectname}'])

        commands.mv(['app',f'{projectname}'])
        commands.mv([f'{projectname}/code/hello.py',f'{projectname}/code/{projectname}.py'])
        commands.mv([f'{projectname}/data/usr/share/applications/hello.desk',f'{projectname}/data/usr/share/applications/{projectname}.desk'])
        files.write (f'{projectname}/control/manifest',f'name: {projectname}\ncopyright: (c) 2020 Your name\nlicense: Your license\nunpack: /\nbuild: year-month-day\nversion: 0.0.1\ndescription: Your application description\ncompile: Yes')
        files.write(f'{projectname}/control/compile', f'{projectname}.py:usr/app/{projectname}.pyc')
        files.write(f'{projectname}/control/list',f'/usr/app/{projectname}.pyc\n/usr/share/application/{projectname}.desk')
        files.write(f'{projectname}/data/usr/share/applications/{projectname}.desk',f'name[en]: {projectname}\nlogo: @icon/breeze-browser\nexec: {projectname}')

        files.write('/proc/info/psel', projectname)
        files.create("config")

        control.write_record('project_name', projectname, "config")
        control.write_record('project_type', 'web', "config")
        control.write_record('project_lang','python','config')
        control.write_record('project_pack',projectname+'.pa','config')
        control.write_record('project_dir',projectname,'config')
        app.switch('persia')
        self.Env.RunApp ('persia',[projectname,None])
        app.switch('persia')

    def generate_pa_ (self):
        self.project = files.readall('/proc/info/psel')
        self.user = files.readall('/proc/info/su')

        if not self.user == 'root':
            self.path = f'/desk/{self.user}/{self.project_folder}/{self.project}'
        else:
            self.path = f'/root/{self.project_folder}/{self.project}'

        self.config = self.path + "/config"

        self.projectname = control.read_record('project_name',self.config)

        System(f'paye pak {self.path}/{self.projectname}')
        commands.mv([f'{self.path}/{self.projectname}.pa',f'{self.path}/{self.projectname}.pa'])

        self.x.genpa(self.projectname)

    def install_(self):
        if not files.isfile(f"{self.path}/{self.projectname}.pa"):
            self.generate_pa_()

        if not files.isdir(f"{self.path}/{self.projectname}.pa"):
            System(f'paye upak {self.path}/{self.projectname}.pa')

    def new_act (self):
        self.Widget.SetWindowTitle (res.get('@string/untitled'))
        self.teEdit.clear()

    def gettext (self,filename):
        self.teEdit.setText(files.readall(filename))
        self.Widget.SetWindowTitle(files.output(filename).replace('//',''))

        if self.Widget.WindowTitle()=='': self.Widget.SetWindowTitle (res.get('@string/untitled'))

    def saveas_ (self,filename):
        files.write(filename,self.teEdit.text())
        files.write('/proc/info/fsel',filename)

    def save_ (self,filename):
        if not self.Widget.WindowTitle()==res.get('@string/untitled'):
            files.write(files.readall('/proc/info/fsel'),self.teEdit.text())
        else:
            app.switch('persia')
            self.Env.RunApp('select', [res.get('@string/saveafile'), 'save', self.saveas_])
            app.switch('persia')

    def open_act (self):
        app.switch('persia')
        self.Env.RunApp('select',[res.get('@string/chooseafile'),'open',self.gettext])
        app.switch('persia')

    def save_as (self):
        app.switch('persia')
        self.Env.RunApp('select', [res.get('@string/saveasfile'), 'save-as', self.saveas_])
        app.switch('persia')


    def langcode (self):
        code = '@temp/' + self.sender().objectName()
        ext = control.read_record('ext',res.get(code))
        connect  = res.get(control.read_record('connect',res.get(code)))
        self.teEdit.setText(files.readall(connect))

        if ext=='cpp' or ext=='c++' or ext=='cxx' or ext=='c':
            lexer = Qsci.QsciLexerCPP()
            lexer.setDefaultFont(font)
            self.teEdit.setLexer(lexer)
        elif ext=='py' or ext=='pashm' or ext=='sa':
            lexer = Qsci.QsciLexerPython()
            lexer.setDefaultFont(font)
            self.teEdit.setLexer(lexer)
        elif ext=='java':
            lexer = Qsci.QsciLexerJava()
            lexer.setDefaultFont(font)
            self.teEdit.setLexer(lexer)
        elif ext=='php' or ext=='html':
            lexer = Qsci.QsciLexerHTML()
            lexer.setDefaultFont(font)
            self.teEdit.setLexer(lexer)
        elif ext=='css':
            lexer = Qsci.QsciLexerCSS()
            lexer.setDefaultFont(font)
            self.teEdit.setLexer(lexer)
        elif ext=='cs':
            lexer = Qsci.QsciLexerCSharp()
            lexer.setDefaultFont(font)
            self.teEdit.setLexer(lexer)
        elif ext=='js':
            lexer = Qsci.QsciLexerJavaScript()
            lexer.setDefaultFont(font)
            self.teEdit.setLexer(lexer)
        else:
            lexer = Qsci.QsciLexerPython()
            lexer.setDefaultFont(font)
            self.teEdit.setLexer(lexer)

    def New_Folder (self):
        app.switch('persia')
        self.Env.RunApp('input',[res.get('@string/foldername'),self.x.mkdir])
        app.switch('persia')

    def New_File (self):
        app.switch('persia')
        self.Env.RunApp('input',[res.get('@string/filename'),self.x.mkfile])
        app.switch('persia')

    def New_Code (self):
        files.write('/tmp/code.tmp','@temp/'+self.sender().objectName())
        app.switch('roller')
        self.Env.RunApp('input', [res.get('@string/filename'), self.x.mkcode])
        app.switch('roller')