'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, PyPI
    * License:          GNU General Publice License v3.0

    - Official Website

    * Persian Page:     https://pyabr.ir
    * English Page:     https://en.pyabr.ir
'''

from pyabr.core import *
from pyabr.quick import *
import sys

class MainApp (MainApp):

    def update_(self,filename):
        self.setProperty ('title',files.filename(filename)+' - '+res.get('@string/barge'))
        self.path.setProperty ('text',filename)

        if filename.endswith ('.py') or filename.endswith ('.sa') or filename.endswith ('.pashm') or filename.endswith('.qml'):
            self.start.setProperty ('visible',True)

    def open__(self,filename):
        if permissions.check(files.output(filename), "r", files.readall("/proc/info/su")):
            self.text.setProperty ('text',files.readall(filename))
            self.update_(filename)
        else:
            self.e = Perm()

    def open_(self):
        self.box = Select (self.open__)

    def saveas__(self,filename):
        if permissions.check(files.output(filename), "w", files.readall("/proc/info/su")):
            files.write (filename,self.text.property('text'))
            self.update_(filename)
        else:
            self.e = Perm()

    def saveas_(self):
        self.box = Save (self.saveas__)

    def save_(self):
        if self.path.property ('text')=='':
            self.box = Save (self.saveas__)
        else:
            if permissions.check(files.output(self.path.property('text')), "w", files.readall("/proc/info/su")):
                files.write (self.path.property('text'),self.text.property('text'))
            else:
                self.e = Perm()
    
    def start_(self):
        if permissions.check(files.output(self.path.property('text')), "x", files.readall("/proc/info/su")):
            if self.path.property('text').endswith ('.py'):
                commands.cc ([self.path.property('text')])
                files.write ('/tmp/exec.sa',f"{self.path.property('text').replace('.py','')}\nrm /tmp/exec.sa\nrm {self.path.property('text')}c\nrm __pycache__\npause")
                app.start ('commento','')
            elif self.path.property('text').endswith ('.sa'):
                files.write ('/tmp/exec.sa',f"{self.path.property('text').replace('.sa','')}\nrm /tmp/exec.sa\npause")
                app.start ('commento','')
            elif self.path.property('text').endswith ('.pashm'):
                files.write ('/tmp/exec.sa',f"pashmak {self.path.property('text')}\nrm /tmp/exec.sa\npause")
                app.start ('commento','')
            elif self.path.property('text').endswith ('.qml'):
                files.copy (self.path.property('text'),'/usr/share/layouts/debug.qml')
                app.start ('debug','')
        else:
            self.e = Perm()

    def add_(self):
        self.text.setProperty('text','')
        self.setProperty('title',res.get('@string/barge'))
        self.path.setProperty('text','')
        self.start.setProperty('visible',False)

    def addwin_(self):
        app.start ('barge','')

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/barge'))

        self.open = self.findChild ('open')
        self.redoz = self.findChild ('redoz')
        self.undoz = self.findChild ('undoz')
        self.save = self.findChild ('save')
        self.saveas = self.findChild ('saveas')
        self.save = self.findChild ('save')
        self.text = self.findChild ('text')
        self.path = self.findChild ('path')
        self.start = self.findChild ('start')
        self.add = self.findChild ('add')
        self.addwin = self.findChild ('addwin')

        self.setProperty ('title',res.get('@string/barge'))

        self.open.clicked.connect(self.open_)
        self.saveas.clicked.connect(self.saveas_)
        self.save.clicked.connect (self.save_)
        self.start.clicked.connect (self.start_)
        self.add.clicked.connect (self.add_)
        self.addwin.clicked.connect (self.addwin_)

        if not sys.argv[1:]==[]:
            self.open__(sys.argv[1])

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('barge','logo'))))
w = MainApp()
application.exec()