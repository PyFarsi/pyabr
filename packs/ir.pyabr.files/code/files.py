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

from typing import SupportsBytes
from pyabr.core import *
from pyabr.quick import *
import multiprocessing,subprocess

class MainApp (MainApp):

    def loop (self):
        if not self.fsel.property('text')=='':

            if files.isdir (self.fsel.property('text')) or self.fsel.property('text')=='..':
                commands.cd ([self.fsel.property('text')])
                self.addFileModel(files.readall('/proc/info/pwd'))


            elif self.fsel.property('text').endswith('.pyc'):
                files.write ('/tmp/exec.sa',files.output(self.fsel.property('text').replace('.pyc','').replace('.sa',''))+"\nrm /tmp/exec.sa\nshut")
                app.start ('commento','')

            elif self.fsel.property('text').endswith('.pashm'):
                files.write ('/tmp/exec.sa','pashmak '+files.output(self.fsel.property('text'))+"\nrm /tmp/exec.sa\nshut")
                app.start ('commento','')


        self.fsel.setProperty('text','')
        QTimer.singleShot (10,self.loop)

    def __init__(self):
        super(MainApp, self).__init__()

        self.addFileModel('/')
        self.load (res.get('@layout/files'))
        try:
            self.setProperty('title',res.get('@string/files.app_name'))
        except:
            pass
        self.fsel = self.findChild ('fsel')
        self.loop()


application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()