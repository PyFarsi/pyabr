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
    i = 0

    def rename_(self,name):
        try:
            commands.mv ([files.filename (self.fselp),name])
        except:
            self.e = Text (res.get('@string/files.exists'),f'{name} {res.get("@string/files.existsm")}')
        self.addFileModel(files.readall('/proc/info/pwd'))

    def newfile_(self,name):
        if not (files.isfile (name) or files.isdir(name)):
            commands.touch ([name])
        else:
            self.e = Text (res.get('@string/files.exists'),f'{name} {res.get("@string/files.existsm")}')
        self.addFileModel(files.readall('/proc/info/pwd'))

    def newfolder_(self,name):
        if not (files.isdir (name) or files.isfile(name)):
            commands.mkdir ([name])
        else:
            self.e = Text (res.get('@string/files.exists'),f'{name} {res.get("@string/files.existsm")}')
        self.addFileModel(files.readall('/proc/info/pwd'))

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

            elif self.fsel.property('text').endswith('.py'):
                commands.cc ([self.fsel.property('text')])
                files.write ('/tmp/exec.sa',f"{self.fsel.property('text').replace('.py','')}\nrm /tmp/exec.sa\nrm {self.fsel.property('text')}c\nrm __pycache__\nshut")
                app.start ('commento','')

            elif self.fsel.property('text').endswith('.exe'):
                files.write ('/tmp/exec.sa',f"wine {self.fsel.property('text')}\nrm /tmp/exec.sa\nshut")
                app.start ('commento','')

            elif self.fsel.property('text').endswith('.jar'):
                files.write ('/tmp/exec.sa',f"java -jar {self.fsel.property('text')}\nrm /tmp/exec.sa\nshut")
                app.start ('commento','')

            elif self.fsel.property('text').endswith ('.desk'):
                try:
                    app.start (files.filename (self.fsel.property('text')).replace('.desk',''),'')
                except:
                    pass

            elif self.fsel.property('text').endswith ('.pa'):
                self.i = Install ( self.fsel.property('text'))

            elif self.fsel.property('text').endswith('.qml'):
                files.copy (self.fsel.property('text'),'/usr/share/layouts/debug.qml')
                app.start ('debug','')

        if not self.fsela.property('text')=='':
            self.fselp = self.fsela.property('text')

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
            if self.fselp.endswith('.pyc') or self.fselp.endswith('.pashm') or self.fselp.endswith('.pa') or self.fselp.endswith('.qml') or self.fselp.endswith('.py') or self.fselp.endswith('.sa') or self.fselp.endswith('.exe'):
                self._execute.setProperty('enabled',True)
            else:
                self._execute.setProperty('enabled',False)
            self._filex.setProperty('text',files.filename(self.fselp))

        if not (files.isfile ('/tmp/files-paste') or files.isdir ('/tmp/files-paste')): self._paste.setProperty('enabled',False)
        else:
            self._paste.setProperty('enabled',True)

        if files.isfile (self.fselp) or files.isdir (self.fselp):
            if self.act.property('text')=='cut':
                if files.isdir ('/tmp/files-paste') or files.isfile ('/tmp/files-paste'): commands.rm (['/tmp/files-paste'])
                commands.mv ([self.fselp,'/tmp/files-paste'])
                files.write ('/tmp/files-paste.name.tmp',files.filename(self.fselp))
                self._paste.setProperty('enabled',True)
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='copy':
                if files.isdir ('/tmp/files-paste') or files.isfile ('/tmp/files-paste'): commands.rm (['/tmp/files-paste'])
                commands.cp ([self.fselp,'/tmp/files-paste'])
                files.write ('/tmp/files-paste.name.tmp',files.filename(self.fselp))
                self._paste.setProperty('enabled',True)

            elif self.act.property('text')=='newfile':
                self.r = Input (res.get('@string/files.newfile'),self.newfile_)

            elif self.act.property('text')=='newfolder':
                self.r = Input (res.get('@string/files.newfolder'),self.newfolder_)

            elif self.act.property('text')=='paste':
                if files.isfile (files.readall('/tmp/files-paste.name.tmp')) or files.isdir (files.readall('/tmp/files-paste.name.tmp')):
                    if  files.isfile (files.readall('/tmp/files-paste.name.tmp')+" 1") or files.isdir (files.readall('/tmp/files-paste.name.tmp')+" 1"):
                        self.i+=1
                    else:
                        self.i=1
                else:
                    self.i=0

                if self.i>0:
                    commands.mv (['/tmp/files-paste',files.readall('/tmp/files-paste.name.tmp')+" "+str(self.i)])
                else:
                    commands.mv (['/tmp/files-paste',files.readall('/tmp/files-paste.name.tmp')])
                self._paste.setProperty('enabled',False)
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='rename':
                self.r = Input (f'{res.get("@string/files.rename")} {files.filename(self.fselp)}',self.rename_)

            elif self.act.property('text')=='delete':
                commands.rm ([self.fselp])
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='execute':
                if self.fselp.endswith('.pyc'):
                    files.write ('/tmp/exec.sa',files.output(self.fselp.replace('.pyc','').replace('.sa',''))+"\nrm /tmp/exec.sa\nshut")
                    app.start ('commento','')

                elif self.fselp.endswith('.pashm'):
                    files.write ('/tmp/exec.sa',f"pashmak {self.fselp}\nrm /tmp/exec.sa\nshut")
                    app.start ('commento','')

                elif self.fselp.endswith('.py'):
                    commands.cc ([self.fselp])
                    files.write ('/tmp/exec.sa',f"{self.fselp.replace('.py','')}\nrm /tmp/exec.sa\nrm {self.fselp}c\nrm __pycache__\nshut")
                    app.start ('commento','')

                elif self.fselp.endswith('.exe'):
                    files.write ('/tmp/exec.sa',f"wine {self.fselp}\nrm /tmp/exec.sa\nshut")
                    app.start ('commento','')

                elif self.fselp.endswith('.jar'):
                    files.write ('/tmp/exec.sa',f"java -jar {self.fselp}\nrm /tmp/exec.sa\nshut")
                    app.start ('commento','')

                elif self.fselp.endswith ('.desk'):
                    try:
                        app.start (files.filename (self.fselp).replace('.desk',''),'')
                    except:
                        pass

                elif self.fselp.endswith ('.pa'):
                    self.i = Install ( self.fselp)

                elif self.fselp.endswith('.qml'):
                    files.copy (self.fsel.property('text'),'/usr/share/layouts/debug.qml')
                    app.start ('debug','')

            self.act.setProperty('text','')
            
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
        self.fsela = self.findChild('fsela')

        self.contextMenu = self.findChild('contextMenu')
        self._open = self.findChild('open')
        self._open.setProperty('text',res.get('@string/files.open'))
        self._openwith = self.findChild('openwith')
        self._openwith.setProperty('text',res.get('@string/files.openwith'))
        self._execute = self.findChild('execute')
        self._execute.setProperty('text',res.get('@string/files.execute'))
        self._cut = self.findChild('cut')
        self._cut.setProperty('text',res.get('@string/files.cut'))
        self._copy = self.findChild('copy')
        self._copy.setProperty('text',res.get('@string/files.copy'))
        self._paste = self.findChild('paste')
        self._paste.setProperty('text',res.get('@string/files.paste'))
        self._rename = self.findChild('rename')
        self._rename.setProperty('text',res.get('@string/files.rename'))
        self._delete = self.findChild('delete')
        self._delete.setProperty('text',res.get('@string/files.delete'))
        self._newfile = self.findChild('newfile')
        self._newfile.setProperty('text',res.get('@string/files.newfile'))
        self._newfolder = self.findChild('newfolder')
        self._newfolder.setProperty('text',res.get('@string/files.newfolder'))
        self._filex = self.findChild('filex')
        self._info = self.findChild('info')
        self._info.setProperty('text',res.get('@string/files.info'))
        self.act = self.findChild('act')

        self.loop()



application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()