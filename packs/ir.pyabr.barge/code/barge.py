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

class MainApp (MainApp):

    def update_(self,filename):
        self.setProperty ('title',files.filename(filename)+' - '+res.get('@string/barge.app_name'))
        self.path.setProperty ('text',filename)

    def open__(self,filename):
        self.text.setProperty ('text',files.readall(filename))
        self.update_(filename)

    def open_(self):
        self.box = Select (self.open__)

    def saveas__(self,filename):
        files.write (filename,self.text.property('text'))
        self.update_(filename)

    def saveas_(self):
        self.box = Save (self.saveas__)

    def save_(self):
        if self.path.property ('text')=='':
            self.box = Save (self.saveas__)
        else:
            files.write (self.path.property('text'),self.text.property('text'))

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/barge'))

        self.open = self.findChild ('open')
        self.redo = self.findChild ('redo')
        self.undo = self.findChild ('undo')
        self.save = self.findChild ('save')
        self.saveas = self.findChild ('saveas')
        self.save = self.findChild ('save')
        self.text = self.findChild ('text')
        self.path = self.findChild ('path')

        self.setProperty ('title',res.get('@string/barge.app_name'))

        self.open.clicked.connect(self.open_)
        self.saveas.clicked.connect(self.saveas_)
        self.save.clicked.connect (self.save_)


application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()