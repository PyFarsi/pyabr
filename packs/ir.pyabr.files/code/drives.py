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
    def loop(self):
        if not self.dsel.property('text')=='':
            if not files.isdir (f"/media/{self.dsel.property('text').replace('/dev/','')}"): files.mkdir (f"/media/{self.dsel.property('text').replace('/dev/','')}")

            try:
                subprocess.call(['mount',self.dsel.property('text'),f"/stor/media/{self.dsel.property('text').replace('/dev/','')}"])
                app.start ('files',f"/media/{self.dsel.property('text').replace('/dev/','')}")
            except:
                self.e = Text (res.get('@string/e_mount'),res.get('@string/e_mountm'))

        self.dsel.setProperty('text','')
        QTimer.singleShot (1000,self.loop)

    isdetail = False

    def MakeDetail (self):
        if self.isdetail:
            self.Details.setProperty('visible',False)
            self.ListView.setProperty('visible',True)
            self.isdetail = False
        else:
            self.Details.setProperty('visible',True)
            self.ListView.setProperty('visible',False)
            self.isdetail = True

    def __init__(self):
        super(MainApp, self).__init__()
        self.addDrivesModel()

        self.load (res.get('@layout/drives'))
        self.setProperty('title','Drives')
        app.launchedlogo(self.property('title'), res.etc('drives', 'logo'))
        self.dsel = self.findChild ('dsel')
        self.btnDetail = self.findChild ('btnDetail')
        self.btnDetail.clicked.connect (self.MakeDetail)
        self.Details = self.findChild ('Details')
        self.ListView = self.findChild ('ListView')
        self.ListView.setProperty('visible',True)

        self.loop()


application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('drives','logo'))))

w = MainApp()
application.exec()