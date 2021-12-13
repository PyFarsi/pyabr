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
import sys
from pyabr.quick import *

class MainApp (MainApp):
    def update_(self,filename):
        self.setProperty ('title',files.filename(filename)+' - '+res.get('@string/nama'))
        self.fullscreen.setProperty ('visible',True)

    def open__(self,filename):
        if permissions.check(files.output(filename), "r", files.readall("/proc/info/su")):
            self.image.setProperty ('source',files.input_qml(filename))
            self.update_(filename)
        else:
            self.e = Perm()

    def open_(self):
        self.box = Select (self.open__)

    fulls = False

    def fullscreen_(self):
        if self.fulls:
            self.setProperty ('visibility','Windowed')  # https://stackoverflow.com/questions/9014298/full-screen-desktop-application-with-qml
            self.fulls = False
        elif self.fulls==False:
            self.setProperty ('visibility','FullScreen')
            self.fulls = True

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/nama'))

        self.open = self.findChild ('open')
        self.open.setProperty('text',res.get('@string/open'))
        self.image = self.findChild ('image')
        self.fullscreen = self.findChild ('fullscreen')
        self.setProperty ('title',res.get('@string/nama'))
        self.open.clicked.connect(self.open_)
        self.fullscreen.clicked.connect(self.fullscreen_)

        if not sys.argv[1:]==[]:
            self.open__(sys.argv[1])

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('nama','logo'))))

w = MainApp()
application.exec()