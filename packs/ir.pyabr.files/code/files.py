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
    fselp = ''
    def loop (self):
        if not self.fsel.property('text')=='':

            if files.isdir (self.fsel.property('text')) or self.fsel.property('text')=='..':
                commands.cd ([self.fsel.property('text')])
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.fsel.property('text').endswith('.pyc'):
                files.write ('/tmp/exec.sa',files.output(self.fsel.property('text').replace('.pyc','').replace('.sa',''))+"\nrm /tmp/exec.sa\nshut")
                app.start ('commento','')

            elif self.fsel.property('text').endswith('.pashm'):
                files.write ('/tmp/exec.sa',f"pashmak {self.fsel.property('text')}\nrm /tmp/exec.sa\nshut")
                app.start ('commento','')

            elif self.fsel.property('text').endswith ('.desk'):
                try:
                    app.start (files.filename (self.fsel.property('text')).replace('.desk',''),'')
                except:
                    pass

            elif self.fsel.property('text').endswith ('.pa'):
                self.i = Install ( self.fsel.property('text'))

            self.fselp = self.fsel.property('text')

        if self.fselp=='':
            self.contextMenu.setProperty('visible',False)
        elif files.isdir (self.fselp):
            self._open.setProperty('enabled',False)
            self._openwith.setProperty('enabled',False)
            self._execute.setProperty('enabled',False)
            self._filex.setProperty('text',files.filename(self.fselp))
        elif files.isfile (self.fselp):
            self._open.setProperty('enabled',True)
            self._openwith.setProperty('enabled',True)
            self._execute.setProperty('enabled',True)
            self._filex.setProperty('text',files.filename(self.fselp))
            
        self.fsel.setProperty('text','')
        QTimer.singleShot (10,self.loop)

    def __init__(self):
        super(MainApp, self).__init__()

        self.addFileModel(files.readall('/proc/info/pwd'))
        self.load (res.get('@layout/files'))
        try:
            self.setProperty('title',res.get('@string/files.app_name'))
        except:
            pass
        self.fsel = self.findChild ('fsel')

        self.contextMenu = self.findChild('contextMenu')
        self._open = self.findChild('open')
        self._openwith = self.findChild('openwith')
        self._execute = self.findChild('execute')
        self._cut = self.findChild('cut')
        self._copy = self.findChild('copy')
        self._paste = self.findChild('paste')
        self._rename = self.findChild('rename')
        self._delete = self.findChild('delete')
        self._filex = self.findChild('filex')
        self._info = self.findChild('info')

        self.loop()



application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()