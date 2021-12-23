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
    def add_(self):
        self.x = Download ()

    def loop(self):
        if self.username=='root':
            self.addFileModel('/root/Downloads')
        else:
            self.addFileModel(f'/desk/{self.username}/Downloads')

        QTimer.singleShot(1000,self.loop)
        
    def __init__(self):
        super(MainApp, self).__init__()
        self.username = files.readall('/proc/info/su')

        if self.username=='root':
            self.addFileModel('/root/Downloads')
        else:
            self.addFileModel(f'/desk/{self.username}/Downloads')
        
        self.load (res.get('@layout/dmgr'))
        self.setProperty('title',res.get('@string/download'))
        app.launchedlogo(self.property('title'), res.etc('dmgr', 'logo'))
        self.add = self.findChild('add')
        self.add.clicked.connect (self.add_)

        self.loop()

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('dmgr','logo'))))

w = MainApp()
application.exec()