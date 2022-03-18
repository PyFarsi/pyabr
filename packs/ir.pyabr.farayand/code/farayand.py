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
import subprocess

class MainApp (MainApp):
    def kill_(self):
        print(self.psel.property('text'))
        if 'Pyabr' in self.psel.property('text'):
            app.signal('shutdown')
        else:
            subprocess.call(['wmctrl','-c',self.psel.property('text')])

    def loop(self):
        self.addProcessModel()
        QTimer.singleShot(200,self.loop)

    def __init__(self):
        super(MainApp, self).__init__()
        self.addProcessModel()
        self.load (res.get('@layout/farayand'))
        self.setProperty('title',res.getname('farayand'))
        app.launchedlogo(self.property('title'), res.etc('farayand', 'logo'))
        self.kill = self.findChild('kill')
        self.psel = self.findChild('psel')
        self.kill.clicked.connect (self.kill_)

        self.loop()

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('farayand','logo'))))

w = MainApp()
application.exec()