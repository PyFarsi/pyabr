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
import multiprocessing,subprocess,sys,random,shutil

class MainApp (MainApp):
    fselp = ''
    i = 0
    isdetail = False

    def addapp_(self,title):
        winappid = f"win{str(random.randint(1000,9999))}"
        desktopfile = f'/usr/share/applications/{winappid}.desk'
        executefile = f'/usr/app/{winappid}'

        files.create (desktopfile)
        control.write_record ('name[en]',title,desktopfile)
        control.write_record ('application','Yes',desktopfile)
        control.write_record ('category','tools',desktopfile)
        control.write_record ('hidden','No',desktopfile)
        control.write_record ('logo',f'@icon/{winappid}',desktopfile)
        control.write_record ('exec',winappid,desktopfile)

        files.write (f'{executefile}.sa',f'wine "{self.fselp}"')

        findlogo = subprocess.check_output(f'cd / && find -iname *{title}*.png',shell=True).decode ('utf-8').split('\n')

        for i in findlogo:
            if '128x128' in i and i.startswith('./root/.local'):
                shutil.copyfile (i.replace('./root','/root'),f'/stor/usr/share/icons/{winappid}.png')
                break

        app.signal ('apps')
        app.signal ('dock')

    def rename_(self,name):
        try:
            if permissions.check(f'{files.output(self.fselp)}', "r", files.readall("/proc/info/su")) and permissions.check(f'{files.output(name)}', "w", files.readall("/proc/info/su")):
                commands.mv ([files.filename (self.fselp),name])
            else:
                self.e = Perm()
        except:
            self.e = Text (res.get('@string/exists').replace('{0}',name),res.get("@string/exists_message").replace('{0}',name))
        self.addFileModel(files.readall('/proc/info/pwd'))

    def newfile_(self,name):
        if not (files.isfile (name) or files.isdir(name)):
            if permissions.check(f'{files.output(name)}', "w", files.readall("/proc/info/su")):
                commands.touch ([name])
            else:
                self.e = Perm()
        else:
            self.e = Text (res.get('@string/exists').replace('{0}',name),res.get("@string/exists_message").replace('{0}',name))
        self.addFileModel(files.readall('/proc/info/pwd'))

    def newfolder_(self,name):
        if not (files.isdir (name) or files.isfile(name)):
            if permissions.check(f'{files.output(name)}', "w", files.readall("/proc/info/su")):
                commands.mkdir ([name])
            else:
                self.e = Perm()
        else:
            self.e = Text (res.get('@string/exists').replace('{0}',name),res.get("@string/exists_message").replace('{0}',name))
        self.addFileModel(files.readall('/proc/info/pwd'))

    def loop (self):
        if not self.fsel.property('text')=='':

            if files.isdir (self.fsel.property('text')) or self.fsel.property('text')=='..':
                if permissions.check(f'{files.output(files.parentdir(self.fsel.property("text")))}', "r", files.readall("/proc/info/su")):
                    print(self.fsel.property('text'))
                    System (f'cd "{self.fsel.property("text")}"')
                    self.addFileModel(files.readall('/proc/info/pwd'))
                    self.title.setProperty('text',files.readall('/proc/info/pwd'))
                else:
                    self.e = Perm()

            elif self.fsel.property('text').endswith('.pyc'):
                if permissions.check(f'{files.output(self.fsel.property("text"))}', "x", files.readall("/proc/info/su")):
                    files.write ('/tmp/exec.sa',files.output(self.fsel.property('text').replace('.pyc','').replace('.sa',''))+"\nrm /tmp/exec.sa\nshut")
                    app.start ('commento','')
                else:
                    self.e = Perm()

            elif self.fsel.property('text').endswith('.pashm'):
                if permissions.check(f'{files.output(self.fsel.property("text"))}', "x", files.readall("/proc/info/su")):
                    files.write ('/tmp/exec.sa',f"pashmak {self.fsel.property('text')}\nrm /tmp/exec.sa\nshut")
                    app.start ('commento','')
                else:
                    self.e = Perm()

            elif self.fsel.property('text').endswith('.py'):
                if permissions.check(f'{files.output(self.fsel.property("text"))}', "x", files.readall("/proc/info/su")):
                    commands.cc ([self.fsel.property('text')])
                    files.write ('/tmp/exec.sa',f"{self.fsel.property('text').replace('.py','')}\nrm /tmp/exec.sa\nrm {self.fsel.property('text')}c\nrm __pycache__\nshut")
                    app.start ('commento','')
                else:
                    self.e = Perm()

            elif self.fsel.property('text').endswith('.exe'):
                if permissions.check(f'{files.output(self.fsel.property("text"))}', "x", files.readall("/proc/info/su")):
                    app.start ('wine',self.fsel.property('text'))
                else:
                    self.e = Perm()

            elif self.fsel.property('text').endswith('.jar'):
                if permissions.check(f'{files.output(self.fsel.property("text"))}', "x", files.readall("/proc/info/su")):
                    files.write ('/tmp/exec.sa',f"java -jar {self.fsel.property('text')}\nrm /tmp/exec.sa\nshut")
                    app.start ('commento','')
                else:
                    self.e = Perm()

            elif self.fsel.property('text').endswith ('.desk'):
                try:
                    app.start (files.filename (self.fsel.property('text')).replace('.desk',''),'')
                except:
                    pass

            elif self.fsel.property('text').endswith ('.pa'):
                if permissions.check(f'{files.output(self.fsel.property("text"))}', "x", files.readall("/proc/info/su")):
                    self.i = Install ( self.fsel.property('text'))
                else:
                    self.e = Perm()

            elif self.fsel.property('text').endswith('.qml'):
                if permissions.check(f'{files.output(self.fsel.property("text"))}', "x", files.readall("/proc/info/su")):
                    files.copy (self.fsel.property('text'),'/usr/share/layouts/debug.qml')
                    app.start ('debug','')
                else:
                    self.e = Perm()

            else:
                if permissions.check(f'{files.output(self.fsel.property("text"))}', "r", files.readall("/proc/info/su")):
                    ext = os.path.splitext(self.fsel.property("text"))[1].replace('.','')

                    if control.read_record (f'{ext}.always','/etc/ext')==None:
                        self.x = OpenWith(files.output(self.fsel.property("text")))
                    else:
                        app.start (control.read_record (f'{ext}.always','/etc/ext'),files.output(self.fsel.property("text")))
                else:
                    self.e = Perm()

        if not self.fsela.property('text')=='':
            self.fselp = self.fsela.property('text')

        if self.fselp=='':
            self.contextMenu.setProperty('visible',False)

        elif files.isdir (self.fselp):
            self._open.setProperty('enabled',False)
            self._openwith.setProperty('enabled',False)
            self._execute.setProperty('enabled',False)
            self._filex.setProperty('text',files.filename(self.fselp))
            self.compressto.setProperty('enabled',True)
            self.cloudops.setProperty('enabled',False)
            self.extract.setProperty('enabled',False)
            self.shortcut.setProperty ('enabled',False)

        elif files.isfile (self.fselp):
            self.compressto.setProperty('enabled',False)
            self.cloudops.setProperty('enabled',True)
            self._open.setProperty('enabled',True)
            self._openwith.setProperty('enabled',True)
            if self.fselp.endswith('.exe'):
                self.shortcut.setProperty ('enabled',True)
            else:
                self.shortcut.setProperty ('enabled',False)
            if self.fselp.endswith('.zip') or self.fselp.endswith('.tar.xz') or self.fselp.endswith('.tar.gz') or self.fselp.endswith('.tar.bz2') or self.fselp.endswith('.tar'):
                self.extract.setProperty('enabled',True)
            else:
                self.extract.setProperty('enabled',False)
            if self.fselp.endswith('.pyc') or self.fselp.endswith('.pashm') or self.fselp.endswith('.pa') or self.fselp.endswith('.qml') or self.fselp.endswith('.py') or self.fselp.endswith('.sa') or self.fselp.endswith('.exe'):
                self._execute.setProperty('enabled',True)
            else:
                self._execute.setProperty('enabled',False)
            self._filex.setProperty('text',files.filename(self.fselp))

        if not (files.isfile ('/tmp/files-paste') or files.isdir ('/tmp/files-paste')): self._paste.setProperty('enabled',False)
        else:
            self._paste.setProperty('enabled',True)

        if self.act.property('text')=='connectcloud':
            self.w = CloudConnector()

        if files.isfile (self.fselp) or files.isdir (self.fselp):
            if self.act.property('text')=='cut':
                if permissions.check(f'{files.output(self.fselp)}', "r", files.readall("/proc/info/su")):

                    if files.isdir ('/tmp/files-paste') or files.isfile ('/tmp/files-paste'): 
                        commands.rm (['/tmp/files-paste'])

                    commands.mv ([self.fselp,'/tmp/files-paste'])
                    files.write ('/tmp/files-paste.name.tmp',files.filename(self.fselp))
                    self._paste.setProperty('enabled',True)
                    self.addFileModel(files.readall('/proc/info/pwd'))
                
                else:
                    self.e = Perm()

            elif self.act.property('text')=='copy':
                if permissions.check(f'{files.output(self.fselp)}', "r", files.readall("/proc/info/su")):
                    if files.isdir ('/tmp/files-paste') or files.isfile ('/tmp/files-paste'): commands.rm (['/tmp/files-paste'])
                    commands.cp ([self.fselp,'/tmp/files-paste'])
                    files.write ('/tmp/files-paste.name.tmp',files.filename(self.fselp))
                    self._paste.setProperty('enabled',True)
                else:
                    self.e = Perm()

            elif self.act.property('text')=='newfile':
                if permissions.check(f'{files.output(self.fselp)}', "w", files.readall("/proc/info/su")):
                    self.r = Input (res.get('@string/newfile'),self.newfile_)
                else:
                    self.e = Perm()

            elif self.act.property('text')=='newfolder':
                if permissions.check(f'{files.output(self.fselp)}', "w", files.readall("/proc/info/su")):
                    self.r = Input (res.get('@string/newfolder'),self.newfolder_)
                else:
                    self.e = Perm()

            elif self.act.property('text')=='paste':
                if files.isfile (files.readall('/tmp/files-paste.name.tmp')) or files.isdir (files.readall('/tmp/files-paste.name.tmp')):
                    if  files.isfile (files.readall('/tmp/files-paste.name.tmp')+" 1") or files.isdir (files.readall('/tmp/files-paste.name.tmp')+" 1"):
                        self.i+=1
                    else:
                        self.i=1
                else:
                    self.i=0

                if self.i>0:
                    if permissions.check(files.output(files.readall('/tmp/files-paste.name.tmp')+" "+str(self.i)), "w", files.readall("/proc/info/su")):
                        commands.mv (['/tmp/files-paste',files.readall('/tmp/files-paste.name.tmp')+" "+str(self.i)])
                    else:
                        self.e = Perm()
                else:
                    if permissions.check(files.output(files.readall('/tmp/files-paste.name.tmp')), "w", files.readall("/proc/info/su")):
                        commands.mv (['/tmp/files-paste',files.readall('/tmp/files-paste.name.tmp')])
                    else:
                        self.e = Perm()

                self._paste.setProperty('enabled',False)
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='rename':
                if permissions.check(f'{files.output(self.fselp)}', "r", files.readall("/proc/info/su")):
                    self.r = Input (f'{res.get("@string/rename")} {files.filename(self.fselp)}',self.rename_)
                else:
                    self.e = Perm()

            elif self.act.property('text')=='delete':
                if permissions.check(f'{files.output(self.fselp)}', "w", files.readall("/proc/info/su")):
                    commands.rm ([self.fselp])
                    self.addFileModel(files.readall('/proc/info/pwd'))
                else:
                    self.e = Perm()

            elif self.act.property('text')=='execute':
                if permissions.check(f'{files.output(self.fselp)}', "x", files.readall("/proc/info/su")):
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
                        app.start ('wine',f"wine '{self.fselp}'")

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
                else:
                    self.e = Perm()

            elif self.act.property('text')=='openwith':
                if permissions.check(f'{files.output(self.fselp)}', "r", files.readall("/proc/info/su")):
                    self.x = OpenWith(self.fselp)
                else:
                    self.e = Perm()

            elif self.act.property('text')=='open':
                if permissions.check(f'{files.output(self.fselp)}', "r", files.readall("/proc/info/su")):
                    ext = os.path.splitext(self.fselp)[1].replace('.','')

                    if control.read_record (f'{ext}.always','/etc/ext')==None:
                        self.x = OpenWith(self.fselp)
                    else:
                        app.start (control.read_record (f'{ext}.always','/etc/ext'),self.fselp)
                else:
                    self.e = Perm()

            elif self.act.property('text')=='up':
                d = Drive()
                d.Upload (self.fselp)
            
            elif self.act.property('text')=='down':
                d = Drive()
                d.Download (self.fselp)

            elif self.act.property('text')=='ziro':
                d = Drive()
                d.Upload (self.fselp)
                files.create (self.fselp)

            elif self.act.property('text')=='link':
                d = Drive()
                self.x = Sharelink(res.get('@string/sharelink'),d.Link(self.fselp))

            elif self.act.property('text')=='info':
                self.x = FileInfo (self.fselp)

            elif self.act.property('text')=='zipc':
                commands.zip ([self.fselp])
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='xzc':
                commands.xzip ([self.fselp])
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='gzc':
                commands.gzip ([self.fselp])
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='tarc':
                commands.tar ([self.fselp])
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='bzc':
                commands.bzip ([self.fselp])
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='shortcut':
                self.s = Input ("Choose name",self.addapp_)

            elif self.act.property('text')=='extract':
                if self.fselp.endswith('.zip'):
                    commands.unzip ([self.fselp,self.fselp.replace('.zip','')])
                elif self.fselp.endswith('.tar.xz'):
                    commands.xunzip ([self.fselp,self.fselp.replace('.tar.xz','')])
                elif self.fselp.endswith('.tar.bz2'):
                    commands.bunzip ([self.fselp,self.fselp.replace('.tar.bz2','')])
                elif self.fselp.endswith('.tar.gz'):
                    commands.gunzip ([self.fselp,self.fselp.replace('.tar.gz','')])
                elif self.fselp.endswith('.tar'):
                    commands.untar ([self.fselp,self.fselp.replace('.tar','')])
                self.addFileModel(files.readall('/proc/info/pwd'))

            elif self.act.property('text')=='details':
                if self.isdetail:
                    self.ListView.setProperty('visible',True)
                    self.Details.setProperty('visible',False)
                    self.isdetail = False
                else:
                    self.ListView.setProperty('visible',False)
                    self.Details.setProperty('visible',True)
                    self.isdetail = True

            self.act.setProperty('text','')
            
        self.fsel.setProperty('text','')
        QTimer.singleShot (10,self.loop)

    def __init__(self):
        super(MainApp, self).__init__()

        if not sys.argv[1:]==[]:
            self.addFileModel(sys.argv[1])
        else:
            self.addFileModel(files.readall('/proc/info/pwd'))

            
        self.load (res.get('@layout/files'))
        try:
            self.setProperty('title',res.get('@string/files'))
        except:
            pass
        self.fsel = self.findChild ('fsel')
        self.fsela = self.findChild('fsela')
        self.title =self.findChild('title')

        if not sys.argv[1:]==[]:
            self.title.setProperty('text',sys.argv[1])
        else:
            self.title.setProperty('text',files.readall('/proc/info/pwd'))
            
        self.contextMenu = self.findChild('contextMenu')
        self._open = self.findChild('open')
        self._open.setProperty('text',res.get('@string/open'))
        self._openwith = self.findChild('openwith')
        self._openwith.setProperty('text',res.get('@string/openwith'))
        self._execute = self.findChild('execute')
        self._execute.setProperty('text',res.get('@string/execute'))
        self._cut = self.findChild('cut')
        self._cut.setProperty('text',res.get('@string/cut'))
        self._copy = self.findChild('copy')
        self._copy.setProperty('text',res.get('@string/copy'))
        self._paste = self.findChild('paste')
        self._paste.setProperty('text',res.get('@string/paste'))
        self._rename = self.findChild('rename')
        self._rename.setProperty('text',res.get('@string/rename'))
        self._delete = self.findChild('delete')
        self._delete.setProperty('text',res.get('@string/delete'))
        self._newfile = self.findChild('newfile')
        self._newfile.setProperty('text',res.get('@string/newfile'))
        self._newfolder = self.findChild('newfolder')
        self._newfolder.setProperty('text',res.get('@string/newfolder'))
        self._filex = self.findChild('filex')
        self._info = self.findChild('info')
        self._info.setProperty('text',res.get('@string/info'))
        self._upcloud = self.findChild('upcloud')
        self._upcloud.setProperty('text',res.get('@string/upload'))
        self._downcloud = self.findChild('downcloud')
        self._downcloud.setProperty('text',res.get('@string/download'))
        self._ziro = self.findChild('ziro')
        self._ziro.setProperty('text',res.get('@string/ziro'))
        self.act = self.findChild('act')

        self.zipc = self.findChild('zipc')
        self.xzc = self.findChild('xzc')
        self.gzc = self.findChild('gzc')
        self.bzc = self.findChild('bzc')
        self.tarc = self.findChild('tarc')
        self.compressto = self.findChild('compressto')
        self.compressto.setProperty('text',res.get('@string/compress'))
        self.cloudops = self.findChild('cloudops')
        self.cloudops.setProperty('text',res.get('@string/cloud_o'))
        self.extract = self.findChild('extract')
        self.extract.setProperty('text',res.get('@string/extract'))
        self.ListView = self.findChild ('ListView')
        self.shortcut = self.findChild ('shortcut')
        self.Details = self.findChild ('Details')

        self.loop()

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('files','logo'))))

w = MainApp()
application.exec()