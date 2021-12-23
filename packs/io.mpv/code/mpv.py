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
    def open__(self,filename):
        if permissions.check(files.output(filename), "r", files.readall("/proc/info/su")):
            subprocess.call(['mpv',files.input(filename)])
        else:
            self.e = Perm()

    def open_(self):
        self.box = Select (self.open__)

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/mpv'))

        self.setProperty('title',res.get('@string/mpv'))
        app.launchedlogo(self.property('title'), res.etc('mpv', 'logo'))

        self.open = self.findChild ('open')
        self.image = self.findChild ('image')
        self.image.setProperty ('source',res.qmlget(res.etc('mpv','logo')))
        self.open.clicked.connect(self.open_)

        if not sys.argv[1:]==[]:
            self.open__(sys.argv[1])

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('mpv','logo'))))

w = MainApp()
application.exec()