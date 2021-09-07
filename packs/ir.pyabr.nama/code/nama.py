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
    index = 0
    max = 0
    def update_(self,filename):
        self.setProperty ('title',files.filename(filename)+' - '+res.get('@string/nama.app_name'))

    def open__(self,filename):
        self.image.setProperty ('source',files.input_qml(filename))
        self.update_(filename)

    def open_(self):
        self.box = Select (self.open__)

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/nama'))

        self.open = self.findChild ('open')
        self.image = self.findChild ('image')
        self.setProperty ('title',res.get('@string/nama.app_name'))
        self.open.clicked.connect(self.open_)

application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()